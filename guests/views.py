import token
from django.http import HttpResponse
from django.shortcuts import redirect, render
from groom.models import Gifts, Guests

# Create your views here.
def guests(request):
    token = request.GET.get('token')
    guest = Guests.objects.get(token=token)
    gifts = Gifts.objects.filter(reserved=False).order_by('-significance')
    return render(request, 'guests.html', {'guest': guest, 'gifts': gifts})

def answer_attendance(request):
    answer = request.GET.get('answer')
    token = request.GET.get('token')
    guest = Guests.objects.get(token=token)

    if answer not in ['C', 'R']:
        return redirect(f'/guests/?token={token}')

    guest.status = answer
    guest.save()

    return redirect(f'/guests/?token={token}')

def reserve_gift(request, id):
     token = request.GET.get('token')
     guest = Guests.objects.get(token=token)
     gift = Gifts.objects.get(id=id)

     gift.reserved = True
     gift.reserved_by=guest
     gift.save()
     return redirect(f'/guests/?token={token}')