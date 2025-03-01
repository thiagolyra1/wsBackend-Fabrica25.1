from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

import requests

from .forms import MoviesForm
from .models import Movies


def home(request):
    return render(request, 'movies/pages/index.html')


def search_view(request):
    form = MoviesForm()
    message = ''

    if request.method == 'POST':
        form = MoviesForm(request.POST)
        filme_digitado = request.POST.get('Title')
        url = f'https://www.omdbapi.com/?t={filme_digitado}&y=2012&apikey=1308d3a0'
        response = requests.get(url)

        if response.status_code == 200:
            dados_filme = response.json()
            if 'erro' in dados_filme:
                message = 'Filme não encontrado'
            else:
                resposta_em_json_filtrada = {
                    'Title': dados_filme['Title'],
                    'Rated': dados_filme['Rated'],
                    'Released': dados_filme['Released'],
                    'Genre': dados_filme['Genre'],
                    'Director': dados_filme['Director'],
                    'Actors': dados_filme['Actors'],
                    'Writer': dados_filme['Writer'],
                    'Plot': dados_filme['Plot'],
                    'Awards': dados_filme['Awards'],
                    'Poster': dados_filme['Poster'],
                    'imdbRating': dados_filme['imdbRating'],
                    'Type': dados_filme['Type'],
                }
                
                if Movies.objects.filter(Title=resposta_em_json_filtrada['Title']).exists():
                    message = f'O filme "{resposta_em_json_filtrada["Title"]}" já foi cadastrado anteriormente. Você pode procurar ele em "Listar filmes cadastrados"'
                else:
                    form = MoviesForm(data=resposta_em_json_filtrada)                
                    if form.is_valid():
                        try:
                            form.save()
                            print("Registro salvo com sucesso!")
                        except Exception as e:
                            print(f"Erro ao salvar: {e}")
                    else:
                        message = "Erro ao validar o formulário."
        else:
            message = 'Erro durante a requisição na API'

            
    return render(request, 'movies/pages/moviesSearch.html', {
        'form': form, 'message': message
        }
    )

class MoviesCreate(CreateView):
    model = Movies
    form_class = MoviesForm
    context_object_name = 'CreateMoviesForm'
    template_name = 'movies/pages/moviesForm.html'
    success_url = reverse_lazy('movies:listar')

class MoviesList(ListView):
    model = Movies
    template_name = 'movies/pages/moviesList.html'
    context_object_name = 'movies_list'

class MoviesDelete(DeleteView):
    model = Movies
    template_name = 'movies/pages/moviesDelete.html'
    success_url = reverse_lazy('movies:listar')

class MoviesUpdate(UpdateView):
    model = Movies
    form_class = MoviesForm
    context_object_name = 'movies'
    template_name = 'movies/pages/moviesForm.html'
    success_url = reverse_lazy('movies:listar')

class MoviesDetail(DetailView):
    model = Movies
    template_name = 'movies/pages/moviesDetail.html'
    context_object_name = 'movies'
