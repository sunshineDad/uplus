<template>
  <div class="chat-interface">
    <div class="chat-header">
      <div class="chat-title">
        <div class="chat-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M12 16v-4"></path>
            <path d="M12 8h.01"></path>
          </svg>
        </div>
        <div class="chat-info">
          <h3>AI Product Manager</h3>
          <div class="chat-status" :class="{ 'status-active': sessionActive }">
            {{ sessionActive ? 'Active Session' : 'No Active Session' }}
          </div>
        </div>
      </div>
      <div class="chat-actions">
        <div class="completeness-indicator" v-if="sessionActive">
          <div class="completeness-label">Completeness:</div>
          <div class="completeness-progress">
            <div class="progress-bar" :style="{ width: `${completenessScore}%` }"></div>
            <div class="progress-text">{{ completenessScore }}%</div>
          </div>
        </div>
        <button 
          class="btn btn-primary" 
          v-if="sessionActive && isSessionComplete" 
          @click="generateRsd"
          :disabled="generatingRsd"
        >
          {{ generatingRsd ? 'Generating...' : 'Generate RSD' }}
        </button>
      </div>
    </div>
    
    <div class="chat-messages" ref="messagesContainer">
      <div v-if="!sessionActive" class="chat-empty-state">
        <div class="empty-state-icon">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
        </div>
        <h3>No Active Session</h3>
        <p>Start a new session to interact with the AI Product Manager.</p>
        <button class="btn btn-primary" @click="$emit('create-session')">Start New Session</button>
      </div>
      
      <template v-else>
        <div 
          v-for="(message, index) in messages" 
          :key="index" 
          class="chat-message" 
          :class="{ 
            'message-user': message.role === 'user',
            'message-assistant': message.role === 'assistant'
          }"
        >
          <div class="message-avatar">
            <div v-if="message.role === 'user'" class="avatar-user">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <div v-else class="avatar-assistant">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="3" y1="9" x2="21" y2="9"></line>
                <line x1="9" y1="21" x2="9" y2="9"></line>
              </svg>
            </div>
          </div>
          <div class="message-content">
            <div class="message-text" v-html="formatMessage(message.content)"></div>
            <div class="message-time">{{ formatTime(message.timestamp) }}</div>
          </div>
        </div>
        
        <div v-if="interacting" class="chat-message message-assistant">
          <div class="message-avatar">
            <div class="avatar-assistant">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="3" y1="9" x2="21" y2="9"></line>
                <line x1="9" y1="21" x2="9" y2="9"></line>
              </svg>
            </div>
          </div>
          <div class="message-content">
            <div class="message-typing">
              <span class="typing-dot"></span>
              <span class="typing-dot"></span>
              <span class="typing-dot"></span>
            </div>
          </div>
        </div>
      </template>
    </div>
    
    <div class="chat-input" v-if="sessionActive">
      <textarea 
        class="input-field" 
        placeholder="Type your message here..." 
        v-model="inputMessage"
        @keydown.enter.prevent="sendMessage"
        :disabled="interacting"
        ref="inputField"
      ></textarea>
      <button 
        class="send-button" 
        @click="sendMessage" 
        :disabled="!inputMessage.trim() || interacting"
      >
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="22" y1="2" x2="11" y2="13"></line>
          <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, nextTick } from 'vue';
import { useSessionStore } from '@/store/sessionStore';
import { useUiStore } from '@/store/uiStore';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

