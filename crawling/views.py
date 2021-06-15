from django.shortcuts import render


def crawling(request):
    page_title = 'Crawling Tweet Admin E-Sentyment Analysis Jabar'
    return render(request, 'administrator/crawling.html', {'page_title': page_title})
