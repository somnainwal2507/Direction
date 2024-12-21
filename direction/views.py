# I have created this file / Som Nainwal

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):

    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    analyzed = djtext

    char_count = sum(1 for char in djtext if char.isalpha())

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)

    if fullcaps == "on":
        analyzed = analyzed.upper()

    if newlineremover == "on":
        analyzed = analyzed.replace('\n', ' ').replace('\r', '')

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on":
        return HttpResponse("Error: No options selected. Please select at least one operation.")

    params = {'purpose': 'Text Analysis', 'analyzed_text': analyzed}

    if charcounter == "on":
        params['char_count'] = char_count

    return render(request, 'analyze.html', params)

def about(request):
    return render(request,'about.html',)

def contact(request):
    return render(request,'contact.html')

from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the form...
        messages.success(request, 'Your message has been sent successfully!')
        return render(request, 'contact.html')
    return render(request, 'contact.html')
