# Generated by Django 4.1.1 on 2022-09-29 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_study_created_at_study_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories', 'verbose_name_plural': '1. Categories'},
        ),
        migrations.AlterModelOptions(
            name='study',
            options={'verbose_name': 'Study', 'verbose_name_plural': '2. Study'},
        ),
        migrations.AlterModelOptions(
            name='studyblog',
            options={'verbose_name': 'Study Blogs', 'verbose_name_plural': '3. Study Blogs'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'Universities', 'verbose_name_plural': '4. Universities'},
        ),
    ]
