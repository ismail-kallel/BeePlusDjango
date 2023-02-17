from django.urls import path
from . import views 


urlpatterns = [
    path('',views.correctif, name='correctif'),
    path('modifier_avis/',views.modifier_avis, name = 'modifier_avis'),
    path('bon_pour_ot/',views.bon_pour_ot, name = 'bon_pour_ot'),
    path('sqcdp/',views.sqcdp, name = 'sqcdp'),
    path('avis_form/<str:pk>/', views.createAvis, name='avis_form')
]
