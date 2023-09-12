# i have created this file - sreevardhan
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    # return HttpResponse('removepunc')
    analyzed =""
    if removepunc=="on":
        pnct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in pnct:
                analyzed+=char
        params = {'purpose':'removed punctuations','analysed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyse.html',params)    
    if capitalize=="on":
        analyzed =""
        analyzed =djtext.upper()
        params = {'purpose':'removed punctuations','analysed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyse.html',params)
    if newlineremover=="on":
        analyzed =""
        for char in djtext:
            if char != "\n" and char!="\r": 
                analyzed+=char
        params = {'purpose':'remove newline character','analysed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyse.html',params) 
    if spaceremover=="on":
        analyzed =""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                continue
            else:
                analyzed+=char
        params = {'purpose':'remove newline character','analysed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyse.html',params) 
    if charcount=="on":
        count=0
        for char in djtext:
            if char.isalpha():
                count+=1
        params = {'purpose':'remove newline character','analysed_text':count}
    if removepunc!="on" and capitalize!="on" and newlineremover!="on" and spaceremover!="on" and charcount!="on":
        return HttpResponse("Choose any operation and try again")
    return render(request,'analyse.html',params)