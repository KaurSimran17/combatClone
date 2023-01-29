from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from combat_app.models import Promoter, Sanctioning, Medics,Role , Fighter, Gym_Owner, Coach, Event_Calendar, Gym_info,Boxing_Record, k1_Record, Mod_Thai_Record,Muya_Thai_Record, MMA_Record, Martial_Art_Record,Achivements
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from countryinfo import countryinfo


# Create your views here.


def index(request):
    if request.method == "POST":
        global cat
        cat =  request.POST["role"]
        if cat == "fighter":  
            return redirect(fight)
        else:
            return redirect(register)
    else:
        HttpResponse("Please select One")


    return render(request, "index.html")


# def fighter(request):
#     return render(request, "fighter.html")
 
# def additional(request):
#     if request.method == "POST":
#         fights_name = request.POST["fight_name"]
#         fight_weight = request.POST["fight_weight"] 
#         wight_units = request.POST["weight_units"]
#         fight_height = request.POST["fight_height"]
#         hight_units = request.POST["height_units"]
#         gym_name = request.POST["gym_name"]
#         datas =Additional_fighter(fight_name=fights_name, fight_weight=fight_weight, wight_units=wight_units, fight_height=fight_height,
#                     height_units=hight_units, gym_name=gym_name)
#         datas.save()
#         return redirect(profile)
#         # return HttpResponse("<h1 style='color:green;'>Data Saved Successfully!</h1>")

#     return render(request, "additional.html")


def register(request):
    
    if request.method == "POST":
            fnm = request.POST["fname"]
            lnm = request.POST["lname"]
            prof= request.FILES["profile"]
            em = request.POST["email"]
            cont = request.POST["contact"]
            gen = request.POST["gender"]
            dy = request.POST["date"]
            mon = request.POST["month"]
            yer = request.POST["year"]
            cit = request.POST["city"]
            tow = request.POST["town"]
            cntry = request.POST["country"]
            docs = request.FILES["document"]
            passw = request.POST["password"]

            if cat == "sanctioning":

                sanc_data = Sanctioning(fname=fnm, lname=lnm, profile=prof, email=em, contact=cont, gender=gen,
                            date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry, document=docs, password=passw)
                sanc_data.save()
                my_user = User.objects.create_user(fnm,em,passw)
                my_user.save()

            if cat == "promoter":
                prom_data = Promoter(fname=fnm, lname=lnm, profile=prof, email=em, contact=cont, gender=gen,
                            date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry, document=docs, password=passw)
                prom_data.save()
                my_user = User.objects.create_user(fnm,em,passw)
                my_user.save()

            if cat =="medics":
                med_data = Medics(first_name=fnm, last_name=lnm, profile=prof, email=em, contact=cont, gender=gen,
                            date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry, document=docs, password=passw)
                med_data.save()
                my_user = User.objects.create_user(fnm,em,passw)
                my_user.save()

            if cat == "gym_owner":
                gy_data = Gym_Owner(first_name=fnm, last_name=lnm, profile=prof, email=em, contact=cont, gender=gen,
                            date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry, document=docs, password=passw)
                gy_data.save()
                my_user = User.objects.create_user(fnm,em,passw)
                my_user.save()

            if cat == "coach":
                coach_data = Coach(fname=fnm, lname=lnm, profile=prof, email=em, contact=cont, gender=gen,
                            date=dy, month=mon, year=yer, city=cit, town=tow, country=cntry, document=docs, password=passw)                
                coach_data.save()

                my_user = User.objects.create_user(fnm,em,passw)
                my_user.save()
            return redirect(profile)


    return render(request, "register.html")

@login_required(login_url='signin')
def profile(request):
    
    prof = Fighter.objects.all()
    return render(request, "profile.html", {'profile':prof})

# def prac(request):
#     data_save  = Sanctioning.objects.all()
#     print(data_save)
#     return render(request, "prac.html", {'all':data_save})


                                            # GYM-INFORMATION ENTRIES
