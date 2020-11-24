from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def cookie_samesite_none_not_secure(request):
    #HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=False, httponly=False, samesite=None)

    html = "<html><body>Check cookies. On mozilla if network.cookie.sameSite.laxByDefault is set in about.config you should get a warning because samesite is set None, but secure is not set.</body></html>"
    theresponse =  HttpResponse(html)
    theresponse.set_cookie("beer", value='sux', max_age=None, samesite=None)
    return theresponse



