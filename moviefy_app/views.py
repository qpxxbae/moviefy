from django.shortcuts import render,get_object_or_404,redirect
from .models import Genre,Movie
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate


def home_page(request):
    return render(request,"./movies/index.html")

def top_movies_page(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()[:10]
    context = {
        'genres':genres,
        'movies':movies
    }
    return render(request,"./movies/top_movies.html",context)

def all_movies_page(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    context = {
        'genres':genres,
        'movies':movies
    }
    return render(request,"./movies/all_movies.html",context)

def movie_detail_page(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie':movie
    }
    return render(request,"./movies/movie-detail.html",context)

def movies_by_category_page(request,slug):
    genre = get_object_or_404(Genre,slug = slug)
    movies = Movie.objects.filter(genre = genre)
    genres = Genre.objects.all()
    context ={
        'genre':genre,
        'genres':genres,
        'movies':movies

    }
    return render(request,"./movies/movies-by-category.html",context)

def movies_by_search_page(request):
    query = request.GET.get("query")
    movies = Movie.objects.filter(name__icontains=query)|Movie.objects.filter(description__icontains=query)
    context = {
        'query':query,
        'movies':movies
    }
    return render(request,"./movies/movies-by-search.html",context)


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login_page")
    else:
        form = NewUserForm()

    return render(request,"./user/sign-up.html",{'form':form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("top_movies_page")
    else:
        form = AuthenticationForm()
    return render(request,"./user/login.html",{'form':form})


def logout_action(request):
    logout(request)
    return redirect("home_page")