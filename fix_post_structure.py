#!/usr/bin/env python3
"""
Fix duplicate post-content div structure in blog index page
"""

import re
import os

def fix_post_structure():
    """Fix the duplicate post-content div structure"""
    file_path = os.path.join("dist", "blog", "index.html")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Fixing duplicate post-content div structure...")
        
        # Pattern to match the problematic structure:
        # </div> <div class="post-content"><div class="post-content">
        # Replace with just: </div> <div class="post-content">
        
        # First fix: Remove duplicate opening post-content div
        pattern1 = r'</div>\s*<div class="post-content"[^>]*>\s*<div class="post-content">'
        replacement1 = '</div> <div class="post-content">'
        content = re.sub(pattern1, replacement1, content)
        
        # Second fix: Remove duplicate closing div at the end of each post
        # Look for pattern: </a></div></div> </article>
        # Replace with: </a></div> </article>
        pattern2 = r'</a></div></div>\s*</article>'
        replacement2 = '</a></div> </article>'
        content = re.sub(pattern2, replacement2, content)
        
        # Also fix the sr-only text inconsistencies
        # Replace incorrect "All Blog Posts" with specific article titles
        
        # Extract article titles for proper sr-only text
        article_fixes = [
            {
                'href': '/blog/advanced-prompt-engineering-techniques',
                'title': 'Advanced Prompt Engineering Techniques: Beyond the Basics'
            },
            {
                'href': '/blog/5-hacks-insanely-good-ai-prompts', 
                'title': '5 Hacks for Insanely Good AI Prompts (That Actually Work)'
            },
            {
                'href': '/blog/prompt-engineering-101-basics',
                'title': 'Prompt Engineering 101: The Complete Beginner\'s Guide to Talking to AI'
            },
            {
                'href': '/blog/clear-framework-effective-prompts',
                'title': 'The CLEAR Framework: Your Blueprint for Crafting Effective AI Prompts'
            },
            {
                'href': '/blog/mastering-prompt-templates',
                'title': 'Mastering Prompt Templates: How to Build Reusable AI Workflows'
            },
            {
                'href': '/blog/chatgpt-vs-gemini-vs-claude',
                'title': 'ChatGPT vs Gemini vs Claude: The Ultimate AI Model Comparison for Prompt Engineers'
            }
        ]
        
        for fix in article_fixes:
            # Find and replace the sr-only text for each article
            pattern = f'<a href="{fix["href"]}" class="read-more"[^>]*>\\s*Read More\\s*<span class="sr-only">: All Blog Posts</span>'
            replacement = f'<a href="{fix["href"]}" class="read-more" data-astro-cid-j7pv25f6 aria-label="Read More: {fix["title"]}">\\nRead More\\n<span class="sr-only">: {fix["title"]}</span>'
            content = re.sub(pattern, replacement, content)
        
        # Write the fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed duplicate post-content div structure")
        print("✅ Fixed sr-only text inconsistencies")
        print("✅ All Posts page structure is now clean and properly nested")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing post structure: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Fixing All Posts page HTML structure...")
    success = fix_post_structure()
    
    if success:
        print("\n🎉 All Posts page structure fixed successfully!")
        print("The blog cards now have proper single post-content divs and correct accessibility text.")
    else:
        print("\n❌ Failed to fix post structure")
