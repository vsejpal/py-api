from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View Class"""

    def get(self, request, format=None):
        """Returns a list of ApiView features."""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URIs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})