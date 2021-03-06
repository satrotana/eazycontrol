# Generated by Django 3.0.10 on 2021-08-23 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communce_name', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=10)),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=50)),
                ('commnuce', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to='')),
                ('phone', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('jobs', models.CharField(max_length=10)),
                ('organization', models.CharField(max_length=10)),
                ('village', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=10)),
                ('communce', models.CharField(max_length=10)),
                ('province', models.CharField(max_length=10)),
                ('user_profile', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('profile_name', models.CharField(max_length=50)),
                ('Pro_shortName', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
                ('created_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(max_length=50)),
            ],
        ),
    ]
