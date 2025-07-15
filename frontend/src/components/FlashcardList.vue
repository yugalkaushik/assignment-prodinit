<template>
  <div>
    <h2 class="section-title">Your Flashcards</h2>
    
    <div v-if="flashcards.length === 0" class="empty-state">
      <h3>No flashcards yet</h3>
      <p>Create your first flashcard above to get started!</p>
    </div>
    
    <div v-else class="grid">
      <FlashcardItem
        v-for="flashcard in flashcards"
        :key="flashcard.id"
        :flashcard="flashcard"
        @delete-flashcard="deleteFlashcard"
      />
    </div>
  </div>
</template>

<script>
import FlashcardItem from './FlashcardItem.vue'

export default {
  name: 'FlashcardList',
  components: {
    FlashcardItem
  },
  props: {
    flashcards: {
      type: Array,
      required: true
    }
  },
  emits: ['flashcard-deleted'],
  setup(props, { emit }) {
    const deleteFlashcard = async (id) => {
      try {
        const response = await fetch(`http://localhost:8000/api/flashcards/${id}/`, {
          method: 'DELETE'
        })
        
        if (response.ok) {
          emit('flashcard-deleted')
        } else {
          console.error('Failed to delete flashcard')
        }
      } catch (error) {
        console.error('Error deleting flashcard:', error)
      }
    }
    
    return {
      deleteFlashcard
    }
  }
}
</script>
