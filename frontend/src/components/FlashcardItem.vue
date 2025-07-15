<template>
  <div class="flashcard">
    <button
      @click="deleteFlashcard"
      class="btn btn-danger"
      title="Delete flashcard"
    >
      ×
    </button>
    
    <div v-if="flashcard.tag" class="tag">
      {{ flashcard.tag }}
    </div>
    
    <div 
      class="flashcard-content"
      :class="{ flipped: isFlipped }"
      @click="toggleFlip"
    >
      <div v-if="!isFlipped">
        <h3 class="flashcard-title">Question</h3>
        <p class="flashcard-text">{{ flashcard.question }}</p>
      </div>
      
      <div v-else>
        <h3 class="flashcard-title">Answer</h3>
        <p class="flashcard-text">{{ flashcard.answer }}</p>
      </div>
    </div>
    
    <div class="text-center">
      <button
        @click="toggleFlip"
        class="btn btn-secondary"
      >
        {{ isFlipped ? 'Show Question' : 'Show Answer' }}
      </button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'FlashcardItem',
  props: {
    flashcard: {
      type: Object,
      required: true
    }
  },
  emits: ['delete-flashcard'],
  setup(props, { emit }) {
    const isFlipped = ref(false)
    
    const toggleFlip = () => {
      isFlipped.value = !isFlipped.value
    }
    
    const deleteFlashcard = () => {
      if (confirm('Are you sure you want to delete this flashcard?')) {
        emit('delete-flashcard', props.flashcard.id)
      }
    }
    
    return {
      isFlipped,
      toggleFlip,
      deleteFlashcard
    }
  }
}
</script>
