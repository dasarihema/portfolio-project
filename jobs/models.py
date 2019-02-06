from django.db import models

# Create your models here.
class job(models.Model):
    image= models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    summary=models.CharField(max_length=200)
    brief=models.CharField(max_length=400)
    project_duration= models.IntegerField()
    OS=models.CharField(max_length=30)
    Client_technologies=models.CharField(max_length=30)
    Server_technologies=models.CharField(max_length=30)
    db=models.CharField(max_length=30)
    web_server=models.CharField(max_length=30)
    framework=models.CharField(max_length=30)
    host_engine=models.CharField(max_length=30)
    version_control=models.CharField(max_length=30)

    def __str__(self):
        return self.summary
