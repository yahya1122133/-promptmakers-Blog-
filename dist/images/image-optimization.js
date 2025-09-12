// Image Optimization Script for AI Agents Blog
// This creates fallback versions and optimizes images for different platforms

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎨 AI Agents Blog - Image Optimization Active');
    
    // Check if we need to create fallback images for older browsers
    if (!supportsSVG()) {
        createImageFallbacks();
    }
    
    // Optimize images for performance
    optimizeImageLoading();
    
    // Add image lazy loading for better performance
    addLazyLoading();
});

function supportsSVG() {
    return document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image", "1.1");
}

function createImageFallbacks() {
    // For browsers that don't support SVG, we can create canvas-based fallbacks
    const svgImages = document.querySelectorAll('img[src$=".svg"]');
    
    svgImages.forEach(img => {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        
        // Set canvas size based on the image
        canvas.width = img.naturalWidth || 800;
        canvas.height = img.naturalHeight || 400;
        
        // Create a fallback background
        const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
        gradient.addColorStop(0, '#0f172a');
        gradient.addColorStop(0.5, '#1e293b');
        gradient.addColorStop(1, '#334155');
        
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Add text overlay
        ctx.fillStyle = '#e2e8f0';
        ctx.font = 'bold 48px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('AI AGENTS', canvas.width / 2, canvas.height / 2 - 20);
        
        ctx.font = '24px Arial';
        ctx.fillText('Ultimate Guide 2025', canvas.width / 2, canvas.height / 2 + 20);
        
        // Replace the SVG with canvas
        img.style.display = 'none';
        img.parentNode.insertBefore(canvas, img.nextSibling);
    });
}

function optimizeImageLoading() {
    // Add intersection observer for image optimization
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    
                    // Add loading optimization
                    img.style.opacity = '0';
                    img.style.transition = 'opacity 0.3s ease';
                    
                    img.onload = function() {
                        this.style.opacity = '1';
                    };
                    
                    observer.unobserve(img);
                }
            });
        });
        
        document.querySelectorAll('img').forEach(img => {
            imageObserver.observe(img);
        });
    }
}

function addLazyLoading() {
    // Add native lazy loading to images
    document.querySelectorAll('img').forEach(img => {
        if (!img.hasAttribute('loading')) {
            img.setAttribute('loading', 'lazy');
        }
    });
}

// Social media image optimization
function generateSocialImages() {
    // This function can be called to generate optimized social media images
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    // Open Graph size (1200x630)
    canvas.width = 1200;
    canvas.height = 630;
    
    // Create the social media optimized version
    const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
    gradient.addColorStop(0, '#0f0f23');
    gradient.addColorStop(0.5, '#1a1a3e');
    gradient.addColorStop(1, '#2d1b69');
    
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Add title with gradient effect
    const titleGradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
    titleGradient.addColorStop(0, '#60a5fa');
    titleGradient.addColorStop(0.5, '#a78bfa');
    titleGradient.addColorStop(1, '#f472b6');
    
    ctx.fillStyle = titleGradient;
    ctx.font = 'bold 72px Arial';
    ctx.textAlign = 'left';
    ctx.fillText('AI AGENTS', 60, 200);
    
    ctx.fillStyle = '#e2e8f0';
    ctx.font = '36px Arial';
    ctx.fillText('The Ultimate Guide to Building', 60, 260);
    ctx.fillText('Smart Digital Assistants', 60, 300);
    
    ctx.font = 'bold 20px Arial';
    ctx.fillStyle = '#60a5fa';
    ctx.fillText('● Autonomous AI That Works 24/7', 60, 380);
    ctx.fillStyle = '#a78bfa';
    ctx.fillText('● No-Code Building Tutorials', 60, 410);
    ctx.fillStyle = '#f472b6';
    ctx.fillText('● Real Business Applications', 60, 440);
    
    // Add brand
    ctx.fillStyle = '#64748b';
    ctx.font = '16px Arial';
    ctx.textAlign = 'right';
    ctx.fillText('promptmakers.app', canvas.width - 60, canvas.height - 20);
    
    return canvas.toDataURL('image/png');
}

console.log('✨ Image optimization loaded for AI Agents blog post!');
