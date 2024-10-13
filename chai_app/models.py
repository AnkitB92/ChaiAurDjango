from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
  CHAI_TYPE = (
    ("PL", "PLAIN"),
    ("MS", "MASALA"),
    ("GG", "GINGER"),
    ("GR", "GREEN"),
  )

  CHAI_SIZE = (
    ("SM", "SMALL"),
    ("MD", "MEDIUM"),
  )

  name = models.CharField(max_length=50)
  image = models.ImageField(upload_to='chais')
  price = models.DecimalField(max_digits=5, decimal_places=2, default=9.99)
  size = models.CharField(max_length=2, choices=CHAI_SIZE)
  type = models.CharField(max_length=2, choices=CHAI_TYPE)
  description = models.TextField(max_length=250,default='Description yet to be added.')
  added_on = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name
