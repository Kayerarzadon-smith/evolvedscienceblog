from django.urls import path
from .views import PostListView, PostDetailView, ostarine
from .import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
    path('medical_disclaimer/', views.medical_disclaimer, name='blog-medical-disclaimer'),
    path('affiliate_disclaimer/', views.affiliate_disclaimer, name='blog-affiliate-disclaimer'),
    path('ostarine-mk-2866/', views.ostarine, name='ostarine'),
    path('lgd-4033/', views.lgd_4033, name='lgd_4033'),
    path('andarine-s-4/', views.AndarineS4, name='AndarineS4'),
    path('S-23/', views.S_23, name='S-23'),
    path('YK-11/', views.YK11, name='YK11'),
    path('LGD-3033/', views.LGD3033, name='LGD3033'),
    path('ACP-105/', views.ACP105, name='ACP105'),
    path('AC-262/', views.AC262, name='AC262'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

