# Generated by Django 4.1.1 on 2022-09-29 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_remove_about_background_en_and_more'),
        ('work', '0003_alter_category_options_alter_visa_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='industry_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='industry_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary_ja',
            field=models.CharField(help_text='For example ($2500 - 3000 / month)', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary_uz',
            field=models.CharField(help_text='For example ($2500 - 3000 / month)', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='title_ja',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='title_uz',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='visa',
            name='background_ja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.background'),
        ),
        migrations.AddField(
            model_name='visa',
            name='background_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.background'),
        ),
        migrations.AddField(
            model_name='visa',
            name='category_ja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='work.category'),
        ),
        migrations.AddField(
            model_name='visa',
            name='category_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='work.category'),
        ),
        migrations.AddField(
            model_name='visa',
            name='description_ja',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='visa',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='visa',
            name='title_ja',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='visa',
            name='title_uz',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='background_ja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='work',
            name='background_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='work',
            name='description_ja',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='title_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
