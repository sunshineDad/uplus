<template>
  <div class="chat-interface">
    <!-- Revolutionary AI-PM Header -->
    <div class="chat-header">
      <div class="header-background">
        <div class="header-gradient"></div>
        <div class="header-particles">
          <div v-for="i in 20" :key="i" class="particle" :style="getParticleStyle(i)"></div>
        </div>
      </div>
      
      <div class="header-content">
        <div class="ai-avatar">
          <div class="avatar-core">
            <div class="avatar-ring"></div>
            <div class="avatar-pulse"></div>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 2L2 7l10 5 10-5-10-5z"/>
              <path d="M2 17l10 5 10-5"/>
              <path d="M2 12l10 5 10-5"/>
            </svg>
          </div>
          <div class="avatar-status" :class="{ active: sessionActive }">
            <div class="status-dot"></div>
          </div>
        </div>
        
        <div class="ai-info">
          <h2 class="ai-title">
            <span class="title-gradient">AI Product Manager</span>
            <div class="title-subtitle">Socratic Intelligence Engine</div>
          </h2>
          <div class="ai-capabilities">
            <div class="capability-tag">Multi-modal Understanding</div>
            <div class="capability-tag">Intent Analysis</div>
            <div class="capability-tag">Requirement Discovery</div>
          </div>
        </div>
        
        <div class="session-metrics" v-if="sessionActive">
          <div class="metric-card">
            <div class="metric-label">Completeness</div>
            <div class="metric-value">
              <div class="circular-progress">
                <svg class="progress-ring" width="60" height="60">
                  <circle
                    class="progress-ring-circle"
                    stroke="var(--primary-400)"
                    stroke-width="4"
                    fill="transparent"
                    r="26"
                    cx="30"
                    cy="30"
                    :stroke-dasharray="circumference"
                    :stroke-dashoffset="progressOffset"
                  />
                </svg>
                <div class="progress-text">{{ completenessScore }}%</div>
              </div>
            </div>
          </div>
          
          <div class="metric-card">
            <div class="metric-label">Interactions</div>
            <div class="metric-value">{{ messages.length }}</div>
          </div>
          
          <div class="metric-card">
            <div class="metric-label">Quality</div>
            <div class="metric-value">
              <div class="quality-indicator" :class="qualityLevel">
                {{ qualityScore }}
              </div>
            </div>
          </div>
        </div>
        
        <div class="header-actions">
          <button 
            v-if="sessionActive && isSessionComplete" 
            class="btn btn-primary btn-glow"
            @click="generateRsd"
            :disabled="generatingRsd"
          >
            <svg v-if="!generatingRsd" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
              <polyline points="14,2 14,8 20,8"/>
              <line x1="16" y1="13" x2="8" y2="13"/>
              <line x1="16" y1="17" x2="8" y2="17"/>
              <polyline points="10,9 9,9 8,9"/>
            </svg>
            <div v-else class="loading-spinner"></div>
            {{ generatingRsd ? 'Materializing RSD...' : 'Generate RSD' }}
          </button>
          
          <button 
            v-if="!sessionActive" 
            class="btn btn-primary btn-glow"
            @click="$emit('create-session')"
          >
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
            Start AI Session
          </button>
        </div>
      </div>
    </div>
    
    <!-- Revolutionary Chat Messages Area -->
    <div class="chat-messages" ref="messagesContainer">
      <div v-if="!sessionActive" class="chat-empty-state">
        <div class="empty-state-visual">
          <div class="neural-network-mini">
            <div v-for="i in 12" :key="i" class="mini-node" :style="getMiniNodeStyle(i)"></div>
            <svg class="mini-connections" viewBox="0 0 200 200">
              <path d="M50,50 Q100,25 150,50" stroke="var(--primary-400)" stroke-width="1" fill="none" opacity="0.3"/>
              <path d="M50,100 Q100,75 150,100" stroke="var(--secondary-400)" stroke-width="1" fill="none" opacity="0.3"/>
              <path d="M50,150 Q100,125 150,150" stroke="var(--accent-400)" stroke-width="1" fill="none" opacity="0.3"/>
            </svg>
          </div>
          <h3 class="empty-title">AI Product Manager Ready</h3>
          <p class="empty-description">
            Initiate a conversation to begin the revolutionary requirement discovery process.
            Our Socratic Intelligence will guide you through comprehensive specification development.
          </p>
          <div class="empty-features">
            <div class="feature-item">
              <div class="feature-icon">🧠</div>
              <span>Multi-modal Understanding</span>
            </div>
            <div class="feature-item">
              <div class="feature-icon">🎯</div>
              <span>Intent Analysis</span>
            </div>
            <div class="feature-item">
              <div class="feature-icon">📋</div>
              <span>RSD Generation</span>
            </div>
          </div>
        </div>
      </div>
      
      <template v-else>
        <!-- Welcome Message -->
        <div v-if="messages.length === 0" class="welcome-message">
          <div class="welcome-avatar">
            <div class="avatar-glow"></div>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M12 2L2 7l10 5 10-5-10-5z"/>
              <path d="M2 17l10 5 10-5"/>
              <path d="M2 12l10 5 10-5"/>
            </svg>
          </div>
          <div class="welcome-content">
            <h4>Welcome to AI Product Manager</h4>
            <p>I'm here to help you transform your vision into precise, executable specifications. Let's begin by understanding what you want to build.</p>
            <div class="suggested-starters">
              <button 
                v-for="starter in suggestedStarters" 
                :key="starter"
                class="starter-button"
                @click="sendSuggestedMessage(starter)"
              >
                {{ starter }}
              </button>
            </div>
          </div>
        </div>
        
        <!-- Chat Messages -->
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
              <div class="avatar-background"></div>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                <circle cx="12" cy="7" r="4"/>
              </svg>
            </div>
            <div v-else class="avatar-assistant">
              <div class="avatar-background"></div>
              <div class="avatar-pulse-ring"></div>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
            </div>
          </div>
          
          <div class="message-content">
            <div class="message-bubble">
              <div class="bubble-background"></div>
              <div class="message-text" v-html="formatMessage(message.content)"></div>
              <div class="message-metadata">
                <div class="message-time">{{ formatTime(message.timestamp) }}</div>
                <div v-if="message.role === 'assistant' && message.intent_analysis" class="intent-indicator">
                  <div class="intent-type">{{ formatIntentType(message.intent_analysis.intent_type) }}</div>
                  <div class="confidence-score">{{ Math.round(message.intent_analysis.confidence * 100) }}%</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- AI Thinking Animation -->
        <div v-if="interacting" class="chat-message message-assistant thinking">
          <div class="message-avatar">
            <div class="avatar-assistant">
              <div class="avatar-background"></div>
              <div class="thinking-animation">
                <div class="thinking-ring"></div>
                <div class="thinking-dots">
                  <div class="dot"></div>
                  <div class="dot"></div>
                  <div class="dot"></div>
                </div>
              </div>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 2L2 7l10 5 10-5-10-5z"/>
                <path d="M2 17l10 5 10-5"/>
                <path d="M2 12l10 5 10-5"/>
              </svg>
            </div>
          </div>
          
          <div class="message-content">
            <div class="message-bubble thinking-bubble">
              <div class="bubble-background"></div>
              <div class="thinking-text">
                <div class="thinking-process">
                  <div class="process-step active">Analyzing intent...</div>
                  <div class="process-step">Generating response...</div>
                  <div class="process-step">Optimizing questions...</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </div>
    
    <!-- Revolutionary Input Interface -->
    <div class="chat-input" v-if="sessionActive">
      <div class="input-container">
        <div class="input-background">
          <div class="input-gradient"></div>
        </div>
        
        <div class="input-content">
          <div class="input-field-container">
            <textarea 
              class="input-field" 
              placeholder="Describe your vision, requirements, or ask questions..." 
              v-model="inputMessage"
              @keydown.enter.prevent="handleEnterKey"
              @input="handleInput"
              :disabled="interacting"
              ref="inputField"
              rows="1"
            ></textarea>
            <div class="input-enhancements">
              <div class="character-count" :class="{ warning: inputMessage.length > 500 }">
                {{ inputMessage.length }}/1000
              </div>
              <div class="input-suggestions" v-if="showSuggestions">
                <button 
                  v-for="suggestion in inputSuggestions" 
                  :key="suggestion"
                  class="suggestion-chip"
                  @click="applySuggestion(suggestion)"
                >
                  {{ suggestion }}
                </button>
              </div>
            </div>
          </div>
          
          <div class="input-actions">
            <button 
              class="action-button voice-button"
              :class="{ active: isRecording }"
              @click="toggleVoiceInput"
              title="Voice Input"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                <line x1="12" y1="19" x2="12" y2="23"/>
                <line x1="8" y1="23" x2="16" y2="23"/>
              </svg>
            </button>
            
            <button 
              class="action-button attachment-button"
              @click="handleAttachment"
              title="Attach File"
            >
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"/>
              </svg>
            </button>
            
            <button 
              class="send-button" 
              @click="sendMessage" 
              :disabled="!canSendMessage"
              :class="{ pulse: canSendMessage }"
            >
              <div class="button-background"></div>
              <svg v-if="!interacting" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="22" y1="2" x2="11" y2="13"/>
                <polygon points="22 2 15 22 11 13 2 9 22 2"/>
              </svg>
              <div v-else class="sending-animation">
                <div class="spinner"></div>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, nextTick, onMounted } from 'vue';
import { useSessionStore } from '@/store/sessionStore';
import { useUiStore } from '@/store/uiStore';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

export default {
  name: 'ChatInterface',
  emits: ['create-session', 'rsd-generated'],
  setup(props, { emit }) {
    const sessionStore = useSessionStore();
    const uiStore = useUiStore();
    
    const inputMessage = ref('');
    const messagesContainer = ref(null);
    const inputField = ref(null);
    const generatingRsd = ref(false);
    const isRecording = ref(false);
    const showSuggestions = ref(false);
    
    // Enhanced computed properties
    const sessionActive = computed(() => !!sessionStore.currentSession);
    const messages = computed(() => sessionStore.dialogueHistory);
    const interacting = computed(() => sessionStore.interacting);
    const completenessScore = computed(() => Math.round(sessionStore.completenessScore * 100));
    const isSessionComplete = computed(() => sessionStore.isSessionComplete);
    
    // New computed properties for premium features
    const circumference = computed(() => 2 * Math.PI * 26);
    const progressOffset = computed(() => {
      const progress = completenessScore.value / 100;
      return circumference.value - (progress * circumference.value);
    });
    
    const qualityScore = computed(() => {
      const messageCount = messages.value.length;
      const completeness = completenessScore.value / 100;
      return Math.round((messageCount * 0.3 + completeness * 0.7) * 100);
    });
    
    const qualityLevel = computed(() => {
      const score = qualityScore.value;
      if (score >= 80) return 'excellent';
      if (score >= 60) return 'good';
      if (score >= 40) return 'fair';
      return 'poor';
    });
    
    const canSendMessage = computed(() => {
      return inputMessage.value.trim().length > 0 && !interacting.value;
    });
    
    // Suggested starters for new sessions
    const suggestedStarters = ref([
      "I want to build a web application for...",
      "I need a mobile app that helps users...",
      "I'm looking to create a system for...",
      "I have an idea for a platform that..."
    ]);
    
    const inputSuggestions = ref([
      "user management",
      "real-time collaboration", 
      "data analytics",
      "mobile-first design",
      "API integration"
    ]);
    
    // Enhanced methods
    const sendMessage = async () => {
      if (!canSendMessage.value) return;
      
      try {
        await sessionStore.interactWithAiPm(inputMessage.value.trim());
        inputMessage.value = '';
        showSuggestions.value = false;
        
        // Auto-resize textarea
        if (inputField.value) {
          inputField.value.style.height = 'auto';
          inputField.value.focus();
        }
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'Communication Error',
          message: error.message || 'Failed to send message to AI Product Manager'
        });
      }
    };
    
    const sendSuggestedMessage = async (message) => {
      inputMessage.value = message;
      await sendMessage();
    };
    
    const handleEnterKey = (event) => {
      if (event.shiftKey) {
        // Allow new line with Shift+Enter
        return;
      }
      event.preventDefault();
      sendMessage();
    };
    
    const handleInput = () => {
      // Auto-resize textarea
      if (inputField.value) {
        inputField.value.style.height = 'auto';
        inputField.value.style.height = Math.min(inputField.value.scrollHeight, 120) + 'px';
      }
      
      // Show suggestions for certain keywords
      const keywords = ['user', 'system', 'feature', 'data', 'mobile'];
      showSuggestions.value = keywords.some(keyword => 
        inputMessage.value.toLowerCase().includes(keyword)
      );
    };
    
    const applySuggestion = (suggestion) => {
      inputMessage.value += (inputMessage.value ? ' ' : '') + suggestion;
      showSuggestions.value = false;
      if (inputField.value) {
        inputField.value.focus();
      }
    };
    
    const toggleVoiceInput = () => {
      if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        uiStore.addNotification({
          type: 'warning',
          title: 'Voice Input Unavailable',
          message: 'Speech recognition is not supported in this browser'
        });
        return;
      }
      
      isRecording.value = !isRecording.value;
      
      if (isRecording.value) {
        startVoiceRecognition();
      } else {
        stopVoiceRecognition();
      }
    };
    
    const handleAttachment = () => {
      // Create file input
      const fileInput = document.createElement('input');
      fileInput.type = 'file';
      fileInput.accept = '.txt,.md,.pdf,.doc,.docx,image/*';
      fileInput.onchange = (event) => {
        const file = event.target.files[0];
        if (file) {
          processAttachment(file);
        }
      };
      fileInput.click();
    };
    
    const processAttachment = (file) => {
      uiStore.addNotification({
        type: 'info',
        title: 'File Processing',
        message: `Processing ${file.name}... (Feature coming soon)`
      });
    };
    
    let speechRecognition = null;
    
    const startVoiceRecognition = () => {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      speechRecognition = new SpeechRecognition();
      
      speechRecognition.continuous = true;
      speechRecognition.interimResults = true;
      speechRecognition.lang = 'en-US';
      
      speechRecognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; i++) {
          transcript += event.results[i][0].transcript;
        }
        inputMessage.value = transcript;
      };
      
      speechRecognition.onerror = () => {
        isRecording.value = false;
        uiStore.addNotification({
          type: 'error',
          title: 'Voice Recognition Error',
          message: 'Failed to recognize speech. Please try again.'
        });
      };
      
      speechRecognition.onend = () => {
        isRecording.value = false;
      };
      
      speechRecognition.start();
    };
    
    const stopVoiceRecognition = () => {
      if (speechRecognition) {
        speechRecognition.stop();
      }
    };
    
    const generateRsd = async () => {
      if (!sessionActive.value || !isSessionComplete.value || generatingRsd.value) return;
      
      generatingRsd.value = true;
      
      try {
        const rsd = await sessionStore.generateRsd();
        
        uiStore.addNotification({
          type: 'success',
          title: 'RSD Successfully Generated',
          message: 'Requirements Specification Document has been materialized from your conversation'
        });
        
        emit('rsd-generated', rsd);
      } catch (error) {
        uiStore.addNotification({
          type: 'error',
          title: 'RSD Generation Failed',
          message: error.message || 'Failed to generate Requirements Specification Document'
        });
      } finally {
        generatingRsd.value = false;
      }
    };
    
    const formatMessage = (content) => {
      if (!content) return '';
      
      // Enhanced markdown parsing with custom renderers
      const renderer = new marked.Renderer();
      
      // Custom list rendering
      renderer.list = (body, ordered) => {
        const type = ordered ? 'ol' : 'ul';
        return `<${type} class="message-list">${body}</${type}>`;
      };
      
      // Custom code rendering
      renderer.code = (code, language) => {
        return `<pre class="message-code"><code class="language-${language || 'text'}">${code}</code></pre>`;
      };
      
      marked.setOptions({ renderer });
      
      return DOMPurify.sanitize(marked.parse(content));
    };
    
    const formatTime = (timestamp) => {
      if (!timestamp) return '';
      
      const date = new Date(timestamp);
      const now = new Date();
      const diffMs = now - date;
      const diffMins = Math.floor(diffMs / 60000);
      
      if (diffMins < 1) return 'Just now';
      if (diffMins < 60) return `${diffMins}m ago`;
      
      return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    };
    
    const formatIntentType = (intentType) => {
      return intentType.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    };
    
    // Animation helpers
    const getParticleStyle = (index) => {
      const angle = (index / 20) * 360;
      const radius = 30 + (index % 3) * 10;
      const x = Math.cos(angle * Math.PI / 180) * radius;
      const y = Math.sin(angle * Math.PI / 180) * radius;
      
      return {
        left: `calc(50% + ${x}px)`,
        top: `calc(50% + ${y}px)`,
        animationDelay: `${index * 0.1}s`,
        animationDuration: `${2 + (index % 3)}s`
      };
    };
    
    const getMiniNodeStyle = (index) => {
      const positions = [
        { x: 20, y: 30 }, { x: 60, y: 20 }, { x: 100, y: 40 },
        { x: 140, y: 25 }, { x: 180, y: 35 }, { x: 30, y: 80 },
        { x: 70, y: 90 }, { x: 110, y: 75 }, { x: 150, y: 85 },
        { x: 40, y: 130 }, { x: 80, y: 140 }, { x: 120, y: 125 }
      ];
      
      const pos = positions[index % positions.length];
      return {
        left: `${pos.x}px`,
        top: `${pos.y}px`,
        animationDelay: `${index * 0.2}s`
      };
    };
    
    // Scroll management
    const scrollToBottom = () => {
      nextTick(() => {
        if (messagesContainer.value) {
          messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight;
        }
      });
    };
    
    // Watchers
    watch(messages, scrollToBottom, { deep: true });
    watch(interacting, scrollToBottom);
    
    // Lifecycle
    onMounted(() => {
      if (inputField.value) {
        inputField.value.focus();
      }
    });
    
    return {
      // Refs
      inputMessage,
      messagesContainer,
      inputField,
      generatingRsd,
      isRecording,
      showSuggestions,
      
      // Computed
      sessionActive,
      messages,
      interacting,
      completenessScore,
      isSessionComplete,
      circumference,
      progressOffset,
      qualityScore,
      qualityLevel,
      canSendMessage,
      suggestedStarters,
      inputSuggestions,
      
      // Methods
      sendMessage,
      sendSuggestedMessage,
      handleEnterKey,
      handleInput,
      applySuggestion,
      toggleVoiceInput,
      handleAttachment,
      generateRsd,
      formatMessage,
      formatTime,
      formatIntentType,
      getParticleStyle,
      getMiniNodeStyle
    };
  }
};
</script>

<style scoped>
/* Revolutionary AI-PM Chat Interface */
.chat-interface {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--surface);
  border-radius: var(--radius-2xl);
  box-shadow: var(--shadow-2xl);
  overflow: hidden;
  position: relative;
  backdrop-filter: blur(20px);
  border: 1px solid var(--border);
}

/* Revolutionary Header */
.chat-header {
  position: relative;
  padding: var(--space-6);
  background: var(--surface-elevated);
  border-bottom: 1px solid var(--border);
  overflow: hidden;
}

.header-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
}

.header-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--gradient-primary);
  opacity: 0.1;
}

.header-particles {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: var(--primary-400);
  border-radius: 50%;
  opacity: 0.6;
  animation: particle-float 3s ease-in-out infinite;
}

@keyframes particle-float {
  0%, 100% { transform: translateY(0) scale(1); opacity: 0.6; }
  50% { transform: translateY(-10px) scale(1.2); opacity: 1; }
}

.header-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  gap: var(--space-6);
  flex-wrap: wrap;
}

/* AI Avatar */
.ai-avatar {
  position: relative;
  flex-shrink: 0;
}

.avatar-core {
  position: relative;
  width: 80px;
  height: 80px;
  background: var(--gradient-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-glow);
}

.avatar-ring {
  position: absolute;
  top: -8px;
  left: -8px;
  right: -8px;
  bottom: -8px;
  border: 2px solid var(--primary-400);
  border-radius: 50%;
  opacity: 0.3;
  animation: avatar-ring-pulse 3s ease-in-out infinite;
}

.avatar-pulse {
  position: absolute;
  top: -16px;
  left: -16px;
  right: -16px;
  bottom: -16px;
  border: 1px solid var(--primary-400);
  border-radius: 50%;
  opacity: 0.2;
  animation: avatar-pulse-expand 4s ease-in-out infinite;
}

@keyframes avatar-ring-pulse {
  0%, 100% { transform: scale(1); opacity: 0.3; }
  50% { transform: scale(1.1); opacity: 0.6; }
}

@keyframes avatar-pulse-expand {
  0% { transform: scale(1); opacity: 0.2; }
  50% { transform: scale(1.2); opacity: 0.1; }
  100% { transform: scale(1.4); opacity: 0; }
}

.avatar-core svg {
  width: 32px;
  height: 32px;
  color: white;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
}

.avatar-status {
  position: absolute;
  bottom: 8px;
  right: 8px;
  width: 20px;
  height: 20px;
  background: var(--surface);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid var(--surface-elevated);
}

.status-dot {
  width: 8px;
  height: 8px;
  background: var(--gray-400);
  border-radius: 50%;
  transition: all var(--transition-normal);
}

.avatar-status.active .status-dot {
  background: var(--success);
  box-shadow: 0 0 8px var(--success);
  animation: status-pulse 2s ease-in-out infinite;
}

@keyframes status-pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.2); }
}

/* AI Info */
.ai-info {
  flex: 1;
  min-width: 200px;
}

.ai-title {
  margin: 0 0 var(--space-2) 0;
}

.title-gradient {
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-size: var(--text-2xl);
  font-weight: 700;
  font-family: var(--font-display);
}

.title-subtitle {
  font-size: var(--text-sm);
  color: var(--text-muted);
  font-weight: 500;
  margin-top: var(--space-1);
}

.ai-capabilities {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
  margin-top: var(--space-3);
}

.capability-tag {
  padding: var(--space-1) var(--space-3);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  color: var(--text-secondary);
  font-weight: 500;
  transition: all var(--transition-fast);
}

.capability-tag:hover {
  background: var(--primary-400);
  color: white;
  transform: translateY(-1px);
}

/* Session Metrics */
.session-metrics {
  display: flex;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.metric-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--space-3);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  min-width: 80px;
  transition: all var(--transition-normal);
}

.metric-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.metric-label {
  font-size: var(--text-xs);
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: var(--space-2);
}

.metric-value {
  font-size: var(--text-lg);
  font-weight: 700;
  color: var(--text-primary);
}

/* Circular Progress */
.circular-progress {
  position: relative;
  width: 60px;
  height: 60px;
}

.progress-ring {
  transform: rotate(-90deg);
}

.progress-ring-circle {
  transition: stroke-dashoffset 0.5s ease;
  stroke-linecap: round;
}

.progress-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: var(--text-sm);
  font-weight: 700;
  color: var(--primary-400);
}

/* Quality Indicator */
.quality-indicator {
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.quality-indicator.excellent {
  background: var(--success-light);
  color: var(--success);
}

.quality-indicator.good {
  background: var(--info-light);
  color: var(--info);
}

.quality-indicator.fair {
  background: var(--warning-light);
  color: var(--warning);
}

.quality-indicator.poor {
  background: var(--error-light);
  color: var(--error);
}

/* Header Actions */
.header-actions {
  display: flex;
  gap: var(--space-3);
  align-items: center;
}

.btn-glow {
  position: relative;
  overflow: hidden;
}

.btn-glow::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  transition: left 0.5s;
}

.btn-glow:hover::before {
  left: 100%;
}

.btn-glow svg {
  width: 20px;
  height: 20px;
  margin-right: var(--space-2);
}

.loading-spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-right: var(--space-2);
}

/* Chat Messages */
.chat-messages {
  flex: 1;
  padding: var(--space-6);
  overflow-y: auto;
  background: var(--background);
  position: relative;
}

/* Empty State */
.chat-empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  padding: var(--space-8);
}

.empty-state-visual {
  position: relative;
  margin-bottom: var(--space-6);
}

.neural-network-mini {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto var(--space-6);
}

.mini-node {
  position: absolute;
  width: 8px;
  height: 8px;
  background: var(--primary-400);
  border-radius: 50%;
  animation: mini-node-pulse 2s ease-in-out infinite;
}

@keyframes mini-node-pulse {
  0%, 100% { opacity: 0.6; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.2); }
}

.mini-connections {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.empty-title {
  font-size: var(--text-3xl);
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: var(--space-4);
  background: var(--gradient-primary);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.empty-description {
  font-size: var(--text-lg);
  color: var(--text-secondary);
  line-height: 1.6;
  max-width: 500px;
  margin-bottom: var(--space-6);
}

.empty-features {
  display: flex;
  gap: var(--space-6);
  justify-content: center;
  flex-wrap: wrap;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-4);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  transition: all var(--transition-normal);
}

.feature-item:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-400);
}

.feature-icon {
  font-size: var(--text-2xl);
  margin-bottom: var(--space-2);
}

/* Welcome Message */
.welcome-message {
  display: flex;
  gap: var(--space-4);
  padding: var(--space-6);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  margin-bottom: var(--space-6);
  animation: fadeIn 0.6s ease-out;
}

.welcome-avatar {
  position: relative;
  width: 60px;
  height: 60px;
  background: var(--gradient-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.avatar-glow {
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  background: var(--gradient-primary);
  border-radius: 50%;
  opacity: 0.3;
  animation: avatar-glow-pulse 2s ease-in-out infinite;
}

@keyframes avatar-glow-pulse {
  0%, 100% { transform: scale(1); opacity: 0.3; }
  50% { transform: scale(1.1); opacity: 0.6; }
}

.welcome-avatar svg {
  width: 24px;
  height: 24px;
  color: white;
  z-index: 1;
  position: relative;
}

.welcome-content h4 {
  font-size: var(--text-xl);
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: var(--space-2);
}

.welcome-content p {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: var(--space-4);
}

.suggested-starters {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.starter-button {
  padding: var(--space-3) var(--space-4);
  background: var(--surface-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  color: var(--text-secondary);
  font-size: var(--text-sm);
  text-align: left;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.starter-button:hover {
  background: var(--primary-400);
  color: white;
  transform: translateX(4px);
  border-color: var(--primary-400);
}

/* Chat Messages */
.chat-message {
  display: flex;
  gap: var(--space-4);
  margin-bottom: var(--space-6);
  animation: fadeIn 0.4s ease-out;
}

.message-user {
  flex-direction: row-reverse;
}

.message-avatar {
  position: relative;
  width: 48px;
  height: 48px;
  flex-shrink: 0;
}

.avatar-user,
.avatar-assistant {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.avatar-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--gradient-secondary);
  z-index: 1;
}

.avatar-user .avatar-background {
  background: var(--gradient-accent);
}

.avatar-pulse-ring {
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  border: 2px solid var(--primary-400);
  border-radius: 50%;
  opacity: 0.3;
  animation: avatar-ring-pulse 3s ease-in-out infinite;
}

.avatar-user svg,
.avatar-assistant svg {
  width: 20px;
  height: 20px;
  color: white;
  z-index: 2;
  position: relative;
}

/* Message Content */
.message-content {
  flex: 1;
  max-width: 70%;
}

.message-bubble {
  position: relative;
  padding: var(--space-4) var(--space-5);
  border-radius: var(--radius-xl);
  overflow: hidden;
}

.bubble-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  z-index: 1;
}

.message-user .bubble-background {
  background: var(--gradient-primary);
  border: none;
}

.message-text {
  position: relative;
  z-index: 2;
  color: var(--text-primary);
  line-height: 1.6;
}

.message-user .message-text {
  color: white;
}

.message-metadata {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: var(--space-3);
  position: relative;
  z-index: 2;
}

.message-time {
  font-size: var(--text-xs);
  color: var(--text-muted);
  opacity: 0.7;
}

.message-user .message-time {
  color: rgba(255,255,255,0.8);
}

.intent-indicator {
  display: flex;
  gap: var(--space-2);
  align-items: center;
}

.intent-type {
  font-size: var(--text-xs);
  padding: var(--space-1) var(--space-2);
  background: var(--primary-400);
  color: white;
  border-radius: var(--radius-md);
  font-weight: 500;
}

.confidence-score {
  font-size: var(--text-xs);
  color: var(--text-muted);
  font-weight: 600;
}

/* Thinking Animation */
.thinking {
  opacity: 0.8;
}

.thinking-animation {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 3;
}

.thinking-ring {
  position: absolute;
  width: 60px;
  height: 60px;
  border: 2px solid var(--primary-400);
  border-top: 2px solid transparent;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.thinking-dots {
  display: flex;
  gap: var(--space-1);
}

.thinking-dots .dot {
  width: 4px;
  height: 4px;
  background: white;
  border-radius: 50%;
  animation: thinking-dot-bounce 1.4s ease-in-out infinite both;
}

.thinking-dots .dot:nth-child(1) { animation-delay: -0.32s; }
.thinking-dots .dot:nth-child(2) { animation-delay: -0.16s; }

@keyframes thinking-dot-bounce {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}

.thinking-bubble {
  background: var(--surface-elevated);
  border: 1px dashed var(--border);
}

.thinking-process {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.process-step {
  font-size: var(--text-sm);
  color: var(--text-muted);
  opacity: 0.5;
  transition: all var(--transition-fast);
}

.process-step.active {
  color: var(--primary-400);
  opacity: 1;
  font-weight: 600;
}

/* Revolutionary Input Interface */
.chat-input {
  position: relative;
  padding: var(--space-6);
  background: var(--surface-elevated);
  border-top: 1px solid var(--border);
}

.input-container {
  position: relative;
  border-radius: var(--radius-xl);
  overflow: hidden;
}

.input-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--surface);
  border: 1px solid var(--border);
  transition: all var(--transition-fast);
}

.input-container:focus-within .input-background {
  border-color: var(--primary-400);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.1);
}

.input-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: var(--gradient-primary);
  opacity: 0;
  transition: opacity var(--transition-fast);
}

.input-container:focus-within .input-gradient {
  opacity: 1;
}

.input-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: flex-end;
  gap: var(--space-3);
  padding: var(--space-4);
}

.input-field-container {
  flex: 1;
  position: relative;
}

.input-field {
  width: 100%;
  min-height: 24px;
  max-height: 120px;
  padding: var(--space-3) var(--space-4);
  background: transparent;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-family: var(--font-primary);
  font-size: var(--text-base);
  line-height: 1.5;
  resize: none;
  overflow-y: auto;
}

.input-field::placeholder {
  color: var(--text-muted);
}

.input-enhancements {
  position: absolute;
  bottom: -30px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.character-count {
  font-size: var(--text-xs);
  color: var(--text-muted);
  font-weight: 500;
}

.character-count.warning {
  color: var(--warning);
}

.input-suggestions {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.suggestion-chip {
  padding: var(--space-1) var(--space-2);
  background: var(--surface-elevated);
  border: 1px solid var(--border);
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.suggestion-chip:hover {
  background: var(--primary-400);
  color: white;
  transform: translateY(-1px);
}

/* Input Actions */
.input-actions {
  display: flex;
  gap: var(--space-2);
  align-items: flex-end;
}

.action-button {
  width: 40px;
  height: 40px;
  background: var(--surface-elevated);
  border: 1px solid var(--border);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast);
  color: var(--text-secondary);
}

.action-button:hover {
  background: var(--primary-400);
  color: white;
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.action-button.active {
  background: var(--error);
  color: white;
  animation: recording-pulse 1s ease-in-out infinite;
}

@keyframes recording-pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

.action-button svg {
  width: 18px;
  height: 18px;
}

.send-button {
  position: relative;
  width: 48px;
  height: 48px;
  background: var(--gradient-primary);
  border: none;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-normal);
  color: white;
  box-shadow: var(--shadow-md);
  overflow: hidden;
}

.send-button:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg), var(--shadow-glow);
}

.send-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none !important;
}

.send-button.pulse {
  animation: send-pulse 2s ease-in-out infinite;
}

@keyframes send-pulse {
  0%, 100% { box-shadow: var(--shadow-md); }
  50% { box-shadow: var(--shadow-lg), var(--shadow-glow); }
}

.button-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--gradient-primary);
  z-index: 1;
}

.send-button svg {
  width: 20px;
  height: 20px;
  z-index: 2;
  position: relative;
}

.sending-animation {
  z-index: 2;
  position: relative;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* Enhanced Message Styling */
.message-text :deep(.message-list) {
  margin: var(--space-3) 0;
  padding-left: var(--space-5);
}

.message-text :deep(.message-list li) {
  margin-bottom: var(--space-2);
  line-height: 1.6;
}

.message-text :deep(.message-code) {
  background: rgba(0,0,0,0.1);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  margin: var(--space-3) 0;
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  overflow-x: auto;
}

.message-user .message-text :deep(.message-code) {
  background: rgba(0,0,0,0.2);
}

.message-text :deep(strong) {
  font-weight: 600;
  color: var(--text-primary);
}

.message-user .message-text :deep(strong) {
  color: white;
}

.message-text :deep(em) {
  font-style: italic;
  color: var(--text-secondary);
}

.message-user .message-text :deep(em) {
  color: rgba(255,255,255,0.9);
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--space-4);
  }
  
  .session-metrics {
    width: 100%;
    justify-content: space-between;
  }
  
  .metric-card {
    flex: 1;
    min-width: 60px;
  }
  
  .chat-messages {
    padding: var(--space-4);
  }
  
  .chat-message {
    gap: var(--space-3);
  }
  
  .message-content {
    max-width: 85%;
  }
  
  .welcome-message {
    flex-direction: column;
    text-align: center;
  }
  
  .empty-features {
    flex-direction: column;
    gap: var(--space-3);
  }
  
  .input-content {
    padding: var(--space-3);
  }
  
  .ai-capabilities {
    justify-content: center;
  }
}

/* Scrollbar Styling */
.chat-messages::-webkit-scrollbar {
  width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
  background: var(--surface);
}

.chat-messages::-webkit-scrollbar-thumb {
  background: var(--border);
  border-radius: var(--radius-full);
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background: var(--primary-400);
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