from django.db import models
import uuid

# Create your models here.

class UserCredentials(models.Model):
    user_id = models.UUIDField(primary_key=True, null=False , default=uuid.uuid4, editable=False)
    username= models.CharField(max_length = 50, null=True, blank=True, unique= True)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True,help_text='Enter a valid email address')
    password = models.CharField(max_length= 200,null=True, blank = True)    

    def __str__(self):
        return self.username