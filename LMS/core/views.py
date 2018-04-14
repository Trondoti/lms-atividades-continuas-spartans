from django.shortcuts import render
from django.http import HttpResponse
from core.utils.utils import calculaMediaFinal


def index(request):
    return render(request,"index.html")

'''def index(request):
    #return HttpResponse('login')
    return HttpResponse(calculaMediaFinal(8,4))   '''

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        user=request.POST.get("email")
        if request.POST.get("senha") != "teste123":
            print ("Usuário {0} digitou senha errada" .format (user))
            # A função render não redireciona -- veja essa função https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#redirect
            return render(request,"login.html")
        else:
            print ("Usuário {0} entrou com sucesso" .format (user))
            return render(request, "index.html")

def contato (request):
    if request.method=="GET":
        return render (request,"contato.html")
    else:
        print (request.POST.get("nome"))
        print (request.POST.get("email"))
        print (request.POST.get("assunto"))
        print (request.POST.get("Mensagem"))
        print (request.POST.get("telefone"))
    return render(request,"contato.html")
    
   