from django.contrib import admin
from main.models import Author,Post,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    exclude = ()
    serch_field = ('comment',)
    list_filter = ('author','date')
    list_display = ('title', 'author', 'date')

admin.site.register(Author)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
