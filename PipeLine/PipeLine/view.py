from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    
    return  render(request, 'index.html')
 



def analyze(request):

    #fetch Value
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    fullupper = request.GET.get('fullupper','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspace = request.GET.get('extraspace','off')
    
    
    #analyzed = djtext

    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        parms = {'purpose':"Removed Text",'analyze_text':analyzed}

        return render(request,'analyze.html',parms)
    elif(fullupper == 'on'):
            analyzed = ""
            for char in djtext:
                analyzed = char.upper()+analyzed
            parms = {'purpose':'Full UpperCase','analyze_text':analyzed}

            return render(request,'analyze.html',parms)

    elif(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        parms= {'purpose':'New Line Remove','analyze_text':analyzed} 
        return render(request,'analyze.html',parms)
    elif(extraspace == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        parms= {'purpose':'New Line Remove','analyze_text':analyzed} 
        return render(request,'analyze.html',parms)
        



    else:
        return HttpResponse("Error")




# def capfirst(request):
#     return HttpResponse("capfirst")
    



# def newlineremove(request):
#     return HttpResponse("newlineremove")
    

# def spaceremove(request):
#     return HttpResponse("spaceremove")


# def charcount(request):
#         return HttpResponse("charcount")
    

    
