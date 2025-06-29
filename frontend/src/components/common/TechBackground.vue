<template>
  <div ref="container" class="tech-background">
    <!-- Neural Network Visualization -->
    <div class="neural-network">
      <div class="neural-nodes">
        <div 
          v-for="node in neuralNodes" 
          :key="node.id"
          class="neural-node"
          :style="node.style"
        ></div>
      </div>
      <svg class="neural-connections" :width="windowWidth" :height="windowHeight">
        <defs>
          <linearGradient id="connectionGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:var(--primary-400);stop-opacity:0" />
            <stop offset="50%" style="stop-color:var(--primary-400);stop-opacity:0.6" />
            <stop offset="100%" style="stop-color:var(--secondary-500);stop-opacity:0" />
          </linearGradient>
          <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge> 
              <feMergeNode in="coloredBlur"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>
        <path 
          v-for="connection in neuralConnections" 
          :key="connection.id"
          :d="connection.path"
          class="neural-connection"
          :class="{ active: connection.active }"
        />
      </svg>
    </div>

    <!-- Floating Data Particles -->
    <div class="data-particles">
      <div 
        v-for="particle in dataParticles" 
        :key="particle.id"
        class="data-particle"
        :style="particle.style"
      >
        <div class="particle-core"></div>
        <div class="particle-ring"></div>
      </div>
    </div>

    <!-- Quantum Grid -->
    <div class="quantum-grid">
      <div 
        v-for="cell in quantumCells" 
        :key="cell.id"
        class="quantum-cell"
        :style="cell.style"
        :class="{ active: cell.active, pulsing: cell.pulsing }"
      ></div>
    </div>

    <!-- AI Consciousness Waves -->
    <div class="consciousness-waves">
      <div class="wave wave-1"></div>
      <div class="wave wave-2"></div>
      <div class="wave wave-3"></div>
    </div>

    <!-- Holographic Interface Elements -->
    <div class="holographic-elements">
      <div class="holo-circle holo-1"></div>
      <div class="holo-circle holo-2"></div>
      <div class="holo-hexagon"></div>
      <div class="holo-scanner"></div>
    </div>

    <!-- Matrix Rain Effect -->
    <div class="matrix-rain">
      <div 
        v-for="drop in matrixDrops" 
        :key="drop.id"
        class="matrix-drop"
        :style="drop.style"
      >{{ drop.char }}</div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onBeforeUnmount, reactive } from 'vue';
import { useUiStore } from '@/store/uiStore';