@login_required(login_url='signin')
def edit_profile(request):
    if request.method=="POST":
        gnm = request.POST["gym_name"]
        dis = request.POST["discipline"]
        url = request.POST["gym_url"]
        em = request.POST["email"]
        appa = request.POST["apartment"]
        tow = request.POST["town"]
        cit = request.POST["city"]
        count = request.POST["country"]
        phn = request.POST["phone_number"]
        mob = request.POST["mobile"]
        hd_ch = request.POST["head_coach"]
        ad_ch = request.POST["add_coach"]

        data = Gym_info(gym_name = gnm,url_link= url, discipline= dis, email=em, apartment= appa, city= cit, town = tow, country= count, phone_number= phn, mobile= mob, head_coach = hd_ch, additi_coach = ad_ch)
        data.save()

                                            # BOXING-RECORD ENTRIES


        box_tot = request.POST["box_total"]
        box_cor_win = request.POST["box_corp_win"]
        box_cor_loose = request.POST["box_corp_loose"]
        box_cor_draw = request.POST["box_corp_draw"]
        box_arm_win = request.POST["box_arm_win"]
        box_arm_loose = request.POST["box_arm_loose"]
        box_arm_draw = request.POST["box_arm_draw"]
        box_pro_win = request.POST["box_prof_win"]
        box_pro_loose = request.POST["box_prof_loose"]
        box_pro_draw = request.POST["box_prof_draw"]

        data2= Boxing_Record(total=box_tot,corporate_win=box_cor_win, corporate_loose=box_cor_loose,corporate_draw=box_cor_draw,armature_win= box_arm_win,
        armature_loose=box_arm_loose,armature_draw=box_arm_draw,professional_win=box_pro_win,professional_loose= box_pro_loose,professional_draw=box_pro_draw )
        data2.save()

                                            # K1 RECORD ENTRIES

        
        k1_tot = request.POST["k1_total"]
        k1_cor_win = request.POST["k1_corp_win"]
        k1_cor_loose = request.POST["k1_corp_loose"]
        k1_cor_draw = request.POST["k1_corp_draw"]
        k1_arm_win= request.POST["k1_arm_win"]
        k1_arm_loose= request.POST["k1_arm_loose"]
        k1_arm_draw= request.POST["k1_arm_draw"]
        k1_pro_win= request.POST["k1_prof_win"]
        k1_pro_loose= request.POST["k1_prof_loose"]
        k1_pro_draw= request.POST["k1_prof_draw"]

        data3= k1_Record(total= k1_tot, padded_win= k1_cor_win, padded_loose= k1_cor_loose, padded_draw = k1_cor_draw, armature_win= k1_arm_win, armature_loose=k1_arm_loose,
        armature_draw= k1_arm_draw, professional_win= k1_pro_win, professional_loose= k1_pro_loose, professional_draw= k1_pro_draw)
        data3.save()

                                            # MOD THAI RECORD ENTRIES

        
        mod_tot = request.POST["mod_total"]
        mod_cor_win = request.POST["mod_corp_win"]
        mod_cor_loose = request.POST["mod_corp_loose"]
        mod_cor_draw = request.POST["mod_corp_draw"]
        mod_arm_win= request.POST["mod_arm_win"]
        mod_arm_loose= request.POST["mod_arm_loose"]
        mod_arm_draw= request.POST["mod_arm_draw"]
        mod_pro_win= request.POST["mod_prof_win"]
        mod_pro_loose= request.POST["mod_prof_loose"]
        mod_pro_draw= request.POST["mod_prof_draw"]

        data4= Mod_Thai_Record(total= mod_tot, padded_win= mod_cor_win, padded_loose= mod_cor_loose, padded_draw = mod_cor_draw, armature_win= mod_arm_win, armature_loose=mod_arm_loose,
        armature_draw= mod_arm_draw, professional_win= mod_pro_win, professional_loose= mod_pro_loose, professional_draw= mod_pro_draw)
        data4.save()

                                            # MUYA-THAI RECORD ENTRIES


        muya_tot = request.POST["muya_total"]
        muya_cor_win = request.POST["muya_corp_win"]
        muya_cor_loose = request.POST["muya_corp_loose"]
        muya_cor_draw = request.POST["muya_corp_draw"]
        muya_arm_win= request.POST["muya_arm_win"]
        muya_arm_loose= request.POST["muya_arm_loose"]
        muya_arm_draw= request.POST["muya_arm_draw"]
        muya_pro_win= request.POST["muya_prof_win"]
        muya_pro_loose= request.POST["muya_prof_loose"]
        muya_pro_draw= request.POST["muya_prof_draw"]

        data5 = Muya_Thai_Record(total = muya_tot, padded_win =muya_cor_win, padded_loose= muya_cor_loose, padded_draw= muya_cor_draw, armature_win=muya_arm_win, armature_loose = muya_arm_loose, armature_draw= muya_arm_draw,professional_win= muya_pro_win,
        professional_loose =muya_pro_loose,professional_draw= muya_pro_draw )
        data5.save()


                                            # ACHIEVEMENT RECORD ENTRIES

        if request.method == "POST":
            year = request.POST["year"]
            amature = request.POST["amature"]
            weight = request.POST["weight"]
            discipline = request.POST["discipline"]
            sanction = request.POST["sanction"]
            rule = request.POST["rule"]
            achievment = request.POST["achieve"]

            achieve_data =Achivements(year = year, amature_pro= amature, weight= weight, discipline= discipline, sanction= sanction, rule_set= rule, achivement= achievment)
            achieve_data.save()


                                            # MMA RECORDS ENTRIES
        
        if request.method == "POST":
            mma_total = request.POST["mma_total"]
            class_C_win = request.POST["class_C_win"]
            class_C_loose = request.POST["class_C_loose"]
            class_C_draw = request.POST["class_C_draw"]
            class_B_win = request.POST["class_B_win"]
            class_B_loose = request.POST["class_B_loose"]
            class_B_draw = request.POST["class_B_draw"]
            class_A_win = request.POST["class_A_win"]
            class_A_loose = request.POST["class_A_loose"]
            class_A_draw = request.POST["class_A_draw"]
            mma_arm_win = request.POST["mma_arm_win"]
            mma_arm_loose = request.POST["mma_arm_loose"]
            mma_arm_draw = request.POST["mma_arm_draw"]
            mma_prof_win = request.POST["mma_prof_win"]
            mma_prof_loose = request.POST["mma_prof_loose"]
            mma_prof_draw = request.POST["mma_prof_draw"]

            mma_data = MMA_Record(total=mma_total, classC_win =class_C_win,classC_loose=class_C_loose ,classC_draw= class_C_draw,classB_win= class_B_win,classB_loose=class_B_loose,
            classB_draw=class_B_draw,classA_win=class_A_win,classA_loose=class_A_loose,classA_draw=class_A_draw,armature_win=mma_arm_win,armature_loose=mma_arm_loose,armature_draw=mma_arm_draw,
            professional_win=mma_prof_win,professional_loose=mma_prof_loose,professional_draw=mma_prof_draw)
            mma_data.save()

                                            # MARTIAL-ART RECORD ENTRIES


        brz_style = request.POST["brazilian_style"]
        brz_rank = request.POST["brazilian_rank"]
        brz_exp = request.POST["brazilian_exp"]
        brz_total = request.POST["brazilian_total"]
        brz_win = request.POST["brazilian_win"]
        wrest_style = request.POST["wrestling_style"]
        wrest_rank = request.POST["wrestling_rank"]
        wrest_exp = request.POST["wrestling_exp"]
        wrest_total = request.POST["wrestling_total"]
        wrest_win = request.POST["wrestling_win"]
        taekwon_style = request.POST["taekwondo_style"]
        taekwon_rank = request.POST["taekwondo_rank"]
        taekwon_exp = request.POST["taekwondo_exp"]
        taekwon_total = request.POST["taekwondo_total"]
        taekwon_win = request.POST["taekwondo_win"]
        taekwon_itf_style = request.POST["taekwondo_itf_style"]
        taekwon_itf_rank = request.POST["taekwondo_itf_rank"]
        taekwon_itf_exp = request.POST["taekwondo_itf_exp"]
        taekwon_itf_total = request.POST["taekwondo_itf_total"]
        taekwon_itf_win = request.POST["taekwondo_itf_win"]
        judo_style = request.POST["judo_style"]
        judo_rank = request.POST["judo_rank"]
        judo_exp = request.POST["judo_exp"]
        judo_total = request.POST["jdzo_total"]
        judo_win = request.POST["juzo_win"]
        kyok_style = request.POST["kyokushin_style"]
        kyok_rank = request.POST["kyokushin_rank"]
        kyok_exp = request.POST["kyokushin_exp"]
        kyok_total = request.POST["kyokushin_total"]
        kyok_win = request.POST["kyokushin_win"]

        data6 = Martial_Art_Record(Brazilian_Jiu_Jitsu_Style= brz_style, Brazilian_Jiu_Jitsu_Rank=brz_rank, Brazilian_Jiu_Jitsu_Experience=brz_exp,Brazilian_Jiu_Jitsu_Total=brz_total,Brazilian_Jiu_Jitsu_Win=brz_win,
        Wrestling_Style=wrest_style, Wrestling_Rank=wrest_rank,Wrestling_Experience=wrest_exp,Wrestling_Total=wrest_total,Wrestling_Win=wrest_win,Taekwondo_WT_Style=taekwon_style, Taekwondo_WT_Rank=taekwon_rank, 
        Taekwondo_WT_Experience=taekwon_exp, Taekwondo_WT_Total=taekwon_total, Taekwondo_WT_Win=taekwon_win, Taekwondo_ITF_Style=taekwon_itf_style, Taekwondo_ITF_Rank=taekwon_itf_rank, Taekwondo_ITF_Experience=taekwon_itf_exp,
        Taekwondo_ITF_Total= taekwon_itf_total, Taekwondo_ITF_Win=taekwon_itf_win, Judo_Style=judo_style,Judo_Rank=judo_rank, Judo_Experience=judo_exp, Judo_Total= judo_total, Judo_Win= judo_win, Kyokushin_Style=kyok_style, 
        Kyokushin_Rank=kyok_rank, Kyokushin_Experience=kyok_exp, Kyokushin_Total= kyok_total, Kyokushin_Win= kyok_win)
        data6.save()

        return HttpResponse(" <h1 style='color:green;'>Data Saved Successfully!</h1> ")


    return render(request, "Edit-Profile2.html")

