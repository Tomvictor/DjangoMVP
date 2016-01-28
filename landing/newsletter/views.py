from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Welcome Guest user'
    if request.user.is_authenticated() :
        title = 'Welcome %s' %(request.user)
    context={
        "title" : title
    }
    return render(request,"home.html", context )