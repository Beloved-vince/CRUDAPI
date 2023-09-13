from django.db import models
from uuid import uuid4
# Create your models here.

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name