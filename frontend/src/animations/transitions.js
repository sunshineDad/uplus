import { gsap } from 'gsap';

// Page transition animations
export const pageTransitions = {
  // Fade in animation
  fadeIn(el, done) {
    gsap.fromTo(
      el,
      { opacity: 0 },
      {
        opacity: 1,
        duration: 0.5,
        ease: 'power2.inOut',
        onComplete: done
      }
    );
  },
  
  // Fade out animation
  fadeOut(el, done) {
    gsap.to(el, {
      opacity: 0,
      duration: 0.3,
      ease: 'power2.inOut',
      onComplete: done
    });
  },
  
  // Slide up animation
  slideUp(el, done) {
    gsap.fromTo(
      el,
      { y: 50, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.5,
        ease: 'power2.out',
        onComplete: done
      }
    );
  },
  
  // Slide down animation
  slideDown(el, done) {
    gsap.to(el, {
      y: 50,
      opacity: 0,
      duration: 0.3,
      ease: 'power2.in',
      onComplete: done
    });
  },
  
  // Scale up animation
  scaleUp(el, done) {
    gsap.fromTo(
      el,
      { scale: 0.8, opacity: 0 },
      {
        scale: 1,
        opacity: 1,
        duration: 0.5,
        ease: 'back.out(1.7)',
        onComplete: done
      }
    );
  },
  
  // Scale down animation
  scaleDown(el, done) {
    gsap.to(el, {
      scale: 0.8,
      opacity: 0,
      duration: 0.3,
      ease: 'back.in(1.7)',
      onComplete: done
    });
  },
};

// Element animations
export const elementAnimations = {
  // Stagger children animation
  staggerChildren(parent, childSelector, staggerAmount = 0.1) {
    const children = parent.querySelectorAll(childSelector);
    
    gsap.fromTo(
      children,
      { y: 20, opacity: 0 },
      {
        y: 0,
        opacity: 1,
        duration: 0.5,
        stagger: staggerAmount,
        ease: 'power2.out'
      }
    );
  },
  
  // Pulse animation
  pulse(element) {
    gsap.fromTo(
      element,
      { scale: 1 },
      {
        scale: 1.05,
        duration: 0.3,
        yoyo: true,
        repeat: 1,
        ease: 'power2.inOut'
      }
    );
  },
  
  // Highlight animation
  highlight(element, color = 'rgba(58, 134, 255, 0.2)') {
    const originalBackground = getComputedStyle(element).backgroundColor;
    
    gsap.fromTo(
      element,
      { backgroundColor: color },
      {
        backgroundColor: originalBackground,
        duration: 1,
        ease: 'power2.out'
      }
    );
  },
  
  // Shake animation
  shake(element) {
    gsap.fromTo(
      element,
      { x: -5 },
      {
        x: 0,
        duration: 0.4,
        ease: 'elastic.out(1, 0.3)',
        yoyo: true,
        repeat: 2
      }
    );
  },
  
  // Typing animation
  typing(element, text, speed = 30) {
    const originalText = text;
    element.textContent = '';
    
    let i = 0;
    const typeInterval = setInterval(() => {
      if (i < originalText.length) {
        element.textContent += originalText.charAt(i);
        i++;
      } else {
        clearInterval(typeInterval);
      }
    }, speed);
    
    return typeInterval;
  },
};

