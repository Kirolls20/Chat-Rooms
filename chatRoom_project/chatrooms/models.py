from django.db import models
from django.contrib.auth.models import User
import random 
import string

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    room_name_id = models.CharField(max_length=50,unique=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    pub_date = models.DateTimeField(auto_now=True)
    is_group = models.BooleanField(default=False)

    def generate_room_name_id(self):
        room = self.name 
        cleaned_name = room.replace(" ","_")
        combination = string.ascii_letters + string.digits
        generated_name_id = cleaned_name + "".join(random.choice(combination) for _ in range(8))
        return generated_name_id

    def save(self,*args,**kwargs):
        if not self.room_name_id:
            self.room_name_id = self.generate_room_name_id()
        super().save(*args,**kwargs)


    def __str__(self):
        return self.name + "Owned by  " + self.owner.username

class Message(models.Model):
    message = models.CharField(max_length=400)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    message_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message + 'By' + self.user.username

