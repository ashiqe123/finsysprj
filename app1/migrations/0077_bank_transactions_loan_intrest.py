# Generated by Django 4.2.1 on 2023-09-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0076_bank_transactions_loan_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_transactions',
            name='loan_intrest',
            field=models.TextField(blank=True, null=True),
        ),
    ]