def events(request):
    prof = Fighter.objects.all()
    event = Event_Calendar.objects.all()
    context = {'eve': event, 'fight':prof}
    return render(request, "events.html", context)



def admin_page(request):
    fight = Fighter.objects.all()
    sanc = Sanctioning.objects.all()
    med = Medics.objects.all()
    gym = Gym_Owner.objects.all()
    prom = Promoter.objects.all()
    mod = Mod_Thai_Record.objects.all()
    coa = Coach.objects.all()
    sanctions = sanc.count()
    registers = fight.count()
    mods = mod.count()
    medic = med.count()
    gym_own = gym.count()
    coac = coa.count()
    pro = prom.count()
    use = User.objects.all()
    context = {'register_count':registers,
                'sanc':sanctions,
                'mod_thai':mods,
                'medics':medic,
                'gym':gym_own,
                'coach':coac,
                'promoter':pro,
                'user':use
    }
    return render(request, "admin.html", context)

def fight_list(request):
    fight = Fighter.objects.all()
    return render(request, "fight_list.html", {'fighter':fight} )

def personal(request):
    fight = Fighter.objects.filter(first_name = "Mohd")
    gym = Gym_info.objects.all()
    corp = Boxing_Record.objects.all()
    k1 = k1_Record.objects.all()
    mods=Mod_Thai_Record.objects.all()
    muya= Muya_Thai_Record.objects.all()
    context = {
        'fighter':fight,
        'gym_info':gym,
        'corp':corp,
        'k1_data':k1,
        'mod':mods,
        'muya':muya

    }
    # print(gym)
    return render(request, "personal.html", context)

