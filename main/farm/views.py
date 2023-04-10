from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import RespawnTime, RaidBoss, ClanMember
from .forms import FarmRaidBossForm

# Create your views here.
class RespawnTimeView(View):
    ''' вывод записи из модели Post
        request - информация, принятая от пользователя, т.е. браузера
        respawn_time - будет ссылаться на всю (all) информацию (objects) из таблицы RespawnTime
        render - объединяет указанный шаблон со словарем (данные из модели)
        respawn_list - просто имя по которому мы будем обращаться к данным из respawn_time '''

    def get(self, request):
        '''получаем сразу отсортированный список по дате и времени в переменную respawn_time'''
        respawn_time = RespawnTime.objects.order_by('date', 'time')
        return render(request, 'farm/respawn.html', {'respawn_list': respawn_time})


class RaidBossView(View):
    ''' вывод записи из модели RaidBoss '''
    def get(self, request):
        raid_boss = RaidBoss.objects.all()
        return render(request, 'farm/respawn.html', {'raid_boss_list': raid_boss})


class ClanMemberView(View):
    ''' вывод записи из модели ClanMember '''
    def get(self, request):
        member = ClanMember.objects.order_by('-score')
        return render(request, 'farm/member.html', {'clan_member_list': member})

def create_farm(request):
    error = ''
    if request.method == 'POST':
        form = FarmRaidBossForm(request.POST)
        if form.is_valid():
            farm_raid_boss = form.save()

            party_members = form.cleaned_data.get('party_members', [])

            for party_member in party_members:
                clan_member = get_object_or_404(ClanMember, name=party_member)
                clan_member.score += 1
                clan_member.save()

            return redirect('/respawn')
        else:
            error = 'Форма была неверной'


    form = FarmRaidBossForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'farm/create_farm.html', context)