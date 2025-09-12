// Enhanced Social Media Sharing Script for AI Agents Blog Post
// This script optimizes social sharing for maximum engagement

document.addEventListener('DOMContentLoaded', function() {
    // Add share buttons if they don't exist
    if (!document.querySelector('.social-share-buttons')) {
        addSocialShareButtons();
    }
    
    // Track social shares for analytics
    trackSocialShares();
    
    // Enhance meta tags dynamically based on user behavior
    enhanceMetaTags();
});

function addSocialShareButtons() {
    const shareHTML = `
        <div class="social-share-buttons" style="
            position: fixed;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 1000;
            display: flex;
            flex-direction: column;
            gap: 10px;
            opacity: 0.8;
            transition: opacity 0.3s ease;
        ">
            <a href="#" onclick="shareOnTwitter()" class="share-btn twitter" style="
                background: linear-gradient(45deg, #1da1f2, #1da1f2);
                color: white;
                padding: 12px;
                border-radius: 50%;
                text-decoration: none;
                box-shadow: 0 4px 15px rgba(29, 161, 242, 0.3);
                transition: transform 0.3s ease;
            ">🐦</a>
            
            <a href="#" onclick="shareOnLinkedIn()" class="share-btn linkedin" style="
                background: linear-gradient(45deg, #0077b5, #0077b5);
                color: white;
                padding: 12px;
                border-radius: 50%;
                text-decoration: none;
                box-shadow: 0 4px 15px rgba(0, 119, 181, 0.3);
                transition: transform 0.3s ease;
            ">💼</a>
            
            <a href="#" onclick="shareOnFacebook()" class="share-btn facebook" style="
                background: linear-gradient(45deg, #1877f2, #1877f2);
                color: white;
                padding: 12px;
                border-radius: 50%;
                text-decoration: none;
                box-shadow: 0 4px 15px rgba(24, 119, 242, 0.3);
                transition: transform 0.3s ease;
            ">📘</a>
            
            <a href="#" onclick="shareOnReddit()" class="share-btn reddit" style="
                background: linear-gradient(45deg, #ff4500, #ff4500);
                color: white;
                padding: 12px;
                border-radius: 50%;
                text-decoration: none;
                box-shadow: 0 4px 15px rgba(255, 69, 0, 0.3);
                transition: transform 0.3s ease;
            ">🔗</a>
            
            <a href="#" onclick="copyLink()" class="share-btn copy" style="
                background: linear-gradient(45deg, #6366f1, #8b5cf6);
                color: white;
                padding: 12px;
                border-radius: 50%;
                text-decoration: none;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
                transition: transform 0.3s ease;
            ">📋</a>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', shareHTML);
    
    // Add hover effects
    const shareButtons = document.querySelectorAll('.share-btn');
    shareButtons.forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.1)';
        });
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
}

function shareOnTwitter() {
    const title = "🚀 AI Agents: Build Smart Digital Assistants That Work 24/7";
    const text = "💡 Just discovered this amazing guide on building AI agents! No coding required - these digital assistants handle emails, schedule meetings & automate workflows while you sleep 😴✨";
    const url = window.location.href;
    const hashtags = "AIAgents,Automation,Productivity,NoCode,AI,TechTrends";
    
    const shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}&hashtags=${hashtags}`;
    window.open(shareUrl, '_blank', 'width=550,height=420');
    
    // Track sharing
    if (typeof gtag !== 'undefined') {
        gtag('event', 'share', {
            method: 'Twitter',
            content_type: 'article',
            content_id: 'ai-agents-ultimate-guide'
        });
    }
}

