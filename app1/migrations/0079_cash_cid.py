# Generated by Django 4.2.1 on 2023-08-18 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0078_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='cid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.company'),
            preserve_default=False,
        ),
    ]