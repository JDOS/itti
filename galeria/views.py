from django.shortcuts import render


def index(request):
    dados = {
        1:{
            "nome": "nome1",
            "legenda": "legenda1"
        },
        2:{
            "nome": "nome2",
            "legenda": "legenda2"
        }
    }

    return render(request,'galeria/index.html', {"cards":dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')