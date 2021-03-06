# Generated by Django 3.0.10 on 2021-08-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0008_auto_20210824_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('communceName', models.CharField(max_length=50, null=True)),
                ('province', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countryConde', models.CharField(max_length=10, null=True)),
                ('CountryName', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtName', models.CharField(max_length=50, null=True)),
                ('communce', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceName', models.CharField(max_length=50, null=True)),
                ('country_code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=10, null=True)),
                ('userImage', models.ImageField(upload_to='')),
                ('phone', models.CharField(max_length=10, null=True)),
                ('nationality', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('dateBirth', models.DateField(null=True)),
                ('jobs', models.CharField(max_length=10, null=True)),
                ('organization', models.CharField(max_length=10, null=True)),
                ('village', models.CharField(max_length=10, null=True)),
                ('district', models.CharField(max_length=10, null=True)),
                ('communce', models.CharField(max_length=10, null=True)),
                ('province', models.CharField(max_length=10, null=True)),
                ('proID', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_created=True, null=True)),
                ('proName', models.CharField(max_length=50, null=True)),
                ('ProShort', models.CharField(max_length=50, null=True)),
                ('lastUdate', models.DateTimeField(null=True)),
                ('createdBy', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villageName', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
