from movies.views import search_view, MoviesCreate, MoviesList, MoviesDelete, MoviesUpdate
from django.urls import path



app_name = 'movies'

urlpatterns = [

    path('buscar/', search_view, name='buscar'),

    # path('', home, name='index'),
    path('criar/', MoviesCreate.as_view(), name='criar'),
    path('listar/', MoviesList.as_view(),  name='listar'),
    path('deletar/<int:pk>/', MoviesDelete.as_view(), name="deletar"),
    path('editar/<int:pk>/', MoviesUpdate.as_view(), name="atualizar"),
]