from django.db import models
import os

# Create your models here.

#skills
class Skill(models.Model):
    nombre_skill = models.CharField(max_length=50, verbose_name="Nombre")
    foto = models.FileField(upload_to='skill/')
    def __str__(self):
        return self.nombre_skill

#project
class Project(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(verbose_name="Descripción")
    foto = models.ImageField(upload_to='project/', null=True, blank=True, verbose_name="Foto")
    skills = models.ManyToManyField(Skill)
    url = models.URLField(null=True, blank=True, verbose_name="URL")

    def __str__(self):
        return self.nombre

#Correo
class Correo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    comentario = models.TextField(verbose_name="Comentario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.correo
