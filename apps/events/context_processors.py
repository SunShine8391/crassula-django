from .models import Event


def get_first_promo_event(request):
    event = Event.objects.filter(is_active=True, promote=True).first()
    if event:
        return {'promo_event': event}
    return {'promo_event': ''}
