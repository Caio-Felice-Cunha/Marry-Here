from django.shortcuts import get_object_or_404, redirect, render
from groom.models import Gifts, Guests

# Create your views here.
def guests(request):
    token = request.GET.get('token')
    guest = get_object_or_404(Guests, token=token)
    gifts = Gifts.objects.filter(reserved=False).order_by('-significance')
    return render(request, 'guests.html', {'guest': guest, 'gifts': gifts})

def answer_attendance(request):
    answer = request.GET.get('answer')
    token = request.GET.get('token')
    guest = get_object_or_404(Guests, token=token)

    if answer not in ['C', 'R']:
        return redirect(f'/guests/?token={token}')

    guest.status = answer
    guest.save()

    return redirect(f'/guests/?token={token}')

def reserve_gift(request, id):
    token = request.GET.get('token')
    guest = get_object_or_404(Guests, token=token)
    gift = get_object_or_404(Gifts, id=id)

    # Do not let a guest overwrite a gift that is already reserved.
    if gift.reserved:
        return redirect(f'/guests/?token={token}')

    gift.reserved = True
    gift.reserved_by = guest
    gift.save()
    return redirect(f'/guests/?token={token}')
