# Generated by Django 4.1.1 on 2022-09-29 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_rename_description_jpn_about_description_ja_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='background_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='article',
            name='background_ja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='article',
            name='background_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
    ]
