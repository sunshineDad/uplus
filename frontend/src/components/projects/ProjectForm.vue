<template>
  <div class="project-form">
    <h2 class="form-title">{{ isEdit ? 'Edit Project' : 'Create New Project' }}</h2>
    
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="project-name" class="form-label">Project Name</label>
        <input
          id="project-name"
          v-model="form.name"
          type="text"
          class="form-control"
          placeholder="Enter project name"
          required
        />
      </div>
      
      <div class="form-group">
        <label for="project-description" class="form-label">Description</label>
        <textarea
          id="project-description"
          v-model="form.description"
          class="form-control"
          placeholder="Enter project description"
          rows="4"
        ></textarea>
      </div>
      
      <div class="form-group">
        <label for="project-status" class="form-label">Status</label>
        <select
          id="project-status"
          v-model="form.status"
          class="form-control"
          required
        >
          <option value="ACTIVE">Active</option>
          <option value="PENDING">Pending</option>
          <option value="COMPLETED">Completed</option>
          <option value="ARCHIVED">Archived</option>
        </select>
      </div>
      
      <div class="form-actions">
        <button type="button" class="btn btn-outline-secondary" @click="$emit('cancel')">
          Cancel
        </button>
        <button type="submit" class="btn btn-primary" :disabled="loading">
          {{ loading ? 'Saving...' : (isEdit ? 'Update Project' : 'Create Project') }}
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';

export default {
  name: 'ProjectForm',
  props: {
    project: {
      type: Object,
      default: null
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
  emits: ['submit', 'cancel'],
  setup(props, { emit }) {
    // Form data
    const form = ref({
      name: '',
      description: '',
      status: 'ACTIVE'
    });
    
    // Computed properties
    const isEdit = computed(() => !!props.project);
    
    // Methods
    const handleSubmit = () => {
      emit('submit', { ...form.value });
    };
    
    // Initialize form with project data if editing
    onMounted(() => {
      if (props.project) {
        form.value = {
          name: props.project.name || '',
          description: props.project.description || '',
          status: props.project.status || 'ACTIVE'
        };
      }
    });
    
    return {
      form,
      isEdit,
      handleSubmit
    };
  }
};
</script>

<style scoped>
.project-form {
  padding: 1.5rem;
  background-color: var(--white);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
}

.form-title {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--gray-900);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--gray-700);
}

.form-control {
  width: 100%;
  padding: 0.75rem 1rem;
  font-size: 1rem;
  color: var(--gray-800);
  background-color: var(--white);
  border: 1px solid var(--gray-300);
  border-radius: var(--border-radius-md);
  transition: all var(--transition-normal) var(--transition-timing);
}

.form-control:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.2);
  outline: none;
}

.form-control::placeholder {
  color: var(--gray-500);
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 2rem;
}

/* Dark mode adjustments */
:global(.dark-mode) .project-form {
  background-color: var(--dark-blue);
}

:global(.dark-mode) .form-title {
  color: var(--white);
}

:global(.dark-mode) .form-label {
  color: var(--gray-300);
}

:global(.dark-mode) .form-control {
  color: var(--gray-200);
  background-color: var(--dark-purple);
  border-color: var(--gray-700);
}

:global(.dark-mode) .form-control:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.3);
}

:global(.dark-mode) .form-control::placeholder {
  color: var(--gray-500);
}
</style>