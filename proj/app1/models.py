from django.db import models
# Create your models here.

class users(models.Model):
    name=models.CharField(max_length=25)
    number=models.IntegerField()
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class mechanic(models.Model):
    name=models.CharField(max_length=25)
    number=models.IntegerField()
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    workshop_name=models.CharField(max_length=20)
    workshop_location = models.CharField(max_length=20)
    workshop_license=models.CharField(max_length=20)
    license_img = models.FileField()
    status_choice=[
        ('approve','approve'),
        ('reject','reject'),
    ]
    status=models.CharField(max_length=10,choices=status_choice, default='pending')
    def __str__(self):
        return self.name

class book_service(models.Model):
    username=models.CharField(max_length=20)
    service=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    vehicle_num=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    msg=models.CharField(max_length=50)
    status_choice=[
        ('accept','accept'),
        ('reject','reject'),
        ('complete','complete'),
        ('cancel','cancel'),
    ]
    status=models.CharField(max_length=10,choices=status_choice)
    def __str__(self):
        return self.name

class accept_serv(models.Model):
    service=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    vehicle_num=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    msg=models.CharField(max_length=50)
    status_choice=[
        ('accept','accept'),
        ('reject','reject'),
    ]
    status=models.CharField(max_length=10,choices=status_choice)
    def __str__(self):
        return self.name

class admin_log(models.Model):
    admin_name=models.CharField(max_length=25)
    admin_pass=models.CharField(max_length=20)
    def __str__(self):
        return self.admin_name

class user_contact(models.Model):
    username=models.CharField(max_length=25)
    user_email=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    message=models.CharField(max_length=25)
    def __str__(self):
        return self.username

class mech_contact(models.Model):
    username=models.CharField(max_length=25)
    user_email=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    message=models.CharField(max_length=25)
    def __str__(self):
        return self.username