from django.shortcuts import render
from .models import Usuario

def lista(request):
    conta = {
        'contas': Usuario.objects.all(),
    }
    return render(request, 'paginas/lista.html', conta)