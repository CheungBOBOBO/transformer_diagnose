from django.db import models

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='oil_xml_file_%Y%m%d_%H%M%S')
