from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    cnic = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=13)
    employPost = models.CharField(max_length=40)
    employDate = models.DateTimeField()

    def __str__(self):
        return self.user.username

class Tasks(models.Model):
    STATUS_CHOICES=[
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    taskName = models.CharField(max_length=200)
    taskDisc = models.TextField(max_length=400)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES ,default='pending')
    
    def __str__(self):
        return f"{self.taskName}-{self.get_status_display()}"
    
class Accounts(models.Model):
    user =models.OneToOneField(User , on_delete=models.CASCADE)
    basic = models.IntegerField()
    bonus = models.IntegerField()
    reward = models.IntegerField()
    
    def salary(self):
        return self.basic+self.bonus+self.reward
    def __str__(self):
        return f"{self.user}-payment account"