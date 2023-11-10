from django.db import models
from tinymce.models import HTMLField


class TextInformation(models.Model):
    header = models.CharField('Header', max_length=200, null=False, blank=False)
    text = HTMLField('Text', max_length=5000, null=False, blank=False)

    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name = 'Text information'
        verbose_name_plural = 'Texts information'


class Certificate(models.Model):
    school = models.CharField('School name', max_length=200, null=False, blank=False)
    course = models.CharField('Course name', max_length=200, null=False, blank=False)
    duration = models.CharField('Course duration', max_length=200, null=True, blank=True)
    date = models.DateField('Certificate date', null=True, blank=True)
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return f'{self.course} from {self.school}'
    
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'