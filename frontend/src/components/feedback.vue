<template>
  <div>
    <button @click="showFeedbackForm">Give Feedback</button>
    
    <div v-if="showForm" class="feedback-popup">
      <h1>Feedback Form</h1>
      <h2>How would you rate your satisfaction with our product?</h2>
      <div id="rating">
        <div
          v-for="star in 5"
          :key="star"
          @mouseover="hoverRating(star)"
          @mouseleave="hoverRating(0)"
          @click="submitFeedback(star)"
          :class="{'active': star <= currentRating, 'hovered': star <= hoverRatingValue}"
          class="star"
        >
          ☆
          <span class="number">{{ star }}</span>
        </div>
      </div>
      <div id="feedback-text">
        <span class="feedback-left">Very Dissatisfied</span>
        <span class="feedback-right">Very Satisfied</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showForm: false,
      currentRating: 0,
      hoverRatingValue: 0,
    };
  },
  methods: {
    async submitFeedback(score) {
      this.currentRating = score;
      try {
        const response = await fetch('http://127.0.0.1:8000/feedback/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ score })
        });
        if (response.ok) {
          const data = await response.json();
          alert('Feedback submitted: ' + data.score);
          this.showForm = false; // Hide the form after submission
        } else {
          alert('Failed to submit feedback');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while submitting feedback');
      }
    },
    hoverRating(value) {
      this.hoverRatingValue = value;
    },
    showFeedbackForm() {
      this.showForm = true;
    }
  }
}
</script>

<style>
.feedback-popup {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000; /* Ensure it's above other content */
  width: 300px;
}

#rating {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.star {
  position: relative;
  cursor: pointer;
  font-size: 5em;
  color: lightgray;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.star::before {
  content: '★';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  color: gold;
  opacity: 0;
}

.star.active::before,
.star.hovered::before {
  opacity: 1;
}

#feedback-text {
  display: flex;
  justify-content: space-between;
  width: 100%;
  max-width: 350px;
  margin: 40px auto 0;
  padding: 0 20px;
}

.feedback-left,
.feedback-right {
  font-size: 1em;
  color: gray;
}

.number {
  font-size: 0.5em;
  margin-top: 5px;
}
</style>
