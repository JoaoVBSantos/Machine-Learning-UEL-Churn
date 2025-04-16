from django.shortcuts import render
from django.views import View


class IrisListView(View):
    
    def get(self, request):
        context = {}
        return render(request, 'appiris/lists.html', context=context)
    