export default {
  name: 'TechBackground',
  setup() {
    const container = ref(null);
    const uiStore = useUiStore();
    
    const windowWidth = ref(window.innerWidth);
    const windowHeight = ref(window.innerHeight);
    
    // Neural Network Data
    const neuralNodes = ref([]);
    const neuralConnections = ref([]);
    
    // Data Particles
    const dataParticles = ref([]);
    
    // Quantum Grid
    const quantumCells = ref([]);
    
    // Matrix Rain
    const matrixDrops = ref([]);
    const matrixChars = '01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン';
    
    let animationId;
    let time = 0;
    
    // Initialize Neural Network
    const initNeuralNetwork = () => {
      const nodeCount = 50;
      neuralNodes.value = [];
      
      for (let i = 0; i < nodeCount; i++) {
        const node = {
          id: i,
          x: Math.random() * windowWidth.value,
          y: Math.random() * windowHeight.value,
          vx: (Math.random() - 0.5) * 0.5,
          vy: (Math.random() - 0.5) * 0.5,
          size: Math.random() * 4 + 2,
          pulse: Math.random() * Math.PI * 2,
          style: {}
        };
        neuralNodes.value.push(node);
      }
      
      updateNeuralConnections();
    };
    
    // Update Neural Connections
    const updateNeuralConnections = () => {
      neuralConnections.value = [];
      const maxDistance = 150;
      
      for (let i = 0; i < neuralNodes.value.length; i++) {
        for (let j = i + 1; j < neuralNodes.value.length; j++) {
          const nodeA = neuralNodes.value[i];
          const nodeB = neuralNodes.value[j];
          
          const distance = Math.sqrt(
            Math.pow(nodeA.x - nodeB.x, 2) + Math.pow(nodeA.y - nodeB.y, 2)
          );
          
          if (distance < maxDistance) {
            const connection = {
              id: `${i}-${j}`,
              path: `M ${nodeA.x} ${nodeA.y} Q ${(nodeA.x + nodeB.x) / 2} ${(nodeA.y + nodeB.y) / 2 - 20} ${nodeB.x} ${nodeB.y}`,
              active: Math.random() > 0.7,
              opacity: 1 - (distance / maxDistance)
            };
            neuralConnections.value.push(connection);
          }
        }
      }
    };
    
    // Initialize Data Particles
    const initDataParticles = () => {
      const particleCount = 30;
      dataParticles.value = [];
      
      for (let i = 0; i < particleCount; i++) {
        const particle = {
          id: i,
          x: Math.random() * windowWidth.value,
          y: Math.random() * windowHeight.value,
          vx: (Math.random() - 0.5) * 2,
          vy: (Math.random() - 0.5) * 2,
          rotation: 0,
          rotationSpeed: (Math.random() - 0.5) * 0.1,
          scale: Math.random() * 0.5 + 0.5,
          style: {}
        };
        dataParticles.value.push(particle);
      }
    };
    
    // Initialize Quantum Grid
    const initQuantumGrid = () => {
      const gridSize = 20;
      quantumCells.value = [];
      
      for (let x = 0; x < Math.ceil(windowWidth.value / gridSize); x++) {
        for (let y = 0; y < Math.ceil(windowHeight.value / gridSize); y++) {
          const cell = {
            id: `${x}-${y}`,
            x: x * gridSize,
            y: y * gridSize,
            active: false,
            pulsing: false,
            activationTime: 0,
            style: {}
          };
          quantumCells.value.push(cell);
        }
      }
    };
    
    // Initialize Matrix Rain
    const initMatrixRain = () => {
      const dropCount = 50;
      matrixDrops.value = [];
      
      for (let i = 0; i < dropCount; i++) {
        const drop = {
          id: i,
          x: Math.random() * windowWidth.value,
          y: Math.random() * windowHeight.value - windowHeight.value,
          speed: Math.random() * 3 + 1,
          char: matrixChars[Math.floor(Math.random() * matrixChars.length)],
          opacity: Math.random() * 0.5 + 0.3,
          style: {}
        };
        matrixDrops.value.push(drop);
      }
    };
    
    // Animation Loop
    const animate = () => {
      animationId = requestAnimationFrame(animate);
      time += 0.016; // ~60fps
      
      // Update Neural Network
      neuralNodes.value.forEach(node => {
        node.x += node.vx;
        node.y += node.vy;
        
        // Boundary bounce
        if (node.x < 0 || node.x > windowWidth.value) node.vx *= -1;
        if (node.y < 0 || node.y > windowHeight.value) node.vy *= -1;
        
        // Keep in bounds
        node.x = Math.max(0, Math.min(windowWidth.value, node.x));
        node.y = Math.max(0, Math.min(windowHeight.value, node.y));
        
        // Update pulse
        node.pulse += 0.05;
        const pulseScale = 1 + Math.sin(node.pulse) * 0.3;
        
        node.style = {
          left: `${node.x}px`,
          top: `${node.y}px`,
          width: `${node.size * pulseScale}px`,
          height: `${node.size * pulseScale}px`,
          opacity: 0.6 + Math.sin(node.pulse) * 0.4
        };
      });
      
      // Update connections every few frames
      if (Math.floor(time * 10) % 30 === 0) {
        updateNeuralConnections();
      }
      
      // Update Data Particles
      dataParticles.value.forEach(particle => {
        particle.x += particle.vx;
        particle.y += particle.vy;
        particle.rotation += particle.rotationSpeed;
        
        // Wrap around screen
        if (particle.x < -50) particle.x = windowWidth.value + 50;
        if (particle.x > windowWidth.value + 50) particle.x = -50;
        if (particle.y < -50) particle.y = windowHeight.value + 50;
        if (particle.y > windowHeight.value + 50) particle.y = -50;
        
        particle.style = {
          left: `${particle.x}px`,
          top: `${particle.y}px`,
          transform: `rotate(${particle.rotation}rad) scale(${particle.scale})`,
          opacity: 0.4 + Math.sin(time * 2 + particle.id) * 0.3
        };
      });
      
      // Update Quantum Grid
      quantumCells.value.forEach(cell => {
        // Random activation
        if (Math.random() > 0.998) {
          cell.active = true;
          cell.activationTime = time;
        }
        
        // Deactivate after time
        if (cell.active && time - cell.activationTime > 2) {
          cell.active = false;
        }
        
        // Pulsing effect
        cell.pulsing = Math.sin(time * 3 + cell.x * 0.01 + cell.y * 0.01) > 0.8;
        
        cell.style = {
          left: `${cell.x}px`,
          top: `${cell.y}px`,
          opacity: cell.active ? 0.8 : (cell.pulsing ? 0.3 : 0.1)
        };
      });
      
      // Update Matrix Rain
      matrixDrops.value.forEach(drop => {
        drop.y += drop.speed;
        
        // Reset when off screen
        if (drop.y > windowHeight.value + 20) {
          drop.y = -20;
          drop.x = Math.random() * windowWidth.value;
          drop.char = matrixChars[Math.floor(Math.random() * matrixChars.length)];
        }
        
        drop.style = {
          left: `${drop.x}px`,
          top: `${drop.y}px`,
          opacity: drop.opacity * (1 - drop.y / windowHeight.value)
        };
      });
    };
    
    // Handle window resize
    const onWindowResize = () => {
      windowWidth.value = window.innerWidth;
      windowHeight.value = window.innerHeight;
      
      // Reinitialize components
      initQuantumGrid();
    };
    
    // Lifecycle hooks
    onMounted(() => {
      initNeuralNetwork();
      initDataParticles();
      initQuantumGrid();
      initMatrixRain();
      
      window.addEventListener('resize', onWindowResize);
      animate();
    });
    
    onBeforeUnmount(() => {
      if (animationId) {
        cancelAnimationFrame(animationId);
      }
      window.removeEventListener('resize', onWindowResize);
    });
    
    return {
      container,
      windowWidth,
      windowHeight,
      neuralNodes,
      neuralConnections,
      dataParticles,
      quantumCells,
      matrixDrops
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
  background: var(--background);
  background-image: 
    radial-gradient(circle at 20% 20%, rgba(58, 134, 255, 0.03) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(131, 56, 236, 0.03) 0%, transparent 50%),
    radial-gradient(circle at 40% 60%, rgba(255, 0, 110, 0.02) 0%, transparent 50%);
}

/* Neural Network */
.neural-network {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.neural-nodes {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.neural-node {
  position: absolute;
  background: radial-gradient(circle, var(--primary-400) 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(0.5px);
  transition: all 0.3s ease;
}

.neural-connections {
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none;
}

.neural-connection {
  fill: none;
  stroke: url(#connectionGradient);
  stroke-width: 1;
  opacity: 0.3;
  filter: url(#glow);
  transition: all 0.5s ease;
}

.neural-connection.active {
  stroke-width: 2;
  opacity: 0.8;
  animation: pulse-connection 2s ease-in-out infinite;
}

@keyframes pulse-connection {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 1; }
}

/* Data Particles */
.data-particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.data-particle {
  position: absolute;
  width: 20px;
  height: 20px;
}

.particle-core {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 6px;
  height: 6px;
  background: var(--secondary-400);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 10px var(--secondary-400);
}

.particle-ring {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 20px;
  border: 1px solid var(--secondary-400);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.3;
  animation: particle-ring-pulse 3s ease-in-out infinite;
}

@keyframes particle-ring-pulse {
  0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.3; }
  50% { transform: translate(-50%, -50%) scale(1.5); opacity: 0.1; }
}

/* Quantum Grid */
.quantum-grid {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.quantum-cell {
  position: absolute;
  width: 20px;
  height: 20px;
  border: 1px solid var(--primary-400);
  background: rgba(58, 134, 255, 0.05);
  transition: all 0.3s ease;
}

.quantum-cell.active {
  background: rgba(58, 134, 255, 0.2);
  box-shadow: 0 0 15px var(--primary-400);
  transform: scale(1.1);
}

.quantum-cell.pulsing {
  background: rgba(58, 134, 255, 0.1);
  animation: quantum-pulse 1s ease-in-out;
}

@keyframes quantum-pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

/* Consciousness Waves */
.consciousness-waves {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.wave {
  position: absolute;
  width: 200%;
  height: 200%;
  background: radial-gradient(ellipse at center, transparent 40%, var(--primary-400) 41%, var(--primary-400) 42%, transparent 43%);
  border-radius: 50%;
  opacity: 0.1;
  animation: consciousness-wave 20s linear infinite;
}

.wave-1 {
  top: -50%;
  left: -50%;
  animation-delay: 0s;
}

.wave-2 {
  top: -50%;
  left: -50%;
  animation-delay: -7s;
}

.wave-3 {
  top: -50%;
  left: -50%;
  animation-delay: -14s;
}

@keyframes consciousness-wave {
  0% { transform: rotate(0deg) scale(0.5); opacity: 0; }
  50% { opacity: 0.1; }
  100% { transform: rotate(360deg) scale(2); opacity: 0; }
}

/* Holographic Elements */
.holographic-elements {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.holo-circle {
  position: absolute;
  border: 2px solid var(--accent-400);
  border-radius: 50%;
  opacity: 0.3;
}

.holo-1 {
  top: 10%;
  right: 10%;
  width: 100px;
  height: 100px;
  animation: holo-rotate 15s linear infinite;
}

.holo-2 {
  bottom: 20%;
  left: 15%;
  width: 150px;
  height: 150px;
  animation: holo-rotate 20s linear infinite reverse;
}

.holo-hexagon {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 80px;
  height: 80px;
  border: 2px solid var(--secondary-400);
  transform: translate(-50%, -50%) rotate(0deg);
  clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
  opacity: 0.2;
  animation: holo-hexagon-spin 25s linear infinite;
}

.holo-scanner {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent 0%, var(--accent-400) 50%, transparent 100%);
  opacity: 0.6;
  animation: holo-scan 8s ease-in-out infinite;
}

@keyframes holo-rotate {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes holo-hexagon-spin {
  0% { transform: translate(-50%, -50%) rotate(0deg); }
  100% { transform: translate(-50%, -50%) rotate(360deg); }
}

@keyframes holo-scan {
  0%, 100% { top: 0; opacity: 0; }
  50% { top: 100%; opacity: 0.6; }
}

/* Matrix Rain */
.matrix-rain {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  font-family: var(--font-mono);
  font-size: 14px;
  color: var(--success);
  pointer-events: none;
}

.matrix-drop {
  position: absolute;
  opacity: 0.3;
  text-shadow: 0 0 5px currentColor;
  animation: matrix-flicker 0.5s ease-in-out infinite alternate;
}

@keyframes matrix-flicker {
  0% { opacity: 0.3; }
  100% { opacity: 0.8; }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .neural-node {
    filter: blur(1px);
  }
  
  .data-particle {
    width: 15px;
    height: 15px;
  }
  
  .particle-core {
    width: 4px;
    height: 4px;
  }
  
  .particle-ring {
    width: 15px;
    height: 15px;
  }
  
  .quantum-cell {
    width: 15px;
    height: 15px;
  }
  
  .matrix-drop {
    font-size: 12px;
  }
}
</style>