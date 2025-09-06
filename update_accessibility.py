#!/usr/bin/env python3
import re
import os

def update_read_more_links():
    """Update Read More links in the homepage to be more accessible"""
    
    # Read the HTML file
    index_path = "c:/Users/Yahya/Downloads/promptmakers-blog-dist/dist/index.html"
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract article titles and their corresponding links
    article_data = [
        ("Advanced Prompt Engineering Techniques: Beyond the Basics", "/blog/advanced-prompt-engineering-techniques"),
        ("5 Hacks for Insanely Good AI Prompts (That Actually Work)", "/blog/5-hacks-insanely-good-ai-prompts"),
        ("Prompt Engineering 101: The Complete Beginner's Guide to Talking to AI", "/blog/prompt-engineering-101-basics"),
        ("The CLEAR Framework: Your Blueprint for Crafting Effective AI Prompts", "/blog/clear-framework-effective-prompts"),
        ("Mastering Prompt Templates: How to Build Reusable AI Workflows", "/blog/mastering-prompt-templates"),
        ("ChatGPT vs Gemini vs Claude: The Ultimate AI Model Comparison for Prompt Engineers", "/blog/chatgpt-vs-gemini-vs-claude")
    ]
    
    # Update each Read More link
    for title, slug in article_data:
        # Pattern to find the specific read more link
        pattern = rf'<a href="{slug}" class="read-more"([^>]*?)>\s*Read More\s*(<svg.*?</svg>)\s*</a>'
        
        # Replacement with accessibility improvements
        replacement = f'<a href="{slug}" class="read-more" aria-label="Read full article: {title}"\\1>\nRead More\n<span class="sr-only">: {title}</span>\n\\2\n</a>'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write the updated content back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated homepage Read More links")

def update_blog_index_links():
    """Update Read Full Article links in the blog index to be more accessible"""
    
    # Read the blog index HTML file
    blog_index_path = "c:/Users/Yahya/Downloads/promptmakers-blog-dist/dist/blog/index.html"
    with open(blog_index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract article titles and their corresponding links
    article_data = [
        ("Advanced Prompt Engineering Techniques: Beyond the Basics", "/blog/advanced-prompt-engineering-techniques"),
        ("5 Hacks for Insanely Good AI Prompts (That Actually Work)", "/blog/5-hacks-insanely-good-ai-prompts"),
        ("Prompt Engineering 101: The Complete Beginner's Guide to Talking to AI", "/blog/prompt-engineering-101-basics"),
        ("The CLEAR Framework: Your Blueprint for Crafting Effective AI Prompts", "/blog/clear-framework-effective-prompts"),
        ("Mastering Prompt Templates: How to Build Reusable AI Workflows", "/blog/mastering-prompt-templates"),
        ("ChatGPT vs Gemini vs Claude: The Ultimate AI Model Comparison for Prompt Engineers", "/blog/chatgpt-vs-gemini-vs-claude")
    ]
    
    # Update each Read Full Article link
    for title, slug in article_data:
        # Pattern to find the specific read more link
        pattern = rf'<a href="{slug}" class="read-more"([^>]*?)>\s*Read Full Article\s*(<svg.*?</svg>)\s*</a>'
        
        # Replacement with accessibility improvements
        replacement = f'<a href="{slug}" class="read-more" aria-label="Read full article: {title}"\\1>\nRead Full Article\n<span class="sr-only">: {title}</span>\n\\2\n</a>'
        
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write the updated content back
    with open(blog_index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated blog index Read Full Article links")

def update_related_posts_links():
    """Update Read More links in related posts sections on individual blog pages"""
    
    # Define the article data
    article_data = [
        ("Advanced Prompt Engineering Techniques: Beyond the Basics", "/blog/advanced-prompt-engineering-techniques"),
        ("5 Hacks for Insanely Good AI Prompts (That Actually Work)", "/blog/5-hacks-insanely-good-ai-prompts"),
        ("Prompt Engineering 101: The Complete Beginner's Guide to Talking to AI", "/blog/prompt-engineering-101-basics"),
        ("The CLEAR Framework: Your Blueprint for Crafting Effective AI Prompts", "/blog/clear-framework-effective-prompts"),
        ("Mastering Prompt Templates: How to Build Reusable AI Workflows", "/blog/mastering-prompt-templates"),
        ("ChatGPT vs Gemini vs Claude: The Ultimate AI Model Comparison for Prompt Engineers", "/blog/chatgpt-vs-gemini-vs-claude")
    ]
    
    # Find all HTML files in the blog directory
    blog_dir = "c:/Users/Yahya/Downloads/promptmakers-blog-dist/dist/blog"
    import glob
    html_files = glob.glob(f"{blog_dir}/**/index.html", recursive=True)
    
    for html_file in html_files:
        if html_file.endswith("blog/index.html"):
            continue  # Skip the main blog index, already handled
            
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update each related post Read Article link
        for title, slug in article_data:
            # Pattern for related posts (using data-astro-cid-dpgbfi7r)
            pattern = rf'<a href="{slug}" class="read-more" data-astro-cid-dpgbfi7r>\s*Read Article\s*(<svg.*?</svg>)\s*</a>'
            
            # Replacement with accessibility improvements
            replacement = f'<a href="{slug}" class="read-more" aria-label="Read full article: {title}" data-astro-cid-dpgbfi7r>\nRead Article\n<span class="sr-only">: {title}</span>\n\\1\n</a>'
            
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Only write if content changed
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated related posts links in {html_file}")

if __name__ == "__main__":
    update_read_more_links()
    update_blog_index_links()
    update_related_posts_links()
    print("All Read More/Read Full Article links have been updated for accessibility!")
