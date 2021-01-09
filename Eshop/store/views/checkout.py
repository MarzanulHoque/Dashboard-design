from django.shortcuts import render, redirect
from django.views import View


class CheckOut(View):
    def post(self, request):
        print(request.POST)
        return redirect('/cart')
