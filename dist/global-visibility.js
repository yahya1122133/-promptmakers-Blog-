// Global Visibility Enhancement Script
(function() {
  'use strict';
  
  // Reading Progress Bar
  function initReadingProgress() {
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    progressBar.innerHTML = '<div class="reading-progress-bar"></div>';
    document.body.appendChild(progressBar);
    
    const bar = progressBar.querySelector('.reading-progress-bar');
    
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      bar.style.width = scrolled + '%';
    });
  }
  
  // Social Sharing Functions - DISABLED to match existing blog style
  function createSocialShare() {
    // Skip creating floating social share - using inline version instead
    return;
  }
  
  // Floating Table of Contents - DISABLED to match existing blog style
  function createFloatingTOC() {
    // Skip creating floating TOC - keeping it simple like other blog posts
    return;
  }
  
  // SEO-focused content enhancements
  function enhanceContentForSEO() {
    // Add reading time estimation - smaller and less intrusive
    const wordCount = document.body.innerText.split(/\s+/).length;
    const readingTime = Math.ceil(wordCount / 200); // 200 WPM average
    
    const timeIndicator = document.createElement('div');
    timeIndicator.className = 'reading-time';
    timeIndicator.innerHTML = `⏱️ ${readingTime} min read`;
    timeIndicator.style.cssText = `
      position: fixed;
      bottom: 20px;
      right: 20px;
      background: rgba(107, 114, 128, 0.8);
      color: white;
      padding: 6px 12px;
      border-radius: 15px;
      font-size: 11px;
      font-weight: 500;
      z-index: 1000;
      backdrop-filter: blur(10px);
      opacity: 0.7;
      transition: opacity 0.3s ease;
    `;
    
    // Make it fade on hover
    timeIndicator.addEventListener('mouseenter', () => {
      timeIndicator.style.opacity = '0.3';
    });
    timeIndicator.addEventListener('mouseleave', () => {
      timeIndicator.style.opacity = '0.7';
    });
    
    document.body.appendChild(timeIndicator);
  }
  
  // Page performance tracking
  function trackPagePerformance() {
    if ('performance' in window) {
      window.addEventListener('load', () => {
        setTimeout(() => {
          const perf = performance.getEntriesByType('navigation')[0];
          const loadTime = perf.loadEventEnd - perf.loadEventStart;
          
          if (typeof gtag !== 'undefined') {
            gtag('event', 'timing_complete', {
              name: 'page_load',
              value: Math.round(loadTime)
            });
          }
        }, 0);
      });
    }
  }
  
  // Initialize all features when DOM is ready
  function init() {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
      return;
    }
    
    // Load CSS if not already present
    if (!document.querySelector('link[href*="social-features.css"]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = '/social-features.css';
      document.head.appendChild(link);
    }
    
    // Initialize features
    initReadingProgress();
    createSocialShare();
    createFloatingTOC();
    enhanceContentForSEO();
    trackPagePerformance();
    
    // Track scroll depth
    let maxScroll = 0;
    window.addEventListener('scroll', () => {
      const scrollPercent = Math.round(
        ((window.scrollY + window.innerHeight) / document.body.scrollHeight) * 100
      );
      
      if (scrollPercent > maxScroll) {
        maxScroll = scrollPercent;
        
        // Track milestone scrolls
        if ([25, 50, 75, 90].includes(scrollPercent) && typeof gtag !== 'undefined') {
          gtag('event', 'scroll', {
            event_category: 'engagement',
            event_label: `${scrollPercent}%`,
            value: scrollPercent
          });
        }
      }
    });
  }
  
  init();
})();

// Newsletter signup enhancement
function enhanceNewsletterSignup() {
  const forms = document.querySelectorAll('.newsletter-form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      if (typeof gtag !== 'undefined') {
        gtag('event', 'newsletter_signup', {
          event_category: 'engagement',
          event_label: 'blog_post'
        });
      }
    });
  });
}

// Call after DOM loads
document.addEventListener('DOMContentLoaded', enhanceNewsletterSignup);