export default {
  name: 'ChatInterface',
  emits: ['create-session'],
  setup(props, { emit }) {
    const sessionStore = useSessionStore();
    const uiStore = useUiStore();
    
    const inputMessage = ref('');
    const messagesContainer = ref(null);
    const inputField = ref(null);
    const generatingRsd = ref(false);
    
    // Computed properties
    const sessionActive = computed(() => !!sessionStore.currentSession);
    const messages = computed(() => sessionStore.dialogueHistory);
    const interacting = computed(() => sessionStore.interacting);
    const completenessScore = computed(() => Math.round(sessionStore.completenessScore));
    const isSessionComplete = computed(() => sessionStore.isSessionComplete);
    
    // Methods
    const sendMessage = async () => {
      if (!inputMessage.value.trim() || interacting.value) return;
      
      try {
        await sessionStore.interactWithAiPm(inputMessage.value.trim());
        inputMessage.value = '';
        
        // Focus input field after sending
        nextTick(() => {
          if (inputField.value) {
            inputField.value.focus();
          }
        });
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'Error',
          message: error.message || 'Failed to send message'
        });
      }
    };
    
    const generateRsd = async () => {
      if (!sessionActive.value || !isSessionComplete.value || generatingRsd.value) return;
      
      generatingRsd.value = true;
      
      try {
        const rsd = await sessionStore.generateRsd();
        
        uiStore.addNotification({
          type: 'success',
          title: 'RSD Generated',
          message: 'Requirements Specification Document has been successfully generated'
        });
        
        // Emit event to parent component to handle RSD generation
        emit('rsd-generated', rsd);
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'Error',
          message: error.message || 'Failed to generate RSD'
        });
      } finally {
        generatingRsd.value = false;
      }
    };
    
    const formatMessage = (content) => {
      // Convert markdown to HTML and sanitize
      return DOMPurify.sanitize(marked.parse(content));
    };
    
    const formatTime = (timestamp) => {
      if (!timestamp) return '';
      
      const date = new Date(timestamp);
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    };
    
    // Scroll to bottom when new messages arrive
    watch(messages, () => {
      nextTick(() => {
        if (messagesContainer.value) {
          messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
        }
      });
    }, { deep: true });
    
    // Scroll to bottom when interacting changes
    watch(interacting, () => {
      nextTick(() => {
        if (messagesContainer.value) {
          messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
        }
      });
    });
    
    return {
      inputMessage,
      messagesContainer,
      inputField,
      sessionActive,
      messages,
      interacting,
      completenessScore,
      isSessionComplete,
      generatingRsd,
      sendMessage,
      generateRsd,
      formatMessage,
      formatTime
    };
  }
};
</script>

<style scoped>
.chat-interface {
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  background-color: var(--gray-100);
  border-bottom: 1px solid var(--gray-200);
}

.chat-title {
  display: flex;
  align-items: center;
}

.chat-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  margin-right: 1rem;
  background-color: var(--primary);
  color: var(--white);
  border-radius: var(--border-radius-circle);
}

.chat-icon svg {
  width: 24px;
  height: 24px;
}

.chat-info h3 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--gray-800);
}

.chat-status {
  font-size: 0.875rem;
  color: var(--gray-500);
}

.status-active {
  color: var(--success);
}

.chat-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.completeness-indicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.completeness-label {
  font-size: 0.875rem;
  color: var(--gray-700);
}

.completeness-progress {
  position: relative;
  width: 150px;
  height: 8px;
  background-color: var(--gray-200);
  border-radius: var(--border-radius-pill);
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background-color: var(--primary);
  border-radius: var(--border-radius-pill);
  transition: width 0.3s ease;
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--gray-700);
}

.chat-messages {
  flex: 1;
  padding: 1.5rem;
  overflow-y: auto;
  background-color: var(--gray-100);
}

.chat-empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 2rem;
  text-align: center;
}

.empty-state-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  margin-bottom: 1.5rem;
  background-color: var(--gray-200);
  color: var(--gray-600);
  border-radius: var(--border-radius-circle);
}

.empty-state-icon svg {
  width: 40px;
  height: 40px;
}

.chat-empty-state h3 {
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
  color: var(--gray-800);
}

.chat-empty-state p {
  margin-bottom: 1.5rem;
  color: var(--gray-600);
}

.chat-message {
  display: flex;
  margin-bottom: 1.5rem;
}

.message-user {
  flex-direction: row-reverse;
}

.message-avatar {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  margin: 0 1rem;
}

.avatar-user, .avatar-assistant {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  border-radius: var(--border-radius-circle);
  color: var(--white);
}

.avatar-user {
  background-color: var(--secondary);
}

.avatar-assistant {
  background-color: var(--primary);
}

.avatar-user svg, .avatar-assistant svg {
  width: 24px;
  height: 24px;
}

.message-content {
  max-width: 70%;
  padding: 1rem;
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-sm);
}

.message-user .message-content {
  background-color: var(--secondary-light);
  color: var(--white);
  border-top-right-radius: 0;
}

.message-assistant .message-content {
  background-color: var(--white);
  color: var(--gray-800);
  border-top-left-radius: 0;
}

.message-text {
  font-size: 1rem;
  line-height: 1.5;
}

.message-text :deep(p) {
  margin-bottom: 0.75rem;
}

.message-text :deep(p:last-child) {
  margin-bottom: 0;
}

.message-text :deep(ul), .message-text :deep(ol) {
  margin-bottom: 0.75rem;
  padding-left: 1.5rem;
}

