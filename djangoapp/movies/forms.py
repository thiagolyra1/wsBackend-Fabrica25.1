from django import forms
from .models import Movies

class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['Title', 'Rated', 'Released', 'Genre', 'Director', 'Actors', 
                  'Writer', 'Plot', 'Awards', 'Poster', 'imdbRating', 'Type']

        labels = {
            'Title': 'Filme:',
            'Rated': 'Classificação de idade:',
            'Released': 'Data de lançamento:',
            'Genre': 'Categoria:',
            'Director': 'Diretor:',
            'Actors': 'Atores:',
            'Writer': 'Escritores:',
            'Plot': 'Sinopse:',
            'Awards': 'Prêmios:',
            'Poster': 'Digite o endereço de um link para a foto do poster',
            'imdbRating': 'Rating do IMDB:',
            'Type': 'Tipo:',
        }
        
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control-lg', 'placeholder': 'Digite o filme:'}),
            'Rated': forms.TextInput(attrs={'class': 'form-control'}),
            'Released': forms.TextInput(attrs={'class': 'form-control'}),
            'Genre': forms.TextInput(attrs={'class': 'form-control'}),
            'Director': forms.TextInput(attrs={'class': 'form-control'}),
            'Actors': forms.TextInput(attrs={'class': 'form-control'}),
            'Writer': forms.TextInput(attrs={'class': 'form-control'}),
            'Plot': forms.TextInput(attrs={'class': 'form-control'}),
            'Awards': forms.TextInput(attrs={'class': 'form-control'}),
            'Poster': forms.TextInput(attrs={'class': 'form-control'}),
            'imdbRating': forms.TextInput(attrs={'class': 'form-control'}),
            'Type': forms.TextInput(attrs={'class': 'form-control'}),
        }