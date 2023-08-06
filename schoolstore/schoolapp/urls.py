from django.urls import path
from . import views


urlpatterns = [
   path('', views.home, name='home'),
   path('commerce', views.commerce, name='commerce'),
   path('science', views.science, name='science'),
   path('architecture', views.architecture, name='architecture'),
   path('fashion_design', views.fashion_design, name='fashion_design'),
   path('inf_technology', views.inf_technology, name='inf_technology'),
   path('login', views.login, name='login'),
   path('register/', views.register,name='register'),
   path('requirements',views.requirements,name='requirements'),
   path('logout',views.logout,name='logout'),
   path('ordconfirm',views.ordconfirm,name='ordconfirm')


]