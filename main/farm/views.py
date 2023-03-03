from django.shortcuts import render
from django.views.generic.base import View
from .models import RespawnTime, RaidBoss, ClanMember

# Create your views here.
class RespawnTimeView(View):
    ''' вывод записи из модели Post
        request - информация, принятая от пользователя, т.е. браузера
        respawn_time - будет ссылаться на всю (all) информацию (objects) из таблицы RespawnTime
        render - объединяет указанный шаблон со словарем (данные из модели)
        respawn_list - просто имя по которому мы будем обращаться к данным из respawn_time '''

    def get(self, request):
        respawn_time = RespawnTime.objects.all()
        return render(request, 'farm/respawn.html', {'respawn_list': respawn_time})


class RaidBossView(View):
    ''' вывод записи из модели RaidBoss '''
    def get(self, request):
        raid_boss = RaidBoss.objects.all()
        return render(request, 'farm/respawn.html', {'raid_boss_list': raid_boss})


class ClanMemberView(View):
    ''' вывод записи из модели ClanMember '''
    def get(self, request):
        member = ClanMember.objects.all()
        return render(request, 'farm/member.html', {'clan_member_list': member})