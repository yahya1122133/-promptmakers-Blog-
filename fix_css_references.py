#!/usr/bin/env python3
"""
Script to fix CSS references in blog posts by replacing external CSS links with inline styles.
This fixes the local development server CSS loading issues.
"""

import os
import re
import glob

def get_inline_css():
    """Return the consolidated CSS styles for blog posts."""
    return '''<style>
/* Consolidated Blog Post Styles */
:root{
    --color-bg: #0f0f23;
    --color-bg-secondary: #1a1a2e;
    --color-text: #ffffff;
    --color-text-secondary: #94a3b8;
    --color-accent: #8b5cf6;
    --color-accent-hover: #7c3aed;
    --color-border: #334155;
    --color-primary: #8b5cf6;
    --color-secondary: #06b6d4;
    --font-family: "Inter", sans-serif;
}

/* Global Resets */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-family);
    background: var(--color-bg);
    color: var(--color-text);
    line-height: 1.6;
}

a {
    color: var(--color-accent);
    text-decoration: none;
}

a:hover {
    color: var(--color-accent-hover);
}

/* Header Styles */
.header {
    background: var(--color-bg);
    border-bottom: 1px solid var(--color-border);
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(10px);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
}

.nav-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 4rem;
    gap: 2rem;
}

.logo {
    display: flex;
    align-items: center;
    gap: .5rem;
    font-weight: 600;
    font-size: 1.25rem;
    color: var(--color-text);
    text-decoration: none;
}

.nav {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.nav-link {
    color: var(--color-text-secondary);
    font-weight: 500;
    transition: color .2s ease;
}

.nav-link:hover {
    color: var(--color-accent);
}

/* Article Styles */
.main {
    padding: 2rem 0;
}

.article-container {
    max-width: 800px;
    margin: 0 auto;
}

.article-header {
    margin-bottom: 2rem;
    text-align: center;
}

.article-meta {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--color-text-secondary);
}

.article-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    line-height: 1.2;
    color: var(--color-text);
}

.article-description {
    font-size: 1.25rem;
    color: var(--color-text-secondary);
    line-height: 1.5;
}

.article-content {
    font-size: 1.1rem;
    line-height: 1.7;
}

.article-content h2 {
    font-size: 1.8rem;
    margin: 2rem 0 1rem;
    color: var(--color-text);
}

.article-content h3 {
    font-size: 1.4rem;
    margin: 1.5rem 0 0.5rem;
    color: var(--color-text);
}

.article-content p {
    margin-bottom: 1.5rem;
}

.article-content ul, .article-content ol {
    margin-bottom: 1.5rem;
    padding-left: 2rem;
}

.article-content li {
    margin-bottom: 0.5rem;
}

.article-content strong {
    color: var(--color-text);
    font-weight: 600;
}

/* Image Styles */
.article-hero picture img,
.post-image picture img,
.related-image picture img,
.article-image picture img {
    width: 100% !important;
    height: auto !important;
    object-fit: cover !important;
    border-radius: 0.5rem;
}

.article-hero picture img {
    height: 400px !important;
}

.post-image picture img {
    height: 200px !important;
}

.related-image picture img {
    height: 150px !important;
    transition: transform 0.3s ease;
}

/* Social Share Styles */
.social-share {
    margin: 2rem 0;
    padding: 1.5rem;
    background: var(--color-bg-secondary);
    border-radius: .5rem;
    border: 1px solid var(--color-border);
}

.share-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--color-text);
}

.share-buttons {
    display: flex;
    gap: .75rem;
    flex-wrap: wrap;
}

.share-button {
    display: inline-flex;
    align-items: center;
    gap: .5rem;
    padding: .5rem 1rem;
    border-radius: .375rem;
    font-size: .875rem;
    font-weight: 500;
    text-decoration: none;
    transition: all .2s ease;
    border: 1px solid transparent;
}

.share-button:hover {
    transform: translateY(-1px);
}

.twitter {
    background: #1da1f2;
    color: #fff;
}

.twitter:hover {
    background: #1a91da;
}

.linkedin {
    background: #0077b5;
    color: #fff;
}

.linkedin:hover {
    background: #006396;
}

/* Related Posts Styles */
.related-posts {
    margin: 3rem 0;
    padding: 2rem;
    background: var(--color-bg-secondary);
    border-radius: 1rem;
    border: 1px solid var(--color-border);
}

.related-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    color: var(--color-text);
    text-align: center;
}

.related-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.related-card {
    background: var(--color-bg);
    border: 1px solid var(--color-border);
    border-radius: .75rem;
    overflow: hidden;
    transition: all .3s ease;
}

.related-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.related-content {
    padding: 1.25rem;
}

.related-meta {
    display: flex;
    align-items: center;
    gap: .75rem;
    font-size: .875rem;
    color: var(--color-text-secondary);
    margin-bottom: .5rem;
}

.related-tag {
    color: var(--color-accent);
    font-weight: 500;
}

.related-post-title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: .5rem;
    line-height: 1.4;
}

.related-post-title a {
    color: var(--color-text);
    text-decoration: none;
}

.related-post-title a:hover {
    color: var(--color-accent);
}

.related-description {
    font-size: .9rem;
    color: var(--color-text-secondary);
    line-height: 1.5;
    margin-bottom: 1rem;
}

.read-more {
    display: inline-flex;
    align-items: center;
    gap: .25rem;
    color: var(--color-accent);
    text-decoration: none;
    font-weight: 500;
    font-size: .9rem;
}

.read-more:hover {
    text-decoration: underline;
}

/* Footer Styles */
.footer {
    background: var(--color-bg-secondary);
    border-top: 1px solid var(--color-border);
    margin-top: 4rem;
}

.footer-content {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 2rem;
    margin-bottom: 2rem;
    padding: 3rem 1rem 2rem;
}

.footer-title {
    color: var(--color-text);
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: .5rem;
}

.footer-description {
    color: var(--color-text-secondary);
    line-height: 1.6;
}

.footer-links {
    list-style: none;
}

.footer-links li {
    margin-bottom: .5rem;
}

.footer-links a {
    color: var(--color-text-secondary);
    transition: color .2s ease;
}

.footer-links a:hover {
    color: var(--color-accent);
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2rem 1rem;
    border-top: 1px solid var(--color-border);
    color: var(--color-text-secondary);
    font-size: .9rem;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .article-title {
        font-size: 2rem;
    }
    
    .article-description {
        font-size: 1.1rem;
    }
    
    .nav-wrapper {
        gap: 1rem;
    }
    
    .nav {
        gap: 1rem;
    }
    
    .footer-content {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
    
    .footer-bottom {
        flex-direction: column;
        gap: .5rem;
        text-align: center;
    }
    
    .article-hero picture img {
        height: 250px !important;
    }
    
    .related-image picture img {
        height: 120px !important;
    }
}
</style>'''

