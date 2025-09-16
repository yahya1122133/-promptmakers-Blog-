#!/usr/bin/env python3

import os
import re
from pathlib import Path

def update_favicon_in_file(file_path):
    """Update favicon declarations in an HTML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Multiple patterns to catch different favicon formats
        patterns = [
            r'    <link rel="icon" type="image/png" href="/images/favicon\.icon\.png">',
            r'<link rel="icon" type="image/png" href="/images/favicon\.icon\.png">',
            r'<link rel="icon"[^>]*href="/images/favicon\.icon\.png"[^>]*>'
        ]
        
        # New favicon declarations for spaced HTML
        new_favicon_spaced = """    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.icon.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon.icon.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/favicon.icon.png">
    <link rel="manifest" href="/site.webmanifest">"""
        
        # New favicon declarations for minified HTML
        new_favicon_minified = '<link rel="icon" type="image/x-icon" href="/favicon.ico"><link rel="icon" type="image/png" sizes="32x32" href="/images/favicon.icon.png"><link rel="icon" type="image/png" sizes="16x16" href="/images/favicon.icon.png"><link rel="apple-touch-icon" sizes="180x180" href="/images/favicon.icon.png"><link rel="manifest" href="/site.webmanifest">'
        
        updated = False
        for i, pattern in enumerate(patterns):
            if re.search(pattern, content):
                # Use appropriate replacement based on file structure
                replacement = new_favicon_spaced if i == 0 else new_favicon_minified
                updated_content = re.sub(pattern, replacement, content)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ Updated favicon in: {file_path}")
                updated = True
                break
        
        if not updated:
            print(f"⚠️  No favicon pattern found in: {file_path}")
            return False
        return True
            
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Update favicon declarations in all HTML files."""
    dist_dir = Path("c:/Users/Yahya/Downloads/promptmakers-blog-dist/dist")
    
    if not dist_dir.exists():
        print(f"❌ Directory not found: {dist_dir}")
        return
    
    # Find all HTML files
    html_files = list(dist_dir.rglob("*.html"))
    
    print(f"🔍 Found {len(html_files)} HTML files")
    print("=" * 50)
    
    updated_count = 0
    for html_file in html_files:
        if update_favicon_in_file(html_file):
            updated_count += 1
    
    print("=" * 50)
    print(f"✅ Updated {updated_count} files with proper favicon declarations")
    print("\nFavicon improvements made:")
    print("• Added standard favicon.ico reference")
    print("• Added multiple PNG sizes (16x16, 32x32)")
    print("• Added Apple touch icon support")
    print("• Added web manifest reference")
    print("\nThis should fix the favicon display issue in Google search results!")

if __name__ == "__main__":
    main()