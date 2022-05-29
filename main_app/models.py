from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

READ = (
     ('W', 'Want To Read'),
     ('R', 'Reading'),
     ('F', 'Finished Reading')
 )

# Create your models here.

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessorys_detail', kwargs={'pk': self.id})

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.TextField(max_length=50)
    accessorys = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Reading(models.Model):
  date = models.DateField('reading date')
  read = models.CharField(
    max_length=1,
    choices=READ,
    default=READ[0][0]
  )
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_read_display()} on {self.date}"

  class Meta: 
    ordering = [ '-date']
    
