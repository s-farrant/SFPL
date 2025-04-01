from django.shortcuts import render

def HomeView(request):

    context = {}

    return render(request, 'a1_core/home.html', context) 