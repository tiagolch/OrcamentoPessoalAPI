from django.shortcuts import render


def ReceitaList(request):
    return render(request, 'receita_list.html')