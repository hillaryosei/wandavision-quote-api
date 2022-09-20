from django.http import JsonResponse
from .models import wandaVisionQuotes
from .serializers import QuoteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# post request


@api_view(['GET', 'POST'])
def quote_list(request, format=None):

    if request.method == 'GET':
        # get all quotes
        quotes = wandaVisionQuotes.objects.all()
        # serialize
        serializer = QuoteSerializer(quotes, many=True)
        # return json
        return JsonResponse({'quotes': serializer.data}, safe=False)

    if request.method == 'POST':
        # de-serialize quote
        serializer = QuoteSerializer(data=request.data)

        #check if data received is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def quote_detail(request, id, format=None):

    try:
        quote = wandaVisionQuotes.objects.get(pk=id)
    except wandaVisionQuotes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #set primary key to id
    #wandaVisionQuotes.objects.get(pk=id)

    if request.method == 'GET':
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuoteSerializer(quote, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        quote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)