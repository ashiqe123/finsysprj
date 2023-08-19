# Generated by Django 4.2.1 on 2023-08-18 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0073_alter_challanitem_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='bankings_G',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=100)),
                ('ifsccode', models.CharField(max_length=20)),
                ('branchname', models.CharField(max_length=100)),
                ('openingbalance', models.IntegerField()),
                ('date', models.DateField()),
                ('balance', models.IntegerField()),
                ('cash_balance', models.IntegerField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
        migrations.CreateModel(
            name='bank_transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_type', models.TextField(max_length=100)),
                ('from_trans', models.TextField(max_length=100)),
                ('to_trans', models.TextField(max_length=100)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('adj_date', models.DateField(blank=True, null=True)),
                ('desc', models.TextField(max_length=100)),
                ('type', models.TextField(max_length=100)),
                ('cash_adjust', models.TextField(max_length=100)),
                ('cash_cash', models.IntegerField(blank=True, null=True)),
                ('cash_description', models.TextField(max_length=100)),
                ('cash_date', models.DateField(blank=True, null=True)),
                ('banking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.bankings_g')),
            ],
        ),
    ]