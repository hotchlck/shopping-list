from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'Salma Kurnia Dewi',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
