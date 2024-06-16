from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Movie, Season, Episode
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password2)
                user.save()

                # log user in
                user_login = auth.authenticate(
                    username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


@login_required
def movie_detail(request, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    context = {
        'movie': movie,
    }

    return render(request, 'movie_detail.html', context)


@login_required
def watch(request, content_type, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    context = {
        'movie': movie,
    }
    if content_type == 'movie':
        return render(request, 'watch_movie.html', context)

    elif content_type == 'serie':
        return render(request, 'watch_serie.html', context)

    if content_type == 'special':
        special = get_object_or_404(Movie, title=movie_title)
        special_episodes = special.special_episodes
        context = {
            'special': special,
            'special_episodes': special_episodes,
        }
        return render(request, 'watch_special.html', context)

    else:
        return render(request, 'index.html')


@login_required
def movie_watching(request, movie_title):
    movie = get_object_or_404(Movie, title=movie_title)
    context = {
        'movie': movie,
    }
    return render(request, 'watch_movie.html', context)


@login_required
def series_watching(request, movie_title):
    serie = get_object_or_404(Movie, title=movie_title)
    context = {
        'serie': serie,
    }
    return render(request, 'watch_serie.html', context)


def serie_watch_page(request, movie_title, season_pk):
    season = get_object_or_404(Season, pk=season_pk)
    movie = season.movie
    episodes = season.episode_set.all()  # Assuming episodes are related to Season

    context = {
        'season': season,
        'episodes': episodes,
        'movie': movie,
        'episode_videos': [episode.episode for episode in episodes],
        # Initial video URL
        'initial_video_url': episodes[0].episode.url if episodes else None,
    }
    return render(request, 'watch_serie.html', context)


def get_episode_video_url(episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    return episode.episode.url
