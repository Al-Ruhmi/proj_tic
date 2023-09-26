from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    
    name = models.CharField(max_length=20, null=True, blank=True)
    surename = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    std_pic = models.ImageField(upload_to='images',null=True, blank=True)
    std_pic_pass_fro = models.ImageField(upload_to='images',null=True, blank=True)
    std_pic_pass_bac = models.ImageField(upload_to='images',null=True, blank=True)
    def __str__(self):
        return self.username


class Students(models.Model):
    std_user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.std_user.username
    
    @receiver(post_save , sender= User)
    def create_user_profile(sender, instance,created,**kwargs):
        if created:
            if instance.is_student == True:
                Students.objects.create(
                std_user = instance
                )



class EmpUser(models.Model):
    emp_user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_birth_date = models.DateTimeField(null=True, blank=True)
    emp_name = models.CharField(max_length=20, null=True, blank=True)
    emp_surename = models.CharField(max_length=20, null=True, blank=True)
    emp_photo = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.emp_user.username
    
    @receiver(post_save , sender= User)
    def create_user_profile(sender, instance,created,**kwargs):
        if created:
            if instance.is_student == False:
                EmpUser.objects.create(
                emp_user = instance
                )
