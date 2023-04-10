from django.db import models
from datetime import datetime, timedelta, time, timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



# Create your models here.
class Character(models.Model):
    ''' Список персонажей клана Wacdonalds и их питомцы '''
    master = models.ForeignKey('ClanMember', on_delete=models.PROTECT, null=True)
    nickname = models.CharField('Имя пользователя', max_length=100)
    level = models.IntegerField('Уровень персонажа')
    pet = models.BooleanField('Питомец')
    main = models.BooleanField('Основной персонаж', default=False)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.nickname

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name = 'Персонаж'
        verbose_name_plural = '2. Персонажи'


class ClanMember(models.Model):
    ''' Список игроков клана Wacdonalds '''
    name = models.CharField('Имя игрока', max_length=50)
    characters = models.ManyToManyField('Character', verbose_name='Персонаж')
    score = models.IntegerField('Score', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name = 'Киска и сосиска'
        verbose_name_plural = '1. Киски и сосиски'

class Role(models.Model):
    ''' Профессии персонажей (например, БД или СВС)
        Для наглядности имеющихся в распоряжении персонажей '''
    profession = models.CharField('Профессия', max_length=100, db_index=True)

    def __str__(self):
        return self.profession


class RaidBoss(models.Model):
    ''' Таблица с описанием РБ, его уровень, сколько очков за его убийство дается персонажам
        Время возрождения дается в минутах '''
    name = models.CharField('Имя РейдБосса', max_length=150)
    level = models.PositiveSmallIntegerField('Уровень РБ', default=70)
    score = models.PositiveSmallIntegerField('ДЦП очки', default=1)
    image = models.ImageField('Изображение', upload_to='image', default='img.jpeg')
    respawn = models.TimeField('Время возрождения')

    def __str__(self):
        return self.name

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name = 'РейдБосс'
        verbose_name_plural = '3. РейдБоссы'

class RespawnTime(models.Model):
    ''' Время возрождения РейдБосса '''
    raid_boss = models.ForeignKey('RaidBoss', on_delete=models.CASCADE, verbose_name='Имя РейдБосса')
    time = models.TimeField('Время возрождения', null=True)
    date = models.DateField('Дата возрождения', null=True, default=datetime.today())

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name_plural = '4. Респавн РейдБоссов'

class FarmRaidBoss(models.Model):
    ''' Информация о фарме боссов:
        1. Какой рейд Босс был побежден
        2. Когда и во сколько
        3. Кто участвовал в убийстве
        4. Что упало '''
    name = models.ForeignKey('RaidBoss', on_delete=models.PROTECT, null=True, verbose_name='Имя РейдБосса')
    date = models.DateField('Дата убийства', default=datetime.now)
    time = models.TimeField('Время убийства', default=datetime.now)
    party_members = models.ManyToManyField('ClanMember', blank=True)




    def __str__(self):
        return f'{self.name} - {self.date}'

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name_plural = '5. Фарм РейдБоссов'



@receiver(post_save, sender=FarmRaidBoss)
def calculate_respawn_time_on_farm_raid_boss_creation(sender, instance, **kwargs):
    ''' Подсчет времени до следующего респа Босса на основе данных:
        1. Когда убили
        2. Дефолтное время респа '''
    raid_boss = instance.name
    last_farm_raid_boss = FarmRaidBoss.objects.filter(name=raid_boss).order_by('-date', '-time').first()
    last_farm_raid_boss_time = last_farm_raid_boss.time
    raid_boss_cd = RaidBoss.objects.get(name=raid_boss).respawn
    h = int(raid_boss_cd.hour)
    m = int(raid_boss_cd.minute)
    respawn_time = datetime.combine(datetime.today(), last_farm_raid_boss_time) + timedelta(hours=h, minutes=m)

    RespawnTime.objects.update_or_create(raid_boss=raid_boss, defaults={'time': respawn_time,
                                                                        'date': respawn_time})


class DropRaidBoss(models.Model):
    ''' Список игроков клана Wacdonalds '''
    title = models.CharField('Предмет', max_length=100, db_index=True, null=True)
    price = models.PositiveBigIntegerField('Стоимость предмета +- в L монетах', default=100)

    def __str__(self):
        return self.title

    class Meta:
        ''' корректное отображение записей в единственном и множественном числе '''
        verbose_name_plural = '6. Дроп с РейдБоссов'