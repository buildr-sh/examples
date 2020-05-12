from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    else:
        name = None

    return render(request, 'home.html', {
        'name': name
    })

