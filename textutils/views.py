


# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyse(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if fullcaps=='on':
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Change to UpperCase', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if newlineremover=='on':
        analysed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed = analysed + char
        params = {'purpose': 'Removed New Lines', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if spaceremover=='on':
        analysed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analysed = analysed + char
        params = {'purpose': 'Removed New Spaces', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)
    if charcount=='on':
        analysed = len(djtext)
        params = {'purpose': 'Find No of Characters', 'analysed_text': analysed}
        djtext = analysed
        #return render(request, 'analyse.html', params)


    if(removepunc != "on" and newlineremover != "on"and spaceremover != "on" and fullcaps != "on"):

        return render(request,'another.html')
    return render(request, 'analyse.html', params)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")





