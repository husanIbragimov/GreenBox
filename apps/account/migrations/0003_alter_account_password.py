# Generated by Django 4.1.1 on 2022-09-26 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=64, verbose_name='Password'),
        ),
    ]
