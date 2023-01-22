from django.shortcuts import render

# Create your views here.
def ds(request):
    return render(request, 'ds.html', {})