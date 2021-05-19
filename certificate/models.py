from django.db import models
from admission.models import admission
from django.core.validators import FileExtensionValidator
from django.urls import reverse

# Create your models here.
class Certificate(models.Model):
    date=models.DateField()
    admission=models.ForeignKey(admission,on_delete=models.CASCADE,related_name="certificate")
    photo=models.ImageField(validators=[FileExtensionValidator(['jpg','png','jpeg'],"file extension is invalid ")],blank=True)

    def __str__(self):
        return f"           {self.admission}"

    def get_absolute_url(self):
        return reverse('certificate-list')
