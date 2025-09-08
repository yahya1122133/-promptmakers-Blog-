#!/usr/bin/env python3
"""
Script to optimize Google Fonts loading for better performance
- Convert blocking font CSS to preload strategy
- Add font-display: swap for better text rendering
- Implement async font loading with fallbacks
"""

import os
import re
import glob

def optimize_font_loading(file_path):
    """Optimize Google Fonts loading in a single HTML file"""
    print(f"Optimizing fonts in: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find Google Fonts links
    google_fonts_pattern = r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet">'
    google_fonts_links = re.findall(google_fonts_pattern, content)
    
    if not google_fonts_links:
        print(f"  No Google Fonts found in {file_path}")
        return
    
    # Extract the font URL
    font_url_pattern = r'href="(https://fonts\.googleapis\.com/css2\?[^"]+)"'
    font_urls = re.findall(font_url_pattern, content)
    
    if not font_urls:
        print(f"  Could not extract font URLs from {file_path}")
        return
    
    font_url = font_urls[0]  # Use the first font URL found
    
    # Create optimized font loading
    optimized_fonts = f'''<!-- Optimized Font Loading -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="{font_url}" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="{font_url}"></noscript>
<script>
  // Optimized font loading with fallback
  (function() {{
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = '{font_url}';
    link.media = 'print';
    link.onload = function() {{ this.media = 'all'; }};
    document.head.appendChild(link);
  }})();
</script>'''
    
    # Remove existing Google Fonts references
    # Remove preconnect links
    content = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com"[^>]*>', '', content)
    content = re.sub(r'<link rel="preconnect" href="https://fonts\.gstatic\.com"[^>]*>', '', content)
    
    # Remove the main font stylesheet
    for font_link in google_fonts_links:
        content = content.replace(font_link, '')
    
    # Insert optimized font loading before <!-- Structured Data -->
    if '<!-- Structured Data -->' in content:
        content = content.replace('<!-- Structured Data -->', optimized_fonts + '\n<!-- Structured Data -->')
    else:
        # If no structured data comment, insert before </head>
        content = content.replace('</head>', optimized_fonts + '\n</head>')
    
    # Update the critical CSS to include font-display properties
    if 'font-family: Inter,' in content:
        # Add font-display: swap to critical CSS
        font_display_css = '''
/* Optimized font loading */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 300 700;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/inter/v13/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyeMZhrib2Bg-4.woff2) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2202, U+2206, U+220F, U+2211, U+2212, U+2215, U+FEFF, U+FFFD;
}'''
        
        # Insert font face after the existing critical CSS
        content = content.replace('/* Prevent invisible text during font swap */', 
                                font_display_css + '\n\n/* Prevent invisible text during font swap */')
    
    # Write back the optimized content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Optimized font loading in {file_path}")

def main():
    """Main function to optimize font loading in all HTML files"""
    print("🔤 Optimizing Google Fonts loading for better performance...")
    
    # Find all HTML files in dist directory
    html_files = glob.glob("dist/**/*.html", recursive=True)
    
    if not html_files:
        print("❌ No HTML files found in dist directory")
        return
    
    print(f"📁 Found {len(html_files)} HTML files to optimize")
    
    for html_file in html_files:
        try:
            optimize_font_loading(html_file)
        except Exception as e:
            print(f"❌ Error optimizing {html_file}: {e}")
    
    print("✅ Font loading optimization complete!")
    print("\n🎯 Benefits:")
    print("   • Eliminates render-blocking font requests")
    print("   • Faster First Contentful Paint (FCP)")
    print("   • Better font loading performance")
    print("   • Prevents invisible text during font load")
    print("   • Maintains text visibility with font-display: swap")

if __name__ == "__main__":
    main()
