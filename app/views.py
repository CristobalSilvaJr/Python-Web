from django.shortcuts import render,redirect 
from app.models import Usuario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'app/index.html',{'usuarios': Usuario.objects.all}) #Mostramos los objetos creados.

def login_request(request): #Creacion del inicio de sesion

    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password')
            user=authenticate(username=usuario,password=contraseña)
            if user is not None:
                login(request, user)
                messages.info(request, f"!Hola {usuario}¡")
                return redirect("main:homepage")
            else:
                messages.error(request,"oops... Usuario o contraseña Incorrecto ")  
        else:
                messages.error(request,"oops... Usuario o contraseña Incorrecto ")  

    form= AuthenticationForm()
    return render(request,'app/login.html', {"form":form})

def publicacion(request):
    return render(request,'app/publicacion.html')

def crearUsuario(request):
    if request.method =="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            usuarios= form.save() #Guardamos usuario
            nombre_get= form.cleaned_data.get('username')
            messages.success(request, f"Nueva cuenta creada :{nombre_get}")
            login(request, usuarios)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:#message=diccionario, msg=llave
                messages.error(request, f"{msg}:form.error_messagges[msg]")
        
    form= UserCreationForm
    return render(request,'app/crearUsuario.html', {"form":form})

def logout_request(request): #Cerramos Sesion
    logout(request)
    print('<script>alert("Sesion Cerrada")</script>')
    return redirect("main:homepage")

