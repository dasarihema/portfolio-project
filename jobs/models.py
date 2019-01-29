from django.db import models

# Create your models here.
class job(models.Model):
    image= models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    summary=models.CharField(max_length=200)
    brief=models.CharField(max_length=200)
    project_duration= models.IntegerField()

    def __str__(self):
        return self.summary
