from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    """ This is Stacked in line style. """
    model = Comment


# class CommentInline(admin.StackedInline):
# """ This is Stacked in line style. """
# model = Comment


class ArticleAdmin(admin.ModelAdmin):
    """ Custom admin for the Article. """
    model = Article
    list_display = ['title', 'author', 'date']

    # Display related comments inside a post.
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
