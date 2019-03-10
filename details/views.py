from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import Bank
from .serializers import BankSerializer


class ListBankView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class FromIFSCView(generics.RetrieveAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get(self, request, *args, **kwargs):
        try:
            bank = self.queryset.get(ifsc=kwargs["pk"].upper())
            return Response(BankSerializer(bank).data)

        except Bank.DoesNotExist:
            return Response(
                data={
                    "message": "Bank does not exist"
                },
                status=status.HTTP_404_NOT_FOUND
            )

