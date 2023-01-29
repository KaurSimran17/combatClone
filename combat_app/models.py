from django.db import models
from django.contrib.auth.models import User
from countryinfo import countryinfo


class Promoter(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100)
    profile = models.ImageField()
    email = models.EmailField(max_length=300)
    contact = models.EmailField(max_length=20)
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    document = models.FileField(upload_to="new/", max_length=250)
    password = models.CharField(max_length=50)
    

class Sanctioning(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, max_length=200)
    email = models.EmailField(max_length=300)
    contact = models.EmailField(max_length=20)
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    document = models.FileField(null=True, max_length=250)
    password = models.CharField(max_length=50)

    # def __str__(self):  
    #     return self.fname+' '+self.lname
    


class Gym_Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, max_length=200)
    email = models.EmailField(max_length=300)
    contact = models.EmailField(max_length=20)
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    document = models.FileField(upload_to="new/", max_length=250)
    password = models.CharField(max_length=50)
    

class Medics(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, max_length=200)
    email = models.EmailField(max_length=300)
    contact = models.EmailField(max_length=20)
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    document = models.FileField(upload_to="new/", max_length=250)
    password = models.CharField(max_length=50)
    
class Coach(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, max_length=200)
    email = models.EmailField(max_length=300)
    contact = models.EmailField(max_length=20)
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    document = models.FileField(upload_to="new/", max_length=250)
    password = models.CharField(max_length=50)


class Role(models.Model):
    role_name = models.CharField(max_length=20)


class Fighter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.ImageField(null=True, blank=True, max_length=200)
    email = models.EmailField(max_length=300)
    contact = models.CharField(max_length=20)
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    document = models.FileField(upload_to="new/", max_length=250)
    password = models.CharField(max_length=50)
    fight_name = models.CharField(max_length=100)
    fight_weight = models.CharField(max_length=50)
    wight_units = models.CharField(max_length=20)
    fight_height= models.CharField(max_length=50)
    height_units = models.CharField(max_length=20)
    discipline = models.CharField(max_length=50)
    gym_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Event_Calendar(models.Model):
    date = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    discipline = models.CharField(max_length=100)
    sanct_body = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    medics = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.date +' '+self.month+' '+ self.year+' '+ self.discipline+' '+ self.sanct_body+' '+ self.address+' '+ self.medics+' '+ self.host+' '+ self.mobile 


class Gym_info(models.Model):
    gym_name = models.CharField(max_length=200)
    url_link = models.CharField(max_length=500)
    discipline = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    apartment = models.CharField(max_length=200)
    city = models.CharField(max_length=80)
    town = models.CharField(max_length=80)
    country = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    head_coach = models.CharField(max_length=100)
    additi_coach = models.CharField(max_length=100)

    def __str__(self):
        return self.gym_name


class Social_link(models.Model):
    facebook = models.URLField(max_length=500)
    instagram = models.URLField(max_length=500)
    twitter = models.URLField(max_length=500)
    gmail = models.EmailField(max_length=300)


class Achivements(models.Model):
    year = models.CharField(max_length=30)
    amature_pro = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    discipline = models.CharField(max_length=100)
    sanction = models.CharField(max_length=100)
    rule_set = models.CharField(max_length=100)
    achivement = models.CharField(max_length=100)


class Boxing_Record(models.Model):
    total = models.CharField(max_length=20)
    corporate_win = models.CharField(max_length=20)
    corporate_loose = models.CharField(max_length=20)
    corporate_draw = models.CharField(max_length=20)
    armature_win = models.CharField(max_length=20)
    armature_loose = models.CharField(max_length=20)
    armature_draw = models.CharField(max_length=20)
    professional_win = models.CharField(max_length=20)
    professional_loose = models.CharField(max_length=20) 
    professional_draw = models.CharField(max_length=20)


class k1_Record(models.Model):
    total = models.CharField(max_length=20)
    padded_win = models.CharField(max_length=20)
    padded_loose = models.CharField(max_length=20)
    padded_draw = models.CharField(max_length=20)
    armature_win = models.CharField(max_length=20)
    armature_loose = models.CharField(max_length=20)
    armature_draw = models.CharField(max_length=20)
    professional_win = models.CharField(max_length=20)
    professional_loose = models.CharField(max_length=20)
    professional_draw = models.CharField(max_length=20)


