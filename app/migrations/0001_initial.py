# Generated by Django 5.1.6 on 2025-05-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('application_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='fertilizer_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='harverst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_variety', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='harvest_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='landprep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(max_length=100)),
                ('cultivation_area', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('fertilizer', models.CharField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='landprep_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_variety', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='packaging_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='packing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('avg_sale_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='packing_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Procurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procurer_name', models.CharField(max_length=100)),
                ('farmer_name', models.CharField(max_length=100)),
                ('seed_variety', models.CharField(max_length=100)),
                ('lot_id', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('avg_price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='procurement_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transplanting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('seed_variety', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('photo', models.ImageField(upload_to='transportation_photos/')),
                ('belongs_to', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
