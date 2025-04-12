from django.shortcuts import render

# Create your views here.


def landing_page(request):
    context = {
        'message': 'This is dynamic data from Django!',
        'items': ['Apple', 'Banana', 'Cherry']
    }
    return render(request, 'furniture/index.html', context)
