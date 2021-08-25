from django.db import models

class UserInfo(models.Model):
    userID = models.CharField(max_length=10,null=True)
    userImage = models.ImageField()
    phone = models.CharField(max_length=10,null=True)
    nationality = models.CharField(max_length=10,null=True)
    gender = models.CharField(max_length=10,null=True)
    dateBirth = models.DateField(null=True)
    jobs = models.CharField(max_length=10,null=True)
    organization = models.CharField(max_length=10,null=True)
    village = models.CharField(max_length=10,null=True)
    district = models.CharField(max_length=10,null=True)
    communce = models.CharField(max_length=10,null=True)
    province = models.CharField(max_length=10,null=True)
    proID = models.CharField(max_length=10,null=True)

class Countries(models.Model):
    countryConde = models.CharField(max_length=10,null=True)
    CountryName = models.CharField(max_length=50,null=True)

class Village(models.Model):
    villageName = models.CharField(max_length=50,null=True)
    district = models.CharField(max_length=50,null=True)

class District(models.Model):
    districtName = models.CharField(max_length=50,null=True)
    communce = models.CharField(max_length=50,null=True)

class Communce(models.Model):
    communceName = models.CharField(max_length=50,null=True)
    province = models.CharField(max_length=50,null=True)

class Provice(models.Model):
    provinceName= models.CharField(max_length=50,null=True)
    country_code = models.CharField(max_length=50,null=True)

class UserProfile(models.Model):
    proName = models.CharField(max_length=50,null=True)
    ProShort = models.CharField(max_length=50,null=True)
    createdDate = models.DateTimeField(auto_created=True,null=True)
    lastUdate = models.DateTimeField(null=True)
    createdBy = models.CharField(max_length=50,null=True)
