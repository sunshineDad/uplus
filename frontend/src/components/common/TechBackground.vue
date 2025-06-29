<template>
  <div ref="container" class="tech-background" :class="{ 'dark-mode': isDarkMode }"></div>
</template>

<script>
import { ref, computed, onMounted, onBeforeUnmount, watch } from 'vue';
import { useUiStore } from '@/store/uiStore';
import * as THREE from 'three';

export default {
  name: 'TechBackground',
  props: {
    particleCount: {
      type: Number,
      default: 1000
    },
    particleSize: {
      type: Number,
      default: 0.02
    },
    speed: {
      type: Number,
      default: 0.001
    }
  },
  setup(props) {
    const container = ref(null);
    const uiStore = useUiStore();
    
    // Computed properties
    const isDarkMode = computed(() => uiStore.darkMode);
    const particleColor = computed(() => isDarkMode.value ? '#3a86ff' : '#3a86ff');
    
    let scene, camera, renderer, particles, animationId;
    
    // Initialize Three.js scene
    const initScene = () => {
      // Create scene
      scene = new THREE.Scene();
      
      // Create camera
      camera = new THREE.PerspectiveCamera(
        75,
        container.value.clientWidth / container.value.clientHeight,
        0.1,
        1000
      );
      camera.position.z = 2;
      
      // Create renderer
      renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
      renderer.setSize(container.value.clientWidth, container.value.clientHeight);
      renderer.setPixelRatio(window.devicePixelRatio);
      container.value.appendChild(renderer.domElement);
      
      // Create particles
      createParticles();
      
      // Handle window resize
      window.addEventListener('resize', onWindowResize);
      
      // Start animation loop
      animate();
    };
    
    // Create particles
    const createParticles = () => {
      // Create geometry
      const geometry = new THREE.BufferGeometry();
      const positions = new Float32Array(props.particleCount * 3);
      const velocities = new Float32Array(props.particleCount * 3);
      
      // Set random positions and velocities
      for (let i = 0; i < props.particleCount; i++) {
        const i3 = i * 3;
        
        // Position
        positions[i3] = (Math.random() - 0.5) * 4;
        positions[i3 + 1] = (Math.random() - 0.5) * 4;
        positions[i3 + 2] = (Math.random() - 0.5) * 4;
        
        // Velocity
        velocities[i3] = (Math.random() - 0.5) * 0.01;
        velocities[i3 + 1] = (Math.random() - 0.5) * 0.01;
        velocities[i3 + 2] = (Math.random() - 0.5) * 0.01;
      }
      
      // Set geometry attributes
      geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
      geometry.setAttribute('velocity', new THREE.BufferAttribute(velocities, 3));
      
      // Create material
      const material = new THREE.PointsMaterial({
        color: new THREE.Color(particleColor.value),
        size: props.particleSize,
        transparent: true,
        opacity: isDarkMode.value ? 0.8 : 0.5,
        blending: THREE.AdditiveBlending,
        sizeAttenuation: true
      });
      
      // Create particles
      particles = new THREE.Points(geometry, material);
      scene.add(particles);
    };
    
    // Update particle material when dark mode changes
    const updateParticleMaterial = () => {
      if (particles && particles.material) {
        particles.material.color = new THREE.Color(particleColor.value);
        particles.material.opacity = isDarkMode.value ? 0.8 : 0.5;
        particles.material.needsUpdate = true;
      }
    };
    
    // Animation loop
    const animate = () => {
      animationId = requestAnimationFrame(animate);
      
      // Rotate particles
      particles.rotation.x += props.speed * 0.5;
      particles.rotation.y += props.speed;
      
      // Update particle positions
      const positions = particles.geometry.attributes.position.array;
      const velocities = particles.geometry.attributes.velocity.array;
      
      for (let i = 0; i < props.particleCount; i++) {
        const i3 = i * 3;
        
        // Update position based on velocity
        positions[i3] += velocities[i3];
        positions[i3 + 1] += velocities[i3 + 1];
        positions[i3 + 2] += velocities[i3 + 2];
        
        // Boundary check
        if (Math.abs(positions[i3]) > 2) velocities[i3] *= -1;
        if (Math.abs(positions[i3 + 1]) > 2) velocities[i3 + 1] *= -1;
        if (Math.abs(positions[i3 + 2]) > 2) velocities[i3 + 2] *= -1;
      }
      
      particles.geometry.attributes.position.needsUpdate = true;
      
      // Render scene
      renderer.render(scene, camera);
    };
    
    // Handle window resize
    const onWindowResize = () => {
      camera.aspect = container.value.clientWidth / container.value.clientHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(container.value.clientWidth, container.value.clientHeight);
    };
    
    // Watch for dark mode changes
    watch(isDarkMode, () => {
      updateParticleMaterial();
    });
    
    // Lifecycle hooks
    onMounted(() => {
      if (container.value) {
        initScene();
      }
    });
    
    onBeforeUnmount(() => {
      if (animationId) {
        cancelAnimationFrame(animationId);
      }
      
      if (renderer) {
        renderer.dispose();
      }
      
      window.removeEventListener('resize', onWindowResize);
    });
    
    return {
      container,
      isDarkMode
    };
  }
};
</script>

<style scoped>
.tech-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
  background-color: var(--gray-100);
  transition: background-color var(--transition-normal) var(--transition-timing);
}

.tech-background.dark-mode {
  background-color: var(--dark);
}
</style>