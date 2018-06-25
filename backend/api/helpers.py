from django.http import JsonResponse
from api.models import BoyName
from api.serializers import BoysNamesSerializer
from .email_sender import Mailer
from django.conf import settings


def send_email(request):

    if request.user.is_authenticated:

        serializer = BoysNamesSerializer(BoyName.objects.all(), many=True)

        names_items = list()

        for item in serializer.data:
            names_items.append({'name': item.get('name'),
                                'frequency': item.get('frequency'),
                                'average_age': item.get('average_age')})

        mail = Mailer()
        mail.send_messages(subject=settings.EMAIL_HEADER,
                           template='emails/customer_email.html',
                           context={
                               'customer': request.user.first_name,
                               'capt': [
                                   {
                                       'name': u'{}'.format('Namn').encode('utf-8'),
                                       'frequency': u'{}'.format('Förecomst').encode('utf-8'),
                                       'average_age': u'{}'.format('Snittalder').encode('utf-8')
                                   }
                               ],
                               'arr': names_items,
                           },
                           to_emails=[request.user.email])

    return JsonResponse({'status': 'Emain Send!'}, status=304)
