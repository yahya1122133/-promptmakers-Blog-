#!/usr/bin/env python3
"""
Fix Search Script Issues
=======================
Removes search script from individual blog posts where it's not needed
and causes console errors.
"""

import os
import re
from pathlib import Path

def fix_search_script_references():
    """Remove search script from individual blog posts"""
    
    print("🔧 Fixing search script references...")
    
    # Find all individual blog post index.html files
    blog_posts = []
    dist_path = Path("dist/blog")
    
    for item in dist_path.iterdir():
        if item.is_dir() and item.name != "index.html":
            post_index = item / "index.html"
            if post_index.exists():
                blog_posts.append(post_index)
    
    fixed_count = 0
    
    for post_file in blog_posts:
        try:
            # Read the file
            with open(post_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if it contains the search script
            if 'Search.astro_astro_type_script_index_0_lang.CsPf_NSL.js' in content:
                print(f"  Fixing: {post_file}")
                
                # Remove the search script tag from individual blog posts
                # They don't have search functionality, only homepage and blog index do
                content = re.sub(
                    r'\s*<script[^>]*Search\.astro_astro_type_script_index_0_lang\.CsPf_NSL\.js[^>]*></script>',
                    '',
                    content
                )
                
                # Write back the fixed content
                with open(post_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_count += 1
        
        except Exception as e:
            print(f"  ❌ Error fixing {post_file}: {e}")
    
    print(f"✅ Fixed {fixed_count} blog posts")
    return fixed_count

def main():
    """Main function"""
    print("🚀 Starting search script fixes...")
    
    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    fixed = fix_search_script_references()
    
    print(f"\n✅ Search script fixes completed!")
    print(f"   Fixed {fixed} individual blog posts")
    print(f"   Search functionality preserved on homepage and blog index")

if __name__ == "__main__":
    main()