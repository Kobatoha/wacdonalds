from django.contrib import admin
from .models import Character, RaidBoss, FarmRaidBoss, DropRaidBoss, ClanMember, RespawnTime


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('nickname', 'level', 'main', 'master')

@admin.register(RaidBoss)
class RaidBossAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('name', 'level')

@admin.register(FarmRaidBoss)
class FarmRaidBossAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('name', 'date', 'time')

@admin.register(DropRaidBoss)
class DropRaidBossAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('title', 'price')

@admin.register(ClanMember)
class ClanMemberAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('name',)

@admin.register(RespawnTime)
class RespawnTimeAdmin(admin.ModelAdmin):
    ''' регистрация модели после ее создания;
        описание класса, который будет отвечать за административную часть модели Post;
        лист_дисплей отвечает за заголовки, таблицы и отбражение модели в панели администратора '''
    list_display = ('time' ,'raid_boss',)