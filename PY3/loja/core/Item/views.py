from django.shortcuts import render

# Create your views here.
def lista_categorias(request):
    return render(request, 'lista_categorias.html')

def cadastra_categoria(request):
    return render(request, 'cadastra_categoria.html')

def altera_categoria(request):
    return render(request, 'altera_categoria.html')
    
def lista_itens(request):
    return render(request, 'lista_itens.html')

def cadastra_item(request):
    return render(request, 'cadastra_item.html')

def altera_item(request):
    return render(request, 'altera_item.html')