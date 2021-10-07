from django.urls import path
from . import views

app_name= 'main' #nombre dinamico

urlpatterns = [
    path('index',views.index,name="homepage"),
    path('login_request',views.login_request, name="login2"),
    path('crearUsuario',views.crearUsuario, name="create"),
    path('publicacion',views.publicacion, name="publicar"),
    path('logout',views.logout_request, name="logout"),
]
