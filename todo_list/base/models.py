from django.db import models

# Create your models here.
class Todos(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    statues = models.BooleanField(null=True)

    def __str__(self):
        return self.name