from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import format_html

from .models import Correo

@receiver(post_save, sender=Correo)
def enviar_notificacion_correo(sender, instance, created, **kwargs):
    if created:
        email = 'kleudyvictor@gmail.com'

        message = format_html(
            "<title>Portfolio</title>"
            "</head>"
            "<body>"          
            "<h4>Mensaje de <strong>{}</strong></h4>"
            "<hr/>"
            "<h2 style='color: blue;'><strong>{}</strong></h2>"
            "<p>{}</p>"
            "<hr/>"
            "<p>desde: <strong>{}</strong></p>"
            "<p>Fecha de Creación: <strong>{}</strong></p>"
            "</body>", instance.nombre,  instance.titulo, instance.comentario, instance.correo, instance.fecha_creacion.strftime("%d/%m/%Y"),
        )

        send_mail(
            "PORTFOLIO - Nuevo mensaje",
            "",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=message
        )