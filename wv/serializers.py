from rest_framework import serializers
from .models import wandaVisionQuotes

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = wandaVisionQuotes
        fields = ['id', 'name', 'quote']