.message-text :deep(pre) {
  margin-bottom: 0.75rem;
  padding: 0.75rem;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: var(--border-radius-sm);
  overflow-x: auto;
}

.message-user .message-text :deep(pre) {
  background-color: rgba(0, 0, 0, 0.1);
}

.message-text :deep(code) {
  font-family: var(--font-family-mono);
  font-size: 0.875em;
  padding: 0.2em 0.4em;
  background-color: rgba(0, 0, 0, 0.05);
  border-radius: var(--border-radius-sm);
}

.message-user .message-text :deep(code) {
  background-color: rgba(0, 0, 0, 0.1);
}

.message-time {
  margin-top: 0.5rem;
  font-size: 0.75rem;
  text-align: right;
  opacity: 0.7;
}

.message-typing {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.5rem;
}

.typing-dot {
  width: 8px;
  height: 8px;
  background-color: var(--gray-500);
  border-radius: var(--border-radius-circle);
  animation: typing-animation 1.5s infinite ease-in-out;
}

.typing-dot:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing-animation {
  0%, 60%, 100% {
    transform: translateY(0);
  }
  30% {
    transform: translateY(-6px);
  }
}

.chat-input {
  display: flex;
  align-items: center;
  padding: 1rem 1.5rem;
  background-color: var(--white);
  border-top: 1px solid var(--gray-200);
}

.input-field {
  flex: 1;
  height: 60px;
  padding: 1rem;
  font-size: 1rem;
  color: var(--gray-800);
  background-color: var(--gray-100);
  border: 1px solid var(--gray-300);
  border-radius: var(--border-radius-lg);
  resize: none;
  transition: all var(--transition-normal) var(--transition-timing);
}

.input-field:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.2);
}

.input-field::placeholder {
  color: var(--gray-500);
}

.send-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  margin-left: 1rem;
  background-color: var(--primary);
  color: var(--white);
  border: none;
  border-radius: var(--border-radius-circle);
  cursor: pointer;
  transition: all var(--transition-normal) var(--transition-timing);
}

.send-button:hover {
  background-color: var(--primary-dark);
}

.send-button:disabled {
  background-color: var(--gray-300);
  cursor: not-allowed;
}

.send-button svg {
  width: 24px;
  height: 24px;
}

/* Dark mode adjustments */
:global(.dark-mode) .chat-interface {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .chat-header {
  background-color: var(--dark-purple);
  border-bottom: 1px solid var(--gray-800);
}

:global(.dark-mode) .chat-info h3 {
  color: var(--white);
}

:global(.dark-mode) .chat-status {
  color: var(--gray-400);
}

:global(.dark-mode) .completeness-label {
  color: var(--gray-300);
}

:global(.dark-mode) .completeness-progress {
  background-color: var(--gray-800);
}

:global(.dark-mode) .progress-text {
  color: var(--gray-300);
}

:global(.dark-mode) .chat-messages {
  background-color: var(--dark);
}

:global(.dark-mode) .empty-state-icon {
  background-color: var(--gray-800);
  color: var(--gray-400);
}

:global(.dark-mode) .chat-empty-state h3 {
  color: var(--white);
}

:global(.dark-mode) .chat-empty-state p {
  color: var(--gray-400);
}

:global(.dark-mode) .message-assistant .message-content {
  background-color: var(--dark-blue);
  color: var(--gray-200);
}

:global(.dark-mode) .message-text :deep(pre) {
  background-color: rgba(255, 255, 255, 0.05);
}

:global(.dark-mode) .message-user .message-text :deep(pre) {
  background-color: rgba(255, 255, 255, 0.1);
}

:global(.dark-mode) .message-text :deep(code) {
  background-color: rgba(255, 255, 255, 0.05);
}

:global(.dark-mode) .message-user .message-text :deep(code) {
  background-color: rgba(255, 255, 255, 0.1);
}

:global(.dark-mode) .chat-input {
  background-color: var(--dark-blue);
  border-top: 1px solid var(--gray-800);
}

:global(.dark-mode) .input-field {
  color: var(--gray-200);
  background-color: var(--dark-purple);
  border: 1px solid var(--gray-700);
}

:global(.dark-mode) .input-field::placeholder {
  color: var(--gray-500);
}

@media (max-width: 768px) {
  .chat-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .chat-actions {
    margin-top: 1rem;
    width: 100%;
  }
  
  .completeness-indicator {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .completeness-progress {
    width: 100%;
  }
  
  .message-content {
    max-width: 80%;
  }
}
</style>