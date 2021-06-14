from django.shortcuts import render
# Create your views here.

def index(request):
    if request.method == "POST":
        author_name = request.POST['name']
        book = request.POST['book']
        email = request.POST['email']
        props = {'name': author_name, 'book': book, 'email': email}
        return render(request, 'index.html', props)
    return render(request, 'index.html')