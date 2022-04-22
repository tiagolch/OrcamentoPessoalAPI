from django.shortcuts import render
from orcamentopessoal.models import Receita, Despesa
from django.db.models import Sum


def Dashboard(request):
    totalReceita = (Receita.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0)
    totalDespesa = (Despesa.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0)
    saldo = totalReceita - totalDespesa
    return render(request, 
                  'dashboard.html',
                  {
                    'totalReceita': totalReceita, 
                    'totalDespesa': totalDespesa, 
                    'saldo': saldo
                  }
                 )

