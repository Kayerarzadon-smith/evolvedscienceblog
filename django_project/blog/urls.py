from django.urls import path
from . views import PostListView, PostDetailView
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('medical_disclaimer/', views.medical_disclaimer, name='blog-medical-disclaimer'),
    path('affiliate_disclaimer/', views.affiliate_disclaimer, name='blog-affiliate-disclaimer'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

