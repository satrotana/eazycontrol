from django.db import models
from django.db.models.fields import DateField

class UserInfo(models.Model):
    userID = models.CharField(max_length=150,null=True)
    userImage = models.ImageField()
    phone = models.CharField(max_length=150,null=True)
    nationality = models.CharField(max_length=1250,null=True)
    gender = models.CharField(max_length=150,null=True)
    dateBirth = models.DateField(null=True)
    jobs = models.CharField(max_length=150,null=True)
    organization = models.CharField(max_length=1250,null=True)
    village = models.CharField(max_length=150,null=True)
    district = models.CharField(max_length=150,null=True)
    communce = models.CharField(max_length=150,null=True)
    province = models.CharField(max_length=150,null=True)
    proID = models.CharField(max_length=150,null=True)

class Countries(models.Model):
    countryConde = models.CharField(max_length=150,null=True)
    CountryName = models.CharField(max_length=250,null=True)

class Village(models.Model):
    villageName = models.CharField(max_length=250,null=True)
    district = models.CharField(max_length=250,null=True)

class District(models.Model):
    districtName = models.CharField(max_length=250,null=True)
    communce = models.CharField(max_length=250,null=True)

class Communce(models.Model):
    communceName = models.CharField(max_length=250,null=True)
    province = models.CharField(max_length=250,null=True)

class Provice(models.Model):
    provinceName= models.CharField(max_length=250,null=True)
    countryCode = models.CharField(max_length=250,null=True)

class UserProfile(models.Model):
    proName = models.CharField(max_length=250,null=True)
    ProShort = models.CharField(max_length=250,null=True)
    createdDate = models.DateTimeField(auto_created=True,null=True)
    lastUdate = models.DateTimeField(null=True)
    createdBy = models.CharField(max_length=250,null=True)

class Books(models.Model):
    bookCode = models.CharField(max_length=250,null=True)
    categoryID = models.CharField(max_length=250,null=True)
    bookTitle = models.CharField(max_length=250,null=True)
    dateIn = models.DateTimeField();
    inputer = models.CharField(max_length=250,null=True)
    releaseYear = models.CharField(max_length=250,null=True)
    page = models.CharField(max_length=250,null=True)
    cost = models.CharField(max_length=250,null=True)
    description = models.TextField(null=True)
    quentity = models.CharField(max_length=250,null=True)
    isbn = models.CharField(max_length=250,null=True)
    image = models.ImageField(null=True)
    pdf = models.FileField(null=True)

class BookCategory(models.Model):
    catName = models.CharField(max_length=250,null=True)
    orderBy = models.CharField(max_length=250,null=True)
    inputer = models.CharField(max_length=250,null=True)
    description = models.CharField(max_length=250,null=True)
    createDate = models.DateTimeField()


class BookHistory(models.Model):
    bookID = models.CharField(max_length=250,null=True)
    userID = models.CharField(max_length=250,null=True)
    actionType = models.CharField(max_length=250,null=True)
    dateTime = models.DateTimeField()

class Visitors(models.Model):
    userID = models.CharField(max_length=250,null=True)
    visitType = models.CharField(max_length=250,null=True)
    visitDateTime = models.DateTimeField()

class BorrowRule(models.Model):
    lateChCost = models.CharField(max_length=250,null=True)
    dates = models.DateField()

