import joblib
import numpy as np
import os
from django.shortcuts import render, redirect
from django.views import View
from .models import ChurnModel
from .forms import ChurnForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model', 'chur.sav')
model = joblib.load(model_path)

class ChurnCreateView(View):
    def get(self, request):
        form = ChurnForm()
        return render(request, 'churn_client/form.html', {'form': form})

    def post(self, request):
        form = ChurnForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            features = [
                obj.Gender,
                obj.SeniorCitizen,
                obj.Partner,
                obj.Dependents,
                obj.tenure,
                obj.PhoneService,
                obj.MultipleLines_No,
                obj.MultipleLines_NoPhoneService,
                obj.MultipleLines_Yes,
                obj.InternetService_DSL,
                obj.InternetService_FiberOptic,
                obj.NoInternetService,
                obj.OnlineSecurity,
                obj.OnlineBackup,
                obj.DeviceProtection,
                obj.TechSupport,
                obj.StreamingTV,
                obj.StreamingMovies,
                obj.Contract_MonthToMonth,
                obj.Contract_OneYear,
                obj.Contract_TwoYear,
                obj.PaperlessBilling,
                obj.PaymentMethod_BankTransfer,
                obj.PaymentMethod_CreditCard,
                obj.PaymentMethod_ElectronicCheck,
                obj.PaymentMethod_MailedCheck,
                obj.MonthlyCharges
            ]

            prediction = model.predict([features])[0]
            obj.Churn = prediction
            obj.save()
            return redirect('listagem')
        return render(request, 'churn_client/form.html', {'form': form})

class ChurnListView(View):
    def get(self, request):
        registros = ChurnModel.objects.all()
        return render(request, 'churn_client/list.html', {'registros': registros})
