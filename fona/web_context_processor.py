from .models import web



def myweb(request):
    myweb = web.objects.last()
    return{"myweb":myweb}