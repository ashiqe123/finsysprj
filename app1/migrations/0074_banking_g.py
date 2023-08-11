# Generated by Django 4.2.1 on 2023-08-11 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0073_alter_challanitem_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='banking_G',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=100)),
                ('ifsccode', models.CharField(max_length=20)),
                ('branchname', models.CharField(max_length=100)),
                ('openingbalance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.company')),
            ],
        ),
    ]
