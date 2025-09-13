#!/usr/bin/env python3
"""
Fix Twitter Card images to use correct local images and domains
"""

import os
import re

def fix_twitter_images():
    """Fix Twitter card image references"""
    
    # Define the correct image mappings for each post
    image_mappings = {
        'prompt-engineering-101-basics': 'prompt-engineering-basics.jpg',
        'clear-framework-effective-prompts': 'clear-framework.jpg', 
        'chatgpt-vs-gemini-vs-claude': 'ai-model-comparison.jpg',
        '5-hacks-insanely-good-ai-prompts': 'ai-prompts-hero.jpg',
        'mastering-prompt-templates': 'prompt-templates.jpg',
        'ai-agents-ultimate-guide': 'ai-agents-guide.jpg',
        'advanced-prompt-engineering-techniques': 'og-advanced-prompt-techniques.jpg'
    }
    
    # Fix each blog post
    for post_name, correct_image in image_mappings.items():
        file_path = f"dist/blog/{post_name}/index.html"
        
        if os.path.exists(file_path):
            print(f"Fixing Twitter images for: {post_name}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix domain from promptmakers.app to blog.promptmakers.app
            content = re.sub(
                r'content="https://promptmakers\.app/images/([^"]+)"',
                r'content="https://blog.promptmakers.app/images/\1"',
                content
            )
            
            # Fix the specific image filename for this post
            content = re.sub(
                r'(twitter:image[^>]+content="https://blog\.promptmakers\.app/images/)[^"]+(")',
                rf'\1{correct_image}\2',
                content
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"  ✓ Updated Twitter image to: {correct_image}")
    
    print("\n✅ Twitter card images fixed!")

if __name__ == "__main__":
    fix_twitter_images()