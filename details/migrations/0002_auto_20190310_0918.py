# Generated by Django 2.1.7 on 2019-03-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=35)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=35)),
                ('bank_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
    ]