# Generated by Django 4.1.1 on 2022-09-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_certificate_alter_brand_image_certificateimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='background',
            name='lang',
            field=models.IntegerField(choices=[(0, 'English'), (1, 'Uzbek'), (2, 'Japanese')], default=0, null=True),
        ),
    ]
