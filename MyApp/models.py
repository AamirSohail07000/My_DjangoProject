from django.db import models

#makemigrations - create and store changes in a file
#migrate - apply the pending changes created by makemigrations


# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=122)
  phone = models.CharField(max_length=122)
  desc = models.TextField()
  date = models.DateField()
  #renaming contact saved as contact1 contact2 to Name input 
  def __str__(self):
      return self.name

