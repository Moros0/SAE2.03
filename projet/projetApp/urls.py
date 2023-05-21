from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machine/' , views.liste_machine_view , name = 'machine'),
    path('personnel/' , views.liste_personnel_view , name = 'personnel'),
    path('login/', views.login_view, name='login'),
    path('compte/', views.compte_view, name='compte'),
    path('machine/<pk>', views.machine_detail_view, name='machine_detail'),
    path('personnel/<pk>', views.personnel_detail_view, name='personnel_detail'),
    path('ajout_machine/', views.ajout_machine_view, name='ajout_machine'),

]