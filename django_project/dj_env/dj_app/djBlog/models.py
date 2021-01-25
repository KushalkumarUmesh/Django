from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model): # Post model - KK
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) # cascade-if the user is deleted then his post will be deleted but not the oter way - KK

    def __str__(self):            #customizing the std __str__ method to get title for execution - KK
        return self.title
 
    def get_absolute_url(self):   #customizing the std method to send the url string in the reverse method
        return reverse('post-detail',kwargs={'pk':self.pk})



# reverse - sends the URL as a string
# redirect - redirect to the url mentioned