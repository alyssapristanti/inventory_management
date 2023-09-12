from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'application_name': 'Inventory Management',
        'name': 'Fathirahma Alyssa Pristanti',
        'class': 'PBP F'
    }

    return render(request, "inventory_main.html", context)