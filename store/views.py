from django.shortcuts import render
from django.views import View


class StoreView(View):

    def get(self, request):
        return render(request, 'store.html')
    
