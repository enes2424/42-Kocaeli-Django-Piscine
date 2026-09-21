from django.http import HttpResponse

def showHelloWorld(request):
    return HttpResponse("Hello World!")
