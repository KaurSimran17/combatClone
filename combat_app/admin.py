from django.contrib import admin
from combat_app.models import Promoter, Sanctioning, Gym_Owner,Medics, Role, Fighter, Event_Calendar ,Gym_info, Achivements, Boxing_Record, k1_Record,Mod_Thai_Record,MMA_Record,Muya_Thai_Record,  Martial_Art_Record, register_table, Social_link
class PromoterAdmin(admin.ModelAdmin):
    list_display = ["fname","lname","profile","email","contact","date","month","year","gender","city","town",
    "country"]
admin.site.register(Promoter, PromoterAdmin)


class SanctioningAdmin(admin.ModelAdmin):
    list_display = ["fname","lname","profile","email","contact","date","month","year","gender","city","town",
    "country","document", "password"]
admin.site.register(Sanctioning, SanctioningAdmin)

class Gym_infoAdmin(admin.ModelAdmin):
    list_display = ["gym_name", "url_link", "discipline", "email","apartment", "city", "town","country", "phone_number", "mobile", "head_coach", "additi_coach" ]
admin.site.register(Gym_info,Gym_infoAdmin )
# admin.site.register(Gym_info)
admin.site.register(Social_link)
admin.site.register(Achivements)
admin.site.register(Boxing_Record)
admin.site.register(k1_Record)
admin.site.register(Mod_Thai_Record)
admin.site.register(Muya_Thai_Record)
admin.site.register(MMA_Record)
admin.site.register(Martial_Art_Record)


class Gym_OwnerAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","profile","email","contact","date","month","year","gender","city","town",
    "country","document","password"]
admin.site.register(Gym_Owner, Gym_OwnerAdmin)


class MedicsAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","profile","email","contact","date","month","year","gender","city","town",
    "country","document","password"]
admin.site.register(Medics, MedicsAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ["role_name"]
admin.site.register(Role,RoleAdmin)

class FighterAdmin(admin.ModelAdmin):
    list_display= ["first_name","last_name","profile","email","contact","date","month","year","gender","city","town",
    "country","document","password","fight_name","fight_weight","wight_units","fight_height","height_units","discipline","gym_name"]
admin.site.register(Fighter,FighterAdmin )

class EventAdmin(admin.ModelAdmin):
    list_display = ["date", "month", "year", "discipline", "sanct_body", "address", "medics", "host", "mobile"]
admin.site.register(Event_Calendar, EventAdmin)

# Register your models here.
