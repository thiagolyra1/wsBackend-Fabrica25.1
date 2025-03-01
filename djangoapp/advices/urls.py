from django.urls import path
from . import views

urlpatterns = [
    path('advices/', views.get_advices, name='get_advices'),
    path('advice/<int:pk>/', views.get_advice_id, name='get_advice'),
    path('advice/random_advice/', views.random_advice, name='random_advice'),
    path('advice/update/<int:pk>/', views.update_advice, name='update_advice'),
    path('advice/delete/<int:pk>/', views.delete_advice, name='delete_advice'),
    path('advice/create/', views.create_advice, name="create_advice"),
]