from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """ Custom admin for the Article. """
    model = Article
    list_display = ['title', 'author', 'date']


admin.site.register(Article, ArticleAdmin)
