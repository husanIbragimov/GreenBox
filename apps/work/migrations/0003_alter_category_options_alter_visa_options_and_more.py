# Generated by Django 4.1.1 on 2022-09-28 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_category_options_alter_expertiselevel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories', 'verbose_name_plural': '1.1. Categories'},
        ),
        migrations.AlterModelOptions(
            name='visa',
            options={'verbose_name': 'Visas', 'verbose_name_plural': '1.2. Visas'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Work', 'verbose_name_plural': '1.0. Work'},
        ),
    ]
