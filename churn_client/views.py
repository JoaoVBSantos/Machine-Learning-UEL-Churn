import joblib
import os
import uuid

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChurnForm
from .models import ChurnModel
from django.http import JsonResponse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'chur.sav')
modelo = joblib.load(model_path)

def prever_churn(request):
    if request.method == 'POST':
        form = ChurnForm(request.POST)
        if form.is_valid():
            dados = [form.cleaned_data[campo] for campo in form.fields]

            
            try:
                resultado = modelo.predict([dados])[0]
            except Exception as e:
                print("Erro na predição:", e)
                raise e

            # Salvar no banco
            registro = ChurnModel(
                customerID=str(uuid.uuid4())[:8],
                Churn=resultado,
                NoInternetService=0,  # valor padrão
                **form.cleaned_data  # preencher os demais campos
            )
            registro.save()
            return redirect('lista_registros')
    else:
        form = ChurnForm()

    return render(request, 'churn_client/form.html', {'form': form})


def lista_registros(request):
    registros = ChurnModel.objects.all()
    return render(request, 'churn_client/list.html', {'registros': registros})


def editar_registro(request, pk):
    registro = get_object_or_404(ChurnModel, pk=pk)

    if request.method == 'POST':
        form = ChurnForm(request.POST)
        if form.is_valid():
            for campo in form.fields:
                setattr(registro, campo, form.cleaned_data[campo])

            # Atualizar classe manualmente
            registro.Churn = int(request.POST.get('Churn', registro.Churn))
            registro.save()
            return redirect('lista_registros')
    else:
        dados_iniciais = {campo: getattr(registro, campo) for campo in ChurnForm.base_fields}
        form = ChurnForm(initial=dados_iniciais)

    return render(request, 'churn_client/editar.html', {'form': form, 'registro': registro})


def dados_churn(request):
    churn_0 = ChurnModel.objects.filter(Churn=0).count()
    churn_1 = ChurnModel.objects.filter(Churn=1).count()
    return JsonResponse({'nao': churn_0, 'sim': churn_1})


def dados_contrato(request):
    contratos = {
        'Month-to-month': ChurnModel.objects.filter(Contract_MonthToMonth=1).count(),
        'One year': ChurnModel.objects.filter(Contract_OneYear=1).count(),
        'Two year': ChurnModel.objects.filter(Contract_TwoYear=1).count()
    }
    return JsonResponse({
        'labels': list(contratos.keys()),
        'valores': list(contratos.values())
    })

def dados_pagamento(request):
    metodos = {
        'Bank Transfer': ChurnModel.objects.filter(PaymentMethod_BankTransfer=1).count(),
        'Credit Card': ChurnModel.objects.filter(PaymentMethod_CreditCard=1).count(),
        'Electronic Check': ChurnModel.objects.filter(PaymentMethod_ElectronicCheck=1).count(),
        'Mailed Check': ChurnModel.objects.filter(PaymentMethod_MailedCheck=1).count(),
    }
    return JsonResponse({
        'labels': list(metodos.keys()),
        'valores': list(metodos.values())
    })

def dashboard(request):
    return render(request, 'churn_client/dashboard.html')