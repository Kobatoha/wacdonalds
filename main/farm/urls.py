from django.urls import path
from . import views

''' из модуля django.urls подключаем фунцию path, которая позволяет работать с путем
    подключаем из коневой папки (где сейчас находимся, т.е. wacdonalds/main/farm/views.py) 
    urlpatterns - список, где будут все пути для url-адресов
    views. - тут указывам функцию, которая будет отрабатывать представление (PostView),
    .as_view - метод '''

urlpatterns = [path('respawn/', views.RespawnTimeView.as_view()),
               path('respawn/', views.RaidBossView.as_view()),
               path('member/', views.ClanMemberView.as_view()),
               path('create/', views.create_farm)]