from django.db import models
from apps.adopcao.models import Person

# Create your models here.
class Vacine (models.Model):
    name = models.CharField(max_length=60)

class Mascota(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    date_save = models.DateField()
    photo = models.ImageField(upload_to='images')
    person = models.ForeignKey(Person, null= True, blank=True, on_delete=models.CASCADE)
    vacine = models.ManyToManyField(Vacine, blank = True)