function shareOnLinkedIn() {
    const title = "AI Agents: The Ultimate Guide to Building Smart Digital Assistants";
    const summary = "Stop doing repetitive tasks! Learn how to build AI agents that work 24/7, handling emails, scheduling, and workflow automation. Comprehensive guide with no-code solutions.";
    const url = window.location.href;
    
    const shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}&summary=${encodeURIComponent(summary)}`;
    window.open(shareUrl, '_blank', 'width=550,height=420');
    
    if (typeof gtag !== 'undefined') {
        gtag('event', 'share', {
            method: 'LinkedIn',
            content_type: 'article',
            content_id: 'ai-agents-ultimate-guide'
        });
    }
}

function shareOnFacebook() {
    const url = window.location.href;
    const shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
    window.open(shareUrl, '_blank', 'width=550,height=420');
    
    if (typeof gtag !== 'undefined') {
        gtag('event', 'share', {
            method: 'Facebook',
            content_type: 'article',
            content_id: 'ai-agents-ultimate-guide'
        });
    }
}

function shareOnReddit() {
    const title = "🚀 AI Agents: Ultimate Guide to Building Smart Digital Assistants That Work 24/7";
    const url = window.location.href;
    
    const shareUrl = `https://reddit.com/submit?url=${encodeURIComponent(url)}&title=${encodeURIComponent(title)}`;
    window.open(shareUrl, '_blank', 'width=550,height=420');
    
    if (typeof gtag !== 'undefined') {
        gtag('event', 'share', {
            method: 'Reddit',
            content_type: 'article',
            content_id: 'ai-agents-ultimate-guide'
        });
    }
}

function copyLink() {
    navigator.clipboard.writeText(window.location.href).then(function() {
        // Show success message
        const btn = event.target;
        const originalText = btn.textContent;
        btn.textContent = '✅';
        btn.style.background = 'linear-gradient(45deg, #10b981, #059669)';
        
        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.background = 'linear-gradient(45deg, #6366f1, #8b5cf6)';
        }, 2000);
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'share', {
                method: 'Copy Link',
                content_type: 'article',
                content_id: 'ai-agents-ultimate-guide'
            });
        }
    });
}

function trackSocialShares() {
    // Track when users scroll to different sections for engagement metrics
    const sections = document.querySelectorAll('h2, h3');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && typeof gtag !== 'undefined') {
                gtag('event', 'scroll', {
                    event_category: 'engagement',
                    event_label: entry.target.textContent.trim(),
                    value: Math.round(entry.intersectionRatio * 100)
                });
            }
        });
    }, { threshold: 0.5 });
    
    sections.forEach(section => observer.observe(section));
}

function enhanceMetaTags() {
    // Add dynamic structured data for better SEO
    const structuredData = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "AI Agents: The Ultimate Guide to Building Smart Digital Assistants in 2025",
        "description": "Stop doing repetitive tasks! Learn how to build AI agents that handle emails, schedule meetings, and automate your workflow while you sleep. No-code solutions with step-by-step tutorials.",
        "image": "https://promptmakers.app/images/og-ai-agents-guide.webp",
        "author": {
            "@type": "Person",
            "name": "Alex Chen"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Promptmakers",
            "logo": {
                "@type": "ImageObject",
                "url": "https://promptmakers.app/favicon.ico"
            }
        },
        "datePublished": "2025-01-10",
        "dateModified": "2025-01-10",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": window.location.href
        },
        "keywords": ["AI agents", "automation", "productivity", "no-code", "digital assistants", "workflow automation"],
        "articleSection": "Technology",
        "wordCount": 2500,
        "timeRequired": "PT8M"
    };
    
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.textContent = JSON.stringify(structuredData);
    document.head.appendChild(script);
}

// Enhanced scroll-to-share feature
window.addEventListener('scroll', function() {
    const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
    const shareButtons = document.querySelector('.social-share-buttons');
    
    if (shareButtons) {
        if (scrollPercent > 20 && scrollPercent < 80) {
            shareButtons.style.opacity = '1';
            shareButtons.style.transform = 'translateY(-50%) scale(1)';
        } else {
            shareButtons.style.opacity = '0.5';
            shareButtons.style.transform = 'translateY(-50%) scale(0.8)';
        }
    }
});

console.log('🚀 AI Agents Blog Post - Social Sharing Enhanced! Share away! 🎉');
