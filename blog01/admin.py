from django.contrib import admin
from blog01.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'modify_date','image')
    list_filter   = ('modify_date',)
    search_fields = ('title', 'content')
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
