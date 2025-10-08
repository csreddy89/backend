from django.http import HttpResponse

     
     
def home(request):
    return HttpResponse("Any kind of HTML Here")