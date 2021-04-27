from django.db import models
import string
import random

def generate_unique_id():
    length=8

    while(True):
        unique_id=''.join(random.choices(string.ascii_uppercase,k=length))
        if(Room.objects.filter(code=unique_id).count()==0):
            break

    return unique_id



# Create your models here.
class Room(models.Model):

    id_u=models.CharField(max_length=8,default="",unique=True)
    the_host=models.CharField(max_length=50,unique=True)
    the_guest_pause=models.BooleanField(null=False,default=False,)
    votes_skip=models.IntegerField(null=False,default=1)
    created_at=models.DateTimeField(auto_now_add=True)