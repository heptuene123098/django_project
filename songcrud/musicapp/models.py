from django.db import models

# Create your models here.

class Artiste(models.Model):  
  first_name = models.CharField(max_length=20)  
   last_name= models.CharField(max_length=100)  
    age = models.EmailField()  
   
    class Meta:  
        db_table = "employee"  
Model: , Song, Lyric
Attributes for “Artiste” : , , 
Attributes for “Song” : title, date released, likes, artiste_id
Attributes for “Lyric”: content, song_id