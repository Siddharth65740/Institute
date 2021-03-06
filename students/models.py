from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    father_firstname=models.CharField(max_length=50)
    father_second_name=models.CharField(max_length=50)
    father_last_name=models.CharField(max_length=50)
    Building_name=models.CharField(max_length=50)
    state_name=models.CharField(max_length=50)
    area_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    ph_number=models.CharField(max_length=11,validators=[MinValueValidator(0,"Number should not be negative")])
    ph_number_house=models.CharField(max_length=11,validators=[MinValueValidator(0,"Number should not be negative")])
    birthdate=models.DateField(null=True, blank=True)
    choice=(
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=10,choices=choice)
    Schoolname=models.CharField(max_length=50)
    education=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='media/')
    email=models.EmailField()
    inquiry_id=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}"


    def get_absolute_url(self):             # helps to redirect to another page
        return reverse('student-list')
