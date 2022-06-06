from cProfile import label
from django.db import models
from django.utils.text import slugify
# from django.contrib.auth.models  import User
from users.models import Profile


# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=30)
    

    def __str__(self):
        return self.label



class Category(models.Model):
    label= models.CharField(max_length=55)
    slug = models.SlugField( null=True, blank=True)

   
    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.label)
        super().save(*args, **kwargs)




class Skill(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50 )
    slug = models.SlugField(null=True , blank=True)
    experience = models.TextField(null=True , blank=True)
    percent = models.BigIntegerField(null=True, blank=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # class Meta:
    #     ordering = ["-updated_at"]

    


    def __str__(self):
        return f"{self.title}"

    @property
    def active(self):
        if self.published:
            return f"{self.title} is published"
        else:
            return f"{self.title} is not published"


    # Redifinition de la methode save qui prend automatiquement le slug s'il nexiste pas
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

