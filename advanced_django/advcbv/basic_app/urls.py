from basic_app import views
from django.urls import path, include

app_name = 'basic_app'


urlpatterns = [
    path("school_list/", views.SchoolListView.as_view(), name='list'),
    path("details/<pk>/", views.SchoolDetailView.as_view(), name='details'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.SchoolDeleteView.as_view(), name='delete'),
]