from django.db import models

# Create your models here.

#category model
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title

#image model
class Image(models.Model):
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField() 
    cat=models.ForeignKey(Category,on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs): #inbuilt method:overriding for customization of image size - KK
        super().save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height >400 or img.width >800:
            output_size=(400,800)
            img.thumbnail(output_size)
            img.save(self.image.path)    

