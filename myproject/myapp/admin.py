from django.contrib import admin
from .models import Developer, Genre, Game, GameInstance

class GameInstanceInline(admin.TabularInline):
    model = GameInstance
    extra = 0

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'display_genre', 'release_date')

    def display_genre(self, obj):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genre.name for genre in obj.genre.all()[:3]])  # Adjust the slice for performance if needed
    display_genre.short_description = 'Genre'

    inlines = [GameInstanceInline]

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_date', 'headquarters')

class GenreAdmin(admin.ModelAdmin):
    pass

class GameInstanceAdmin(admin.ModelAdmin):
    list_display = ('game', 'edition', 'status')
    list_filter = ('status',)

admin.site.register(Game, GameAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(GameInstance, GameInstanceAdmin)
