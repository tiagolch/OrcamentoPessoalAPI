from datetime import date
from ninja import ModelSchema
from django.shortcuts import get_object_or_404
from typing import List
from ninja import NinjaAPI, Schema
from .models import Receita, Despesa


class ReceitaSchema(ModelSchema):
    class Config:
        model = Receita
        model_fields = "__all__"


api = NinjaAPI()


@api.get('/receitas/', response=List[ReceitaSchema])
def get_receitas(request):
    return Receita.objects.all()


@api.get('/receita/{id}/', response=ReceitaSchema)
def get_receita(request, id: int):
    receita = get_object_or_404(Receita, id=id)
    return receita


@api.post('/receita/')
def post_receita(request, payload: ReceitaSchema):
    receita = Receita.objects.create(**payload.dict())
    return {"msg": f"Receita com ID_{receita.id} Criado com sucesso!"}

