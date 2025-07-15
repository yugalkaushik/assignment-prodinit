<template>
  <div class="card">
    <h2 class="section-title">Create New Flashcard</h2>
    <form @submit.prevent="createFlashcard">
      <div class="form-group">
        <label for="question" class="form-label">Question</label>
        <textarea
          id="question"
          v-model="form.question"
          class="form-textarea"
          rows="3"
          placeholder="Enter your question..."
          required
        ></textarea>
      </div>
      
      <div class="form-group">
        <label for="answer" class="form-label">Answer</label>
        <textarea
          id="answer"
          v-model="form.answer"
          class="form-textarea"
          rows="3"
          placeholder="Enter the answer..."
          required
        ></textarea>
      </div>
      
      <div class="form-group">
        <label for="tag" class="form-label">Tag (Optional)</label>
        <input
          id="tag"
          v-model="form.tag"
          type="text"
          class="form-input"
          placeholder="e.g., Math, Science, History..."
        />
      </div>
      
      <button
        type="submit"
        :disabled="isSubmitting"
        class="btn btn-primary"
        style="width: 100%;"
      >
        {{ isSubmitting ? 'Creating...' : 'Create Flashcard' }}
      </button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'FlashcardForm',
  emits: ['flashcard-created'],
  setup(props, { emit }) {
    const form = ref({
      question: '',
      answer: '',
      tag: ''
    })
    
    const isSubmitting = ref(false)
    
    const createFlashcard = async () => {
      if (!form.value.question.trim() || !form.value.answer.trim()) {
        alert('Please fill in both question and answer fields')
        return
      }
      
      isSubmitting.value = true
      
      try {
        const response = await fetch('http://localhost:8000/api/flashcards/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(form.value)
        })
        
        if (response.ok) {
          const result = await response.json()
          form.value = { question: '', answer: '', tag: '' }
          emit('flashcard-created')
        } else {
          console.error('Failed to create flashcard, status:', response.status)
        }
      } catch (error) {
        console.error('Error creating flashcard:', error)
      } finally {
        isSubmitting.value = false
      }
    }
    
    return {
      form,
      isSubmitting,
      createFlashcard
    }
  }
}
</script>
