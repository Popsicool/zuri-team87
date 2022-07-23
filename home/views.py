from django.shortcuts import render

# Create your views here.
def HomeView(request):
    context = {}
    if request.method == 'POST':
        username= request.POST['username']
        context= {'username':username}
    return render(request, "home/index.html", context)
