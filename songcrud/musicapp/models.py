from django.db import models

# Create your models here.

class Artiste(models.Model):  
    first_name = models.CharField(max_length=20)  
last_name= models.CharField(max_length=100)  
age = models.IntegerField(_(""))()  
    
class Meta:  
        db_table = "artiste"  
        def __str__(self):
            return (self.first_name, self.last_name, self.age)
        
class Song(models.Model):  
  title = models.CharField(max_length=200)  
date_released= models.CharField(max_length=100)  
likes = models.ForeignKey(on_delete=models.CASCADE)  
artiste_id = models.CharField(max_length=20)  
class Meta:  
        db_table = "song"  
def __str__(self):
        return self.title
    
class Lyric(models.Model):  
 content = models.CharField(max_length=200)  
song_id= models.CharField(max_length=20)  
class Meta:  
        db_table = "lyric"  
def __str__(self):
        return self.content