# def login(request):
#     if request.method == "POST":
#         un = request.POST["username"]
#         pwd = request.POST["password"] 
  
#         user = authenticate(username=un, password = pwd) 
#         if user:
#             return HttpResponseRedirect("/admin")
#         else:
#             return HttpResponse(user)
            
#     return render(request, "login.html")

def signin(request):
    if request.method == "POST":
        email_1 = request.POST.get('email_id')
        username = User.objects.get(email=email_1).username
        pass1 = request.POST.get('password_id')
        
        user = authenticate(request, username = username, password = pass1)
        if user is not None:                                    
            login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect(profile)
        else:
            messages.error("Invalid Credentials, Please try again")
    return render(request, "signin.html") 


def logout_page(request):
    logout(request)
    return redirect(signin)

def edit(request):
    if request.method == "POST":
            year = request.POST["year"]
            amature = request.POST["amature"]
            weight = request.POST["weight"]
            discipline = request.POST["discipline"]
            sanction = request.POST["sanction"]
            rule = request.POST["rule"]
            achievment = request.POST["achieve"]

            achieve_data =Achivements(year = year, amature_pro= amature, weight= weight, discipline= discipline, sanction= sanction, rule_set= rule, achivement= achievment)
            achieve_data.save()
    return render(request, "Edit-Profile2.html")


def fight(request):
    if request.method == "POST":
            fnm = request.POST["fname"]
            lnm = request.POST["lname"]
            profiles = request.FILES["profile"]
            em = request.POST["email"]
            cont = request.POST["contact"]
            gen = request.POST["gender"]
            dy = request.POST["date"]
            mon = request.POST["month"]
            yer = request.POST["year"]
            cit = request.POST["city"]
            tow = request.POST["town"]
            cntry = request.POST["country"]
            docs = request.FILES["document"]
            passw = request.POST["password"]
            fights_name = request.POST["fight_name"]
            fight_weight = request.POST["fight_weight"] 
            wight_units = request.POST["weight_units"]
            fight_height = request.POST["fight_height"]
            hight_units = request.POST["height_units"]
            discipline = request.POST["discipline"]
            gym_name = request.POST["gym_name"]
            
            data = Fighter(first_name=fnm, last_name=lnm, profile=profiles, email=em, contact=cont, gender=gen, date=dy, month=mon, year=yer, city=cit, town=tow,
                           country=cntry, document=docs, password=passw,fight_name=fights_name, fight_weight=fight_weight, wight_units=wight_units, fight_height=fight_height,
                           height_units=hight_units,discipline=discipline ,gym_name=gym_name)
            data.save()
            # my_user = User.objects.create_user(fnm,em,passw)
            # my_user.save()
            # return HttpResponse("Created")
            return redirect(profile)
    return render(request, "fighter.html")


def upcoming(request):

    return render(request, "upcoming.html")


def add_event(request):
    event = Event_Calendar.objects.all()
    context = {"eve": event}
    return render(request, "add_event.html", context)

