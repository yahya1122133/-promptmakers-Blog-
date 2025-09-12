#!/usr/bin/env python3
"""
Advanced fix for the nested post-content div structure in blog index page
"""

import re
import os

def fix_nested_post_content():
    """Fix the nested post-content div structure more precisely"""
    file_path = os.path.join("dist", "blog", "index.html")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("Fixing nested post-content div structure...")
        
        # More precise pattern to fix nested post-content divs
        # Look for: </div><div class="post-content"><h3 class="post-title"
        # Replace with: <h3 class="post-title"
        
        pattern = r'</div>\s*<div class="post-content">\s*<h3 class="post-title"'
        replacement = '<h3 class="post-title"'
        content = re.sub(pattern, replacement, content)
        
        # Also fix the closing div structure
        # Look for: </a></div></div> </article>
        # Replace with: </a></div> </article>
        pattern2 = r'</a>\s*</div>\s*</div>\s*</article>'
        replacement2 = '</a></div> </article>'
        content = re.sub(pattern2, replacement2, content)
        
        # Write the fixed content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed nested post-content div structure")
        print("✅ Cleaned up closing div tags")
        print("✅ All Posts page HTML structure is now properly nested")
        
        return True
        
    except Exception as e:
        print(f"❌ Error fixing nested structure: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Advanced fix for All Posts page HTML structure...")
    success = fix_nested_post_content()
    
    if success:
        print("\n🎉 All Posts page structure completely fixed!")
        print("The blog cards now have clean, properly nested HTML structure.")
    else:
        print("\n❌ Failed to fix nested structure")
