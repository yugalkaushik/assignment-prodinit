from django.urls import path
from .views import FlashcardListCreateView, FlashcardDeleteView

urlpatterns = [
    path('flashcards/', FlashcardListCreateView.as_view(), name='flashcard-list-create'),
    path('flashcards/<int:pk>/', FlashcardDeleteView.as_view(), name='flashcard-delete'),
]
