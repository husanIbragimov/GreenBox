# Generated by Django 4.1.1 on 2022-09-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_remove_background_lang_background_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='description_jp',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='About title'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_jp',
            field=models.CharField(max_length=100, null=True, verbose_name='About title'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='About title'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_jp',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Article title'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_jp',
            field=models.CharField(max_length=100, null=True, verbose_name='Article title'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Article title'),
        ),
        migrations.AddField(
            model_name='background',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='background',
            name='title_jp',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='background',
            name='title_uz',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Brand title'),
        ),
        migrations.AddField(
            model_name='brand',
            name='title_jp',
            field=models.CharField(max_length=100, null=True, verbose_name='Brand title'),
        ),
        migrations.AddField(
            model_name='brand',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Brand title'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='description_jp',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='description_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Certificate title'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='title_jp',
            field=models.CharField(max_length=100, null=True, verbose_name='Certificate title'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Certificate title'),
        ),
        migrations.AlterField(
            model_name='background',
            name='status',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'TOP'), (2, 'MIDDLE'), (3, 'BOTTOM')], default=0, verbose_name='Status'),
        ),
    ]