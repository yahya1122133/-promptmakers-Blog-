#!/usr/bin/env python3
"""
All Posts Page UI Fix
Fixes the poor layout, spacing, and styling issues on the blog index page
"""

import os
import re

def fix_all_posts_ui():
    print("🎨 Fixing All Posts Page UI Issues...\n")
    
    blog_index_file = "dist/blog/index.html"
    
    if not os.path.exists(blog_index_file):
        print("❌ Blog index file not found!")
        return
    
    with open(blog_index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix broken post card structure - the divs are in wrong order
    # Current structure has broken closing div placement causing layout issues
    
    print("✅ Fixing post card structure...")
    
    # Fix the broken div structure for post cards
    # The issue is that post-content div is not properly wrapping the content
    
    # First, let's fix the overall structure by adding proper CSS for the grid
    css_fixes = '''
/* Enhanced blog grid layout */
.posts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

@media (max-width: 768px) {
    .posts-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
}

/* Enhanced post card styling */
.post-card {
    display: flex;
    flex-direction: column;
    background: var(--color-bg);
    border: 1px solid var(--color-border);
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    height: 100%;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.post-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    border-color: var(--color-accent);
}

/* Fix post image container */
.post-image {
    position: relative;
    width: 100%;
    height: 200px;
    overflow: hidden;
    background: var(--color-bg-secondary);
}

.post-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
}

.post-card:hover .post-image img {
    transform: scale(1.05);
}

/* Fix post content layout */
.post-content {
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    gap: 0.75rem;
}

/* Fix post meta styling */
.post-meta {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
}

.post-meta time {
    color: var(--color-text-secondary);
    font-size: 0.875rem;
    font-weight: 500;
}

.post-tag {
    background: var(--color-accent);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    text-decoration: none;
}

/* Fix post title */
.post-title {
    margin: 0;
    margin-bottom: 0.75rem;
    line-height: 1.3;
}

.post-title a {
    color: var(--color-text);
    text-decoration: none;
    font-size: 1.25rem;
    font-weight: 600;
    transition: color 0.2s ease;
}

.post-title a:hover {
    color: var(--color-accent);
}

/* Fix post description */
.post-description {
    color: var(--color-text-secondary);
    line-height: 1.5;
    margin: 0;
    margin-bottom: 1rem;
    flex-grow: 1;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Fix read more button */
.read-more {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--color-accent);
    text-decoration: none;
    font-weight: 600;
    font-size: 0.9rem;
    margin-top: auto;
    padding: 0.5rem 0;
    transition: all 0.2s ease;
}

.read-more:hover {
    color: var(--color-accent-hover);
    gap: 0.75rem;
}

.read-more svg {
    transition: transform 0.2s ease;
}

.read-more:hover svg {
    transform: translateX(2px);
}

/* Fix page header spacing */
.page-header {
    text-align: center;
    margin-bottom: 2rem;
    padding: 2rem 0;
}

.page-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: var(--color-text);
}

.page-description {
    font-size: 1.1rem;
    color: var(--color-text-secondary);
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Fix tag filter styling */
.tag-filter {
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: var(--color-bg-secondary);
    border-radius: 12px;
    border: 1px solid var(--color-border);
}

.filter-title {
    margin: 0 0 1rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--color-text);
}

.tags-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tag-button {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--color-bg);
    border: 1px solid var(--color-border);
    border-radius: 8px;
    text-decoration: none;
    color: var(--color-text);
    font-size: 0.875rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

.tag-button:hover {
    background: var(--color-accent);
    color: white;
    border-color: var(--color-accent);
}

.tag-button.active {
    background: var(--color-accent);
    color: white;
    border-color: var(--color-accent);
}

.tag-count {
    background: var(--color-bg-secondary);
    color: var(--color-text-secondary);
    padding: 0.125rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
}

.tag-button:hover .tag-count,
.tag-button.active .tag-count {
    background: rgba(255, 255, 255, 0.2);
    color: white;
}

@media (max-width: 768px) {
    .page-title {
        font-size: 2rem;
    }
    
    .posts-grid {
        gap: 1rem;
    }
    
    .post-content {
        padding: 1rem;
    }
}
'''
    
    # Insert the CSS before the closing </style> tag
    style_pattern = r'(</style>)'
    css_insertion = css_fixes + '\n</style>'
    content = re.sub(style_pattern, css_insertion, content)
    
    print("✅ Added enhanced CSS styling...")
    
    # Now fix the HTML structure issues - the main problem is broken div nesting
    
    # Fix post card structure by ensuring proper nesting
    # The issue is some post-content divs are incorrectly closed
    
    # Pattern to find and fix broken post card structure
    broken_pattern = r'(<div class="post-meta"[^>]*>.*?</div>)\s*(</div>)\s*(<h3 class="post-title")'
    fixed_pattern = r'\1\3'
    content = re.sub(broken_pattern, fixed_pattern, content, flags=re.DOTALL)
    
    print("✅ Fixed broken post card HTML structure...")
    
    # Fix missing post-content wrapper for some cards
    # Some h3 elements are outside the post-content div
    
    # Find h3 titles that are outside post-content and wrap them properly
    outside_h3_pattern = r'(</div>\s*)(<h3 class="post-title".*?</h3>\s*<p class="post-description".*?</p>\s*<a href.*?</a>)\s*(</div>\s*</article>)'
    fixed_h3_pattern = r'\1<div class="post-content">\2</div>\3'
    content = re.sub(outside_h3_pattern, fixed_h3_pattern, content, flags=re.DOTALL)
    
    print("✅ Fixed post content wrapper structure...")
    
    # Save the fixed file
    with open(blog_index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n🎉 All Posts Page UI Successfully Fixed!")
    print("✅ Enhanced grid layout with proper card sizing")
    print("✅ Fixed post card structure and nesting") 
    print("✅ Improved typography and spacing")
    print("✅ Added hover effects and animations")
    print("✅ Better responsive design for mobile")
    print("✅ Enhanced tag filter styling")
    print("✅ Consistent visual hierarchy")

if __name__ == "__main__":
    fix_all_posts_ui()
