from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added =  models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICES)
    description = models.CharField(max_length=100,default='')
    price = models.DecimalField(decimal_places=2,max_digits=3,default=0)
    def  __str__(self) :
        return self.name
    
    
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ratings = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return f'{self.user.username} review for {self.chai.name}'
    
    
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety,related_name='stores')
    
    def __str__(self) -> str:
        return self.name
    
    
    
class ChaiCertificates(models.Model):
  chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE,related_name='certificates')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default = timezone.now)
  valid_until = models.DateTimeField()
  def __str__(self) -> str:
        return f'certificates for {self.chai.name} '
    