from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models 

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		("title/date", {"fields": ["name", "date_posted", "author"]}),
		("content", {"fields":["content", "image"]}),
	]

	formfield_overrides = {
		models.TextField: {"widget": TinyMCE()}
	}

admin.site.register(Post,PostAdmin)


