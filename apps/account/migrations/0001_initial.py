# Generated by Django 4.1.1 on 2022-09-25 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, db_index=True, max_length=50, null=True, unique=True, verbose_name='Email')),
                ('first_name', models.CharField(max_length=100, verbose_name='Ismi')),
                ('last_name', models.CharField(max_length=100, verbose_name='Familiyasi')),
                ('username', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Username')),
                ('phone', models.CharField(db_index=True, help_text='9 ta raqam bolishi kerak, masalan: 979998877', max_length=9, unique=True, verbose_name='Raqami*')),
                ('gender', models.IntegerField(choices=[(0, 'None'), (1, 'Male'), (2, 'female')], default=0, verbose_name='Jinsi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Xodim')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin foydalanuvchi')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super foydalanuvchi')),
                ('date_login', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sanasi')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sanasi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
