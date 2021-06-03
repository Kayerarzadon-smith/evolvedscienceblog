from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 
from django.urls import reverse 

class Post(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_pictures')
    slug = models.SlugField(default='', editable=False, max_length=200, null=False)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):

        kwargs = {
            "pk": self.id,
            "slug": self.slug
        }

        return reverse('post-detail', kwargs = kwargs)

    def save(self, *args, **kwargs):

        value = self.name
        self.slug = slugify(value, allow_unicode=False)
        super().save(*args, **kwargs)