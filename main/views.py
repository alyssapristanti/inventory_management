from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'application name': 'Inventory Management',
        'name': 'Fathirahma Alyssa Pristanti',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)