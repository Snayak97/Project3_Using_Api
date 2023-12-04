from django.db import models

# Create your models here.
class Details(models.Model):
    Id=models.PositiveIntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    def __str__(self):
        return self.Name
