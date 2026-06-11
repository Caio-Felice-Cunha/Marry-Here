from django.shortcuts import redirect, render
from .models import Gifts, Guests

# Create your views here.
def home(request):
    if request.method == 'GET':
        all_gifts = Gifts.objects.all()
        not_reserved = Gifts.objects.filter(reserved=False).count()
        reserved = Gifts.objects.filter(reserved=True).count()
        data = [not_reserved, reserved]
        return render(request, 'home.html', {'all_gifts': all_gifts, 'data':data})

    elif request.method == 'POST':
        gift_name       = request.POST.get('gift_name')
        photo           = request.FILES.get('photo')
        price           = request.POST.get('price')

        try:
            significance = int(request.POST.get('significance'))
        except (TypeError, ValueError):
            return redirect('home')

        if significance < 1 or significance > 5:
            return redirect('home')

        gifts = Gifts(
            gift_name = gift_name
            , photo=photo
            , price=price
            , significance=significance
        )

        gifts.save()

        return redirect('home')

def guests_list(request):
    if request.method == "GET":
        guests = Guests.objects.all()
        return render(request, 'guests_list.html', {'guests':guests})
    elif request.method == "POST":
        guest_name = request.POST.get('guest_name')
        whatsapp = request.POST.get('whatsapp')

        try:
            maximum_companions = int(request.POST.get('maximum_companions'))
        except (TypeError, ValueError):
            maximum_companions = 0

        guests = Guests(
            guest_name=guest_name,
            whatsapp=whatsapp,
            maximum_companions=maximum_companions
        )

        guests.save()

        return redirect('guests_list')

    
