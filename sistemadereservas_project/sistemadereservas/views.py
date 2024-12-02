from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sobre (request):
    html='<html lang="pt-br"> <body>Ó pai ó</body></html>'
    return HttpResponse(html)
def minhainfo(request):
    html='<html lang="pt-br"> <body> <h1>Minha Info</h1><p>Heloilson</p> <p>Idade:17</p> <p>Matrícula: 20221261020247</p> </body></html>'
    return HttpResponse(html)