def fix_blog_post_css(file_path):
    """Fix CSS references in a single blog post file."""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has inline CSS (skip if already processed)
        if 'Consolidated Blog Post Styles' in content:
            print(f"  ✓ Already processed: {file_path}")
            return True
        
        # Pattern to match both preload and stylesheet links for the three CSS files
        css_pattern = r'<link\s+rel="preload"\s+href="/_astro/_slug_\.Bf5ABjYN\.css"[^>]*>\s*<link\s+rel="preload"\s+href="/_astro/_slug_\.DEt5kPu5\.css"[^>]*>\s*<link\s+rel="preload"\s+href="/_astro/base\.css"[^>]*>\s*<noscript[^>]*>.*?</noscript>\s*<link\s+rel="stylesheet"\s+href="/_astro/_slug_\.Bf5ABjYN\.css">\s*<link\s+rel="stylesheet"\s+href="/_astro/_slug_\.DEt5kPu5\.css">\s*<link\s+rel="stylesheet"\s+href="/_astro/base\.css">'
        
        # If the complex pattern doesn't match, try simpler patterns
        if not re.search(css_pattern, content, re.DOTALL):
            # Try to match just the stylesheet links
            css_pattern = r'<link\s+rel="stylesheet"\s+href="/_astro/_slug_\.Bf5ABjYN\.css">\s*<link\s+rel="stylesheet"\s+href="/_astro/_slug_\.DEt5kPu5\.css">\s*<link\s+rel="stylesheet"\s+href="/_astro/base\.css">'
        
        # Replace CSS links with inline styles
        updated_content = re.sub(css_pattern, get_inline_css(), content, flags=re.DOTALL)
        
        # If no replacement happened, maybe the pattern is different
        if updated_content == content:
            print(f"  ⚠ No CSS pattern matched in: {file_path}")
            return False
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"  ✓ Fixed CSS references: {file_path}")
        return True
        
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all blog post files."""
    # Get all blog post HTML files (excluding the blog index)
    blog_posts = glob.glob('dist/blog/*/index.html')
    
    print(f"Found {len(blog_posts)} blog post files to process:")
    
    processed = 0
    skipped = 0
    errors = 0
    
    for post_file in blog_posts:
        result = fix_blog_post_css(post_file)
        if result is True:
            processed += 1
        elif result is None:  # Already processed
            skipped += 1
        else:
            errors += 1
    
    print(f"\n📊 Summary:")
    print(f"  ✅ Processed: {processed}")
    print(f"  ⏭  Skipped: {skipped}")
    print(f"  ❌ Errors: {errors}")
    print(f"  📁 Total: {len(blog_posts)}")
    
    if errors == 0:
        print(f"\n🎉 All blog posts now have self-contained CSS!")
    else:
        print(f"\n⚠  Some files had issues. Check the output above.")

if __name__ == "__main__":
    main()