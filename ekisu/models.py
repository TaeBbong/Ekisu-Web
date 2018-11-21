from django.db import models

# Create your models here.
class Text(models.Model):
    inputContent = models.TextField()
    ratio = models.CharField(max_length=10)
    outputContent = models.TextField()

    def __str__(self):
        return { 'inputContent': self.inputContent, 'ratio': self.ratio, 'outputContent': self.outputContent }