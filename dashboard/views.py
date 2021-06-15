from django.shortcuts import render


def dashboard(request):
    page_title = 'Dashboard Admin E-Sentyment Analysis Jabar'
    return render(request, 'administrator/dashboard.html', {'page_title': page_title})
