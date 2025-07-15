<template>
  <div class="container">
    <h1 class="title">Flashcard App</h1>
    
    <FlashcardForm @flashcard-created="loadFlashcards" />
    <FlashcardList :flashcards="flashcards" @flashcard-deleted="loadFlashcards" />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import FlashcardForm from './components/FlashcardForm.vue'
import FlashcardList from './components/FlashcardList.vue'

export default {
  name: 'App',
  components: {
    FlashcardForm,
    FlashcardList
  },
  setup() {
    const flashcards = ref([])
    
    const loadFlashcards = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/flashcards/')
        if (response.ok) {
          const data = await response.json()
          flashcards.value = data
        } else {
          console.error('Failed to load flashcards, status:', response.status)
        }
      } catch (error) {
        console.error('Error loading flashcards:', error)
      }
    }
    
    onMounted(() => {
      loadFlashcards()
    })
    
    return {
      flashcards,
      loadFlashcards
    }
  }
}
</script>
