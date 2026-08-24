# models.py
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    prod_image = models.ImageField(upload_to='products/',null=True,blank=True)
    short_description = models.TextField()
    description = CKEditor5Field(
        'Description',
        config_name='extends'
    )
    slug = models.SlugField(unique=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


from django.db import models


class Enquiry(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True,
        null=True
    )

    company = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    product = models.CharField(
        max_length=200
    )

    requirement = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.product}"