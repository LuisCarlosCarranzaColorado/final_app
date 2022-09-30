from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . import views
from .views import MyTokenObtainPairView

urlpatterns = [
    path('home', views.home, name='Home'),
    #path('login', views.login, name='login'),
    #path('login', MyTokenObtainPairView.as_view(), name='login'),
    #path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('newCustomer', views.newCustomer, name='newCustomer'),
    path('getAllCustomers', views.getAllCustomers, name='getAllCustomers'),
    path('getOneCustomer/<int:id>', views.getOneCustomer, name='getOneCustomer'),
    path('updateCustomer/<int:id>', views.updateCustomer, name='updateCustomer'),
    path('deleteCustomer/<int:id>', views.deleteCustomer, name='deleteCustomer'),
    path('account/newAccount', views.newAccount, name='newAccount'),
    path('account/updateAccount/<int:id>', views.updateAccount, name='updateAccount'),
    path('account/deleteAccount/<int:id>', views.deleteAccount, name='deleteAccount'),

    #path('login2', views.login, name='login2'),
    path('login2', MyTokenObtainPairView.as_view(), name='login2'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),

#url de usuario
    path('getAllUsuarios', views.getAllUsuarios, name='getAllUsuarios'),
    path('newUsuario', views.newUsuario, name='newUsuario'),
    path('updateUsuario/<int:id>', views.updateUsuario, name='updateUsuario'),
    path('deleteUsuario/<int:no_cedula>', views.deleteUsuario, name='deleteUsuario'),
    path('getOneMedico/<int:no_cedula>', views.getOneMedico, name='getOneMedico'),
    
#url de medicos
    path('getAllMedicos', views.getAllMedicos, name='getAllMedicos'),
    path('getOneMedico/<int:no_cedula>', views.getOneMedico, name='getOneMedico'),
    path('newMedico', views.newMedico, name='newMedico'),
    path('updateMedico/<int:no_cedula>', views.updateMedico, name='updateMedico'),
    path('deleteMedico/<int:no_cedula>', views.deleteMedico, name='deleteMedico'),

#url de secretario
    path('newSecretario', views.newSecretario, name='newSecretario'),
    path('getOneSecretario/<int:no_cedula>', views.getOneSecretario, name='getOneSecretario'),

#url de enfermero
    path('newEnfermero', views.newEnfermero, name='newEnfermero'),
    path('getOneEnfermero/<int:no_cedula>', views.getOneEnfermero, name='getOneEnfermero'),

#url de paciente
    path('getPacientes', views.getPacientes, name='getPacientes'),
    path('newPaciente', views.newPaciente, name='newPaciente'),
    path('getOnePaciente/<int:no_cedula>', views.getOnePaciente, name='getOnePaciente'),
#url de HC
    path('newHC', views.newHC, name='newHC'),
    path('getOneHC/<int:no_cedula>', views.getOneHC, name='getOneHC'),
    path('getAllHC', views.getAllHC, name='getAllHC'),

#url de acompanante
    path('newAcompanante', views.newAcompanante, name='newAcompanante'),
]
