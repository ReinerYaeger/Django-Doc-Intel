from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


class IreaderView(View):

    def get(self, request):
        return render(request, "ireader/index.html")
