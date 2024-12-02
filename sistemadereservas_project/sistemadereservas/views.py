from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def sobre(request):
    html = '<html lang="pt-br"> <body>Ó pai ó</body></html>'
    return HttpResponse(html)

def minhainfo(request):
    html = '<html lang="pt-br"> <body> <h1>Minha Info</h1><p>Heloilson</p> <p>Idade:17</p> <p>Matrícula: 20221261020247</p> </body></html>'
    return HttpResponse(html)

def home(request):
    context = {
        'user': request.user 
    }
    return render(request, 'html/index.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            auth_login(request, user_obj)  # Correctly call the imported login function
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
            return redirect('login')  # Removed extra space

    return render(request, 'html/login.html')
