#!/usr/bin/env python3
"""
Script to optimize CSS loading for better First Contentful Paint (FCP)
- Inlines critical CSS (above-the-fold styles)
- Defers non-critical CSS with media="print" trick
- Adds preload hints for better performance
"""

import os
import re
import glob

def get_critical_css():
    """Define critical CSS that should be inlined for immediate rendering"""
    return """
<style>
/* Critical CSS - Inlined for FCP optimization */
:root {
    --color-bg: #ffffff;
    --color-text: #1a202c;
    --color-text-secondary: #4a5568;
    --color-accent: #3b82f6;
    --color-accent-hover: #2563eb;
    --color-border: #e2e8f0;
    --color-bg-secondary: #f8fafc;
}

[data-theme="dark"] {
    --color-bg: #1a202c;
    --color-text: #f7fafc;
    --color-text-secondary: #a0aec0;
    --color-border: #2d3748;
    --color-bg-secondary: #2d3748;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: var(--color-text);
    background: var(--color-bg);
}

/* Critical layout styles */
.header { position: sticky; top: 0; z-index: 50; background: var(--color-bg); border-bottom: 1px solid var(--color-border); }
.container { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }
.main { min-height: calc(100vh - 4rem); }

/* Critical image styles - prevent layout shift */
.article-hero picture img,
.article-hero[data-astro-cid-4dqtj3le] picture img {
    width: 100% !important;
    height: 400px !important;
    object-fit: cover !important;
    border-radius: 0.5rem;
    display: block;
}

.post-image picture img,
.post-image[data-astro-cid-j7pv25f6] picture img {
    width: 100% !important;
    height: 200px !important;
    object-fit: cover !important;
    display: block;
}

/* Mobile responsive adjustments */
@media (max-width: 768px) {
    .article-hero picture img,
    .article-hero[data-astro-cid-4dqtj3le] picture img {
        height: 250px !important;
    }
}

/* Prevent invisible text during font swap */
.logo-text, .article-title, h1, h2, h3 {
    font-display: swap;
}
</style>
"""

def optimize_html_file(file_path):
    """Optimize a single HTML file for critical CSS rendering"""
    print(f"Optimizing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the CSS links
    css_pattern = r'<link rel="stylesheet" href="([^"]+)">'
    css_links = re.findall(css_pattern, content)
    
    if not css_links:
        print(f"  No CSS links found in {file_path}")
        return
    
    # Get critical CSS
    critical_css = get_critical_css()
    
    # Build optimized CSS loading
    optimized_css = critical_css + "\n"
    
    # Add preload hints for CSS files
    for css_href in css_links:
        optimized_css += f'<link rel="preload" href="{css_href}" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n'
    
    # Add noscript fallback
    optimized_css += "<noscript>\n"
    for css_href in css_links:
        optimized_css += f'<link rel="stylesheet" href="{css_href}">\n'
    optimized_css += "</noscript>\n"
    
    # Add the loadCSS polyfill for better browser support
    optimized_css += """
<script>
/*! loadCSS. [c]2017 Filament Group, Inc. MIT License */
!function(a){"use strict";var b=function(b,c,d){function e(a){return h.body?a():void setTimeout(function(){e(a)})}function f(){i.addEventListener&&i.removeEventListener("load",f),i.media=d||"all"}var g,h=a.document,i=h.createElement("link");if(c)g=c;else{var j=(h.body||h.getElementsByTagName("head")[0]).childNodes;g=j[j.length-1]}var k=h.styleSheets;i.rel="stylesheet",i.href=b,i.media="only x",e(function(){g.parentNode.insertBefore(i,c?g:g.nextSibling)});var l=function(a){for(var b=i.href,c=k.length;c--;)if(k[c].href===b)return a();setTimeout(function(){l(a)})};return i.addEventListener&&i.addEventListener("load",f),i.onloadcssdefined=l,l(f),i};"undefined"!=typeof exports?exports.loadCSS=b:a.loadCSS=b}("undefined"!=typeof global?global:this);
</script>
"""
    
    # Replace the original CSS links with optimized version
    # Remove original CSS links
    for css_href in css_links:
        content = content.replace(f'<link rel="stylesheet" href="{css_href}">', '')
    
    # Insert optimized CSS before </head>
    content = content.replace('</head>', optimized_css + '</head>')
    
    # Write back the optimized content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✅ Optimized CSS loading in {file_path}")

def main():
    """Main function to optimize all HTML files"""
    print("🚀 Optimizing Critical CSS for First Contentful Paint...")
    
    # Find all HTML files in dist directory
    html_files = glob.glob("dist/**/*.html", recursive=True)
    
    if not html_files:
        print("❌ No HTML files found in dist directory")
        return
    
    print(f"📁 Found {len(html_files)} HTML files to optimize")
    
    for html_file in html_files:
        try:
            optimize_html_file(html_file)
        except Exception as e:
            print(f"❌ Error optimizing {html_file}: {e}")
    
    print("✅ Critical CSS optimization complete!")
    print("\n🎯 Benefits:")
    print("   • Faster First Contentful Paint (FCP)")
    print("   • Reduced render-blocking resources")
    print("   • Better Core Web Vitals scores")
    print("   • Improved user experience")

if __name__ == "__main__":
    main()