// Tech-style animations
export const techAnimations = {
  // Glitch effect
  glitch(element, duration = 1) {
    const timeline = gsap.timeline();
    
    // Save original position
    const originalX = element.getBoundingClientRect().left;
    const originalY = element.getBoundingClientRect().top;
    
    // Create glitch effect
    timeline
      .to(element, {
        x: originalX - 5,
        y: originalY + 3,
        duration: 0.05,
        skewX: 10,
        opacity: 0.8
      })
      .to(element, {
        x: originalX + 3,
        y: originalY - 2,
        duration: 0.05,
        skewX: -5,
        opacity: 0.9
      })
      .to(element, {
        x: originalX - 2,
        y: originalY + 1,
        duration: 0.05,
        skewX: 3,
        opacity: 1
      })
      .to(element, {
        x: 0,
        y: 0,
        skewX: 0,
        duration: 0.05
      });
    
    return timeline;
  },
  
  // Data flow animation
  dataFlow(element, direction = 'right') {
    const overlay = document.createElement('div');
    overlay.style.position = 'absolute';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.background = 'linear-gradient(90deg, transparent, rgba(58, 134, 255, 0.3), transparent)';
    overlay.style.zIndex = '1';
    
    // Make sure element has position relative
    const originalPosition = getComputedStyle(element).position;
    if (originalPosition === 'static') {
      element.style.position = 'relative';
    }
    
    element.appendChild(overlay);
    
    // Animate the overlay
    let fromX, toX;
    if (direction === 'right') {
      fromX = '-100%';
      toX = '200%';
    } else {
      fromX = '200%';
      toX = '-100%';
    }
    
    gsap.fromTo(
      overlay,
      { x: fromX },
      {
        x: toX,
        duration: 1.5,
        ease: 'power2.inOut',
        onComplete: () => {
          element.removeChild(overlay);
          if (originalPosition === 'static') {
            element.style.position = originalPosition;
          }
        }
      }
    );
  },
  
  // Hologram effect
  hologram(element) {
    // Add hologram effect classes
    element.classList.add('hologram-effect');
    
    // Create style if it doesn't exist
    if (!document.getElementById('hologram-style')) {
      const style = document.createElement('style');
      style.id = 'hologram-style';
      style.textContent = `
        .hologram-effect {
          position: relative;
          overflow: hidden;
        }
        .hologram-effect::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: linear-gradient(45deg, transparent 65%, rgba(58, 134, 255, 0.3) 70%, transparent 75%);
          background-size: 200% 200%;
          animation: hologram-scan 3s linear infinite;
          pointer-events: none;
        }
        .hologram-effect::after {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          height: 1px;
          background: rgba(58, 134, 255, 0.5);
          animation: hologram-line 5s linear infinite;
          pointer-events: none;
        }
        @keyframes hologram-scan {
          0% { background-position: 0% 0%; }
          100% { background-position: 200% 200%; }
        }
        @keyframes hologram-line {
          0% { top: 0%; }
          100% { top: 100%; }
        }
      `;
      document.head.appendChild(style);
    }
    
    // Return a function to remove the effect
    return () => {
      element.classList.remove('hologram-effect');
    };
  },
  
  // Matrix code rain effect
  matrixRain(container, duration = 10) {
    // Create canvas
    const canvas = document.createElement('canvas');
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.zIndex = '1';
    canvas.style.opacity = '0.7';
    canvas.style.pointerEvents = 'none';
    
    // Make sure container has position relative
    const originalPosition = getComputedStyle(container).position;
    if (originalPosition === 'static') {
      container.style.position = 'relative';
    }
    
    container.appendChild(canvas);
    
    // Set canvas size
    canvas.width = container.offsetWidth;
    canvas.height = container.offsetHeight;
    
    // Get context
    const ctx = canvas.getContext('2d');
    
    // Matrix characters
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    
    // Column setup
    const fontSize = 14;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = [];
    
    // Initialize drops
    for (let i = 0; i < columns; i++) {
      drops[i] = Math.floor(Math.random() * -canvas.height / fontSize);
    }
    
    // Draw function
    function draw() {
      // Fade effect
      ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      
      // Text style
      ctx.fillStyle = '#3a86ff';
      ctx.font = `${fontSize}px monospace`;
      
      // Draw characters
      for (let i = 0; i < drops.length; i++) {
        // Random character
        const char = chars[Math.floor(Math.random() * chars.length)];
        
        // Draw character
        ctx.fillText(char, i * fontSize, drops[i] * fontSize);
        
        // Move drop
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }
        drops[i]++;
      }
    }
    
    // Animation loop
    let animationId;
    function animate() {
      draw();
      animationId = requestAnimationFrame(animate);
    }
    
    // Start animation
    animate();
    
    // Stop after duration
    if (duration) {
      setTimeout(() => {
        cancelAnimationFrame(animationId);
        container.removeChild(canvas);
        if (originalPosition === 'static') {
          container.style.position = originalPosition;
        }
      }, duration * 1000);
    }
    
    // Return function to stop animation
    return () => {
      cancelAnimationFrame(animationId);
      if (container.contains(canvas)) {
        container.removeChild(canvas);
      }
      if (originalPosition === 'static') {
        container.style.position = originalPosition;
      }
    };
  },
};

export default {
  pageTransitions,
  elementAnimations,
  techAnimations,
};