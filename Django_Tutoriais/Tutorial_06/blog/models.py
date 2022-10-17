from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body=models.TextField()
   
    def __str__(self):
<<<<<<< HEAD
       return self.title
       
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
=======
     return self.title
    
>>>>>>> 0f34069531d58b2ce86903428c8cef0c7024d676
