from django.urls import path
from .views import ListBankView, FromIFSCView


urlpatterns = [
    path('banks/', ListBankView.as_view(), name="banks-all"),
    path('banks/<str:pk>/', FromIFSCView.as_view(), name="from-ifsc"),
]
