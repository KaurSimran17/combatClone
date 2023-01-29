"""combat_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from combat_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name="index" ),
    # path('fighter/', views.fighter, name="fighter"),
    path('register/',views.register, name="register"),
    # path('additional/', views.additional, name="additional"),
    path('profile/', views.profile, name= "profile"),
    path('events/', views.events, name="events"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('fight_list/', views.fight_list, name="fight_list" ),
    path('personal/', views.personal, name="personal"),
    # path('login/', views.login, name="login" ),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.logout_page, name="logout"),
    # path('dummy/',views.dummy, name="dummy" ),
    path('edit/',views.edit, name="edit" ),
    path('fight/', views.fight, name="fight"),
    path('upcoming/', views.upcoming, name="upcoming" ),
    path('add_event/', views.add_event, name="add_event")
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

