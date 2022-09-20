from django.db import models


class wandaVisionQuotes (models.Model):
    name = models.CharField(max_length=200)
    quote = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ' ' + self.quote
