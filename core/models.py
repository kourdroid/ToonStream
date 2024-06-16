from django.db import models
import uuid

class Movie(models.Model):
    TYPE_CHOICE = [
       ('movie','Movie'),
       ('serie','Series'),
       ('special','Special')
    ]
    uu_id = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    type = models.CharField(max_length=100,choices=TYPE_CHOICE,default='Movie')
    production_company = models.CharField(max_length=255,default='Uknown')
    length = models.PositiveIntegerField()
    image_card = models.ImageField(upload_to='movie_images/')
    image_cover = models.ImageField(upload_to='movie_images/')
    video = models.FileField(upload_to='movie_videos/')
    trailer_link = models.TextField()
    movie_views = models.IntegerField(default=0)
    is_series = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Season(models.Model):
  movie = models.ForeignKey(
      Movie, on_delete=models.CASCADE)
  season_number = models.PositiveIntegerField()
  poster = models.ImageField(upload_to='season_posters/')
  episodes_count = models.PositiveIntegerField(default=0)

  def __str__(self):
    return f"Season {self.season_number} - {self.movie.title}"


class Episode(models.Model):
  season = models.ForeignKey(Season, on_delete=models.CASCADE)
  episode_number = models.PositiveIntegerField()
  episode = models.FileField(upload_to='episodes/')

  def __str__(self):
    return f"E{self.episode_number} - {self.season.movie.title} S{self.season.season_number}"


