from io import BytesIO
from PIL import Image

from django.core.files import File

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from apps.vendor.models import Vendor

# Create your models here.
class Category(models.Model):
    ## for product category
    title = models.CharField(max_length=50)
    #image = models.ImageField(upload_to='uploads/', , blank=True , null=True)
    ordering = models.IntegerField(default=0)

    slug = models.SlugField(blank=True  , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.title :
            self.slug = slugify(self.title)
        super(Category , self).save(*args , **kwargs)

    class Meta:
        ordering = ['ordering']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True  , null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_two = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_three = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date_added']

    def save(self , *args , **kwargs):
        if not self.slug and self.title :
            self.slug = slugify(self.title)
        super(Product , self).save(*args , **kwargs)

    def __str__(self):
        return self.title
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail