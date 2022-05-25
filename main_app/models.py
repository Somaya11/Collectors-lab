from django.db import models
from django.urls import reverse

READ = (
     ('W', 'Want To Read'),
     ('R', 'Reading'),
     ('F', 'Finished Reading')
 )

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    type = models.TextField(max_length=250)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Reading(models.Model):
  date = models.DateField('feeding date')
  read = models.CharField(
    max_length=1,
    choices=READ,
    default=READ[0][0]
  )
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_read_display()} on {self.date}"
    
