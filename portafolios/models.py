from django.db import models

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=70)
    tipo_proyecto = models.CharField(max_length=70)
    descripcion_proyecto = models.TextField(max_length=500)
    url_imagen = models.URLField(max_length=250)
    url_demo = models.URLField(max_length=250)
    url_github = models.URLField(max_length=250)
    prioridad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre_proyecto} - {self.tipo_proyecto}"
    
class ContactMessage(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=200, blank=True)
    contact_message = models.TextField()

    def __str__(self):
        return f"{self.contact_name} - {self.contact_subject}"
        
