from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('title', 'date')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Comments;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('name', 'post')