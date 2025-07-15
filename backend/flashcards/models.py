from django.db import models

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    tag = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.question[:50]}..."
    
    class Meta:
        ordering = ['-created_at']
