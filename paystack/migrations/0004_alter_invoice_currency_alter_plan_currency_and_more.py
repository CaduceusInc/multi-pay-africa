# Generated by Django 4.0.3 on 2022-04-05 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paystack', '0003_subaccount_primary_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(choices=[('NGN', 'NGN'), ('USD', 'USD'), ('ZAR', 'ZAR'), ('GHS', 'GHS')], default='NGN', help_text='Three-letter ISO currency. Allowed values are: NGN, GHS, ZAR or USD', max_length=3, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='currency',
            field=models.CharField(choices=[('NGN', 'NGN'), ('USD', 'USD'), ('ZAR', 'ZAR'), ('GHS', 'GHS')], help_text='Currency in which amount is set. Allowed values are NGN, GHS, ZAR or USD', max_length=50, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='refund',
            name='currency',
            field=models.CharField(choices=[('NGN', 'NGN'), ('USD', 'USD'), ('ZAR', 'ZAR'), ('GHS', 'GHS')], help_text='Three-letter ISO currency. Allowed values are: NGN, GHS, ZAR or USD', max_length=3, verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='subaccount',
            name='account_number',
            field=models.CharField(help_text='Bank Account Number', max_length=100, verbose_name='Account number'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.CharField(choices=[('NGN', 'NGN'), ('USD', 'USD'), ('ZAR', 'ZAR'), ('GHS', 'GHS')], default='NGN', help_text='Currency of transaction', max_length=4, verbose_name='Currency'),
        ),
    ]
