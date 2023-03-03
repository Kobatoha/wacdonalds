from django.urls import path
from . import views

''' из модуля django.urls подключаем фунцию path, которая позволяет работать с путем
    подключаем из коневой папки (где сейчас находимся, т.е. wacdonalds/main/blog/views.py) 
    urlpatterns - список, где будут все пути для url-адресов
    views. - тут указывам функцию, которая будет отрабатывать представление (PostView),
    .as_view - метод '''

urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
               path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes')]