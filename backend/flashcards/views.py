from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardListCreateView(generics.ListCreateAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

class FlashcardDeleteView(generics.DestroyAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
