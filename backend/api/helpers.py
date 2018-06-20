from django.http import JsonResponse
from .email_sender import Mailer
from django.conf import settings


def send_email(request):
    print(request.user.email)

    mail = Mailer()
    mail.send_messages(subject=settings.EMAIL_HEADER,
                       template='emails/customer_email.html',
                       context={'customer': request.user},
                       to_emails=[request.user.email])

    return JsonResponse({'status': 'Emain Send!'}, status=304)