class Mod_Thai_Record(models.Model):
    total = models.CharField(max_length=20)
    padded_win = models.CharField(max_length=20)
    padded_loose = models.CharField(max_length=20)
    padded_draw = models.CharField(max_length=20)
    armature_win = models.CharField(max_length=20)
    armature_loose = models.CharField(max_length=20)
    armature_draw = models.CharField(max_length=20)
    professional_win = models.CharField(max_length=20)
    professional_loose = models.CharField(max_length=20)
    professional_draw = models.CharField(max_length=20)


class Muya_Thai_Record(models.Model):
    total = models.CharField(max_length=20)
    padded_win = models.CharField(max_length=20)
    padded_loose = models.CharField(max_length=20)
    padded_draw = models.CharField(max_length=20)
    armature_win = models.CharField(max_length=20)
    armature_loose = models.CharField(max_length=20)
    armature_draw = models.CharField(max_length=20)
    professional_win = models.CharField(max_length=20)
    professional_loose = models.CharField(max_length=20)
    professional_draw = models.CharField(max_length=20)



class MMA_Record(models.Model):
    total = models.CharField(max_length=20)
    classC_win = models.CharField(max_length=20)
    classC_loose = models.CharField(max_length=20)
    classC_draw = models.CharField(max_length=20)
    classB_win = models.CharField(max_length=20)
    classB_loose = models.CharField(max_length=20)
    classB_draw = models.CharField(max_length=20)
    classA_win = models.CharField(max_length=20)
    classA_loose = models.CharField(max_length=20)
    classA_draw = models.CharField(max_length=20)
    armature_win = models.CharField(max_length=20)
    armature_loose = models.CharField(max_length=20)
    armature_draw = models.CharField(max_length=20)
    professional_win = models.CharField(max_length=20)
    professional_loose = models.CharField(max_length=20)
    professional_draw = models.CharField(max_length=20)


class Martial_Art_Record(models.Model):
    Brazilian_Jiu_Jitsu_Style = models.CharField(max_length=20)
    Brazilian_Jiu_Jitsu_Rank = models.CharField(max_length=20)
    Brazilian_Jiu_Jitsu_Experience = models.CharField(max_length=20)
    Brazilian_Jiu_Jitsu_Total = models.CharField(max_length=20)
    Brazilian_Jiu_Jitsu_Win = models.CharField(max_length=20)
    Wrestling_Style = models.CharField(max_length=20)
    Wrestling_Rank = models.CharField(max_length=20)
    Wrestling_Experience = models.CharField(max_length=20)
    Wrestling_Total = models.CharField(max_length=20)
    Wrestling_Win = models.CharField(max_length=20)
    Taekwondo_WT_Style  = models.CharField(max_length=20)
    Taekwondo_WT_Rank = models.CharField(max_length=20)
    Taekwondo_WT_Experience = models.CharField(max_length=20)
    Taekwondo_WT_Total = models.CharField(max_length=20)
    Taekwondo_WT_Win = models.CharField(max_length=20)
    Taekwondo_ITF_Style = models.CharField(max_length=20)
    Taekwondo_ITF_Rank = models.CharField(max_length=20)
    Taekwondo_ITF_Experience = models.CharField(max_length=20)
    Taekwondo_ITF_Total = models.CharField(max_length=20)
    Taekwondo_ITF_Win = models.CharField(max_length=20)
    Judo_Style =  models.CharField(max_length=20)
    Judo_Rank =  models.CharField(max_length=20)
    Judo_Experience =  models.CharField(max_length=20)
    Judo_Total =  models.CharField(max_length=20)
    Judo_Win =  models.CharField(max_length=20)
    Kyokushin_Style = models.CharField(max_length=20)
    Kyokushin_Rank = models.CharField(max_length=20)
    Kyokushin_Experience = models.CharField(max_length=20)
    Kyokushin_Total = models.CharField(max_length=20)
    Kyokushin_Win = models.CharField(max_length=20)
    other_Style = models.CharField(max_length=20)
    Other_Rank = models.CharField(max_length=20)
    Other_Experience = models.CharField(max_length=20)
    Other_Total = models.CharField(max_length=20)
    Other_Win = models.CharField(max_length=20)


class register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

# class Add_event(models.Model):



# class countries(models.Model):
#     country = CountryField(blank_label='Sélectionner un pays', verbose_name='Pays de naissance')
    


