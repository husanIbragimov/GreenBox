# Generated by Django 4.1.1 on 2022-09-27 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_background_lang'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Articles', 'verbose_name_plural': '2. Articles'},
        ),
        migrations.AlterModelOptions(
            name='background',
            options={'verbose_name': 'Backgrounds', 'verbose_name_plural': '1. Backgrounds'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Brands', 'verbose_name_plural': '4. Brands'},
        ),
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': 'Certificates', 'verbose_name_plural': '5. Certificates'},
        ),
    ]
