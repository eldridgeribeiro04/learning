from django.urls import path
from templates_app import views

app_name = 'templates_app'

urlpatterns = [
    path("relative/", views.relative_url, name='relative'),
    path('other/', views.other, name='other')
]