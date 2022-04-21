from django.shortcuts import render
from orcamentopessoal.models import Receita, Despesa
from django.db.models import Sum


def Dashboard(request):
    totalReceita = Receita.objects.all().aggregate(Sum('valor'))['valor__sum'] 
    totalDespesa = Despesa.objects.all().aggregate(Sum('valor'))['valor__sum']
    saldo = totalReceita - totalDespesa
    # print(total) 
    return render(request, 'dashboard.html', {'totalReceita': totalReceita, 'totalDespesa': totalDespesa, 'saldo': saldo})