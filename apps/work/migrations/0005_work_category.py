# Generated by Django 4.1.1 on 2022-09-29 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_category_title_ja_category_title_uz_job_industry_ja_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='work.category'),
        ),
    ]
