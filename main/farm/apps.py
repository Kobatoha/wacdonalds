from django.apps import AppConfig



class FarmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farm'

#class RaidBossTimeConfig(AppConfig):
#    name = 'raidbosstime'
#
#    def ready(self):
#        from raidbosstime.signals import update_respawn_time_on_farm_raid_boss_creation
#        from farm.models import FarmRaidBoss, RaidBoss
#        post_save.connect(update_respawn_time_on_farm_raid_boss_creation, sender=FarmRaidBoss)
