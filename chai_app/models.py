from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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


class ChaiReview(models.Model):
  chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField()
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)
  
  def __str__(self) -> str:
    return f"{self.user.username}"


class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_variety = models.ManyToManyField(ChaiVariety, related_name='stores')
  
  def __str__(self):
      return self.name


class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
  serial_number = models.CharField(max_length=50)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_till = models.DateTimeField()
  
  def __str__(self):
      return f'Certificate for {self.chai.name}'