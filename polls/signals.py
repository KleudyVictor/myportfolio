from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html

from .models import Correo

@receiver(post_save, sender=Correo)
def enviar_notificacion_correo(sender, instance, created, **kwargs):
    if created:
        email = 'michelalejandro2406@gmail.com'
        
        # Leer el archivo HTML
        with open('./static/email.html', 'r') as file:
            html_message = file.read()

        html_message = html_message.format(
            nombre=instance.nombre,
            titulo=instance.titulo,
            comentario=instance.comentario,
            correo=instance.correo
        )

        send_mail(
            "PORTFOLIO - Nuevo mensaje",
            "",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=html_message
        )