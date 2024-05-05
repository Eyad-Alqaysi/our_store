import uuid
from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100)
    founded_date = models.DateField(null=True, blank=True)
    headquarters = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the game")
    release_date = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this game")

    def __str__(self):
        return self.title

class GameInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular game across whole library")
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    edition = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('available', 'Available'),('sold out', 'Sold out'),('preorder', 'Pre-order')], blank=True, default='available')

    def __str__(self):
        return f'{self.game.title} - {self.edition} Edition'
