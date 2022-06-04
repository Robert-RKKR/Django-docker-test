from django.db import models

# Create your models here.

class SimpleBaseModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    # Model data time information:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Model status values:
    deleted = models.BooleanField(default=False)
    
    # Main model values:
    name = models.CharField(max_length=32, blank=False, unique=True)
    description = models.CharField(max_length=256)

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.created}'

    def __str__(self) -> str:
        return  f'{self.pk}: {self.created}'
