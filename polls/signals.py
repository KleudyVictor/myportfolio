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
            "<h2>Mensaje de <strong>{}</strong></h2>"
            "<p>desde: <strong>{}</strong></p>"
            "<h6>Título: <strong>{}</strong></h6>"
            "<p>Comentario: <strong>{}</strong></p>"
            "<p>Fecha de Creación: <strong>{}</strong></p>"
            "</body>", instance.nombre, instance.correo, instance.titulo, instance.comentario, instance.fecha_creacion.strftime("%d/%m/%Y"),
        )

        send_mail(
            "Nuevo mensaje recibido",
            "",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=message
        )