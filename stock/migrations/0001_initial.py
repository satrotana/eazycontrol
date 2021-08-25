# Generated by Django 3.0.10 on 2021-08-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communce_name', models.CharField(max_length=50, null=True)),
                ('province', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=10, null=True)),
                ('country_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50, null=True)),
                ('communce', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=50, null=True)),
                ('country_code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, null=True)),
                ('user_image', models.ImageField(upload_to='')),
                ('phone', models.CharField(max_length=10, null=True)),
                ('nationality', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('jobs', models.CharField(max_length=10, null=True)),
                ('organization', models.CharField(max_length=10, null=True)),
                ('village', models.CharField(max_length=10, null=True)),
                ('district', models.CharField(max_length=10, null=True)),
                ('communce', models.CharField(max_length=10, null=True)),
                ('province', models.CharField(max_length=10, null=True)),
                ('profile_id', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True, null=True)),
                ('profile_name', models.CharField(max_length=50, null=True)),
                ('Pro_shortName', models.CharField(max_length=50, null=True)),
                ('last_update', models.DateTimeField(null=True)),
                ('created_by', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]