from django.db import models

# Create your models here.

class Artiste(models.Model):  
  first_name = models.CharField(max_length=20)  
   last_name= models.CharField(max_length=100)  
    age = models.()  
    class Meta:  
        db_table = "artiste"  
            def __str__(self):
            return self.(first_name, last_name, age)
        
class Song(models.Model):  
  title = models.CharField(max_length=200)  
   date_released= models.CharField(max_length=100)  
    likes = models.EmailField()  
    artiste_id = models.EmailField()  
     class Meta:  
        db_table = "song"  
    def __str__(self):
        return self.title
    
class Lyric(models.Model):  
 content = models.CharField(max_length=20)  
   song_id= models.CharField(max_length=100)  
    class Meta:  
        db_table = "lyric"  
