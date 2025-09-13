#!/bin/bash

# Promptmakers Blog - Deployment Script
# Usage: ./deploy.sh [platform]
# Platforms: netlify, vercel, github

echo "🚀 Promptmakers Blog Deployment Script"
echo "======================================"

PLATFORM=${1:-netlify}
DIST_DIR="dist"

# Check if dist directory exists
if [ ! -d "$DIST_DIR" ]; then
    echo "❌ Error: dist directory not found!"
    echo "Please run this script from the project root."
    exit 1
fi

echo "📦 Deployment package ready:"
echo "   Files: $(find $DIST_DIR -type f | wc -l)"
echo "   Size: $(du -sh $DIST_DIR | cut -f1)"

case $PLATFORM in
    "netlify")
        echo ""
        echo "🌐 NETLIFY DEPLOYMENT"
        echo "===================="
        echo "Option 1 - Drag & Drop (Fastest):"
        echo "  1. Open: https://netlify.com/drop"
        echo "  2. Drag the 'dist' folder to the browser"
        echo "  3. Set custom domain: blog.promptmakers.app"
        echo ""
        echo "Option 2 - CLI:"
        echo "  npm install -g netlify-cli"
        echo "  netlify deploy --prod --dir=dist"
        ;;
    
    "vercel")
        echo ""
        echo "▲ VERCEL DEPLOYMENT"
        echo "=================="
        echo "1. Install Vercel CLI:"
        echo "   npm install -g vercel"
        echo ""
        echo "2. Deploy:"
        echo "   cd dist && vercel --prod"
        ;;
    
    "github")
        echo ""
        echo "🐙 GITHUB PAGES DEPLOYMENT"
        echo "========================="
        echo "1. Create gh-pages branch:"
        echo "   git checkout -b gh-pages"
        echo "   git add dist/*"
        echo "   git commit -m 'Deploy to GitHub Pages'"
        echo "   git push origin gh-pages"
        echo ""
        echo "2. Enable Pages in repository settings"
        ;;
    
    *)
        echo "❌ Unknown platform: $PLATFORM"
        echo "Available platforms: netlify, vercel, github"
        exit 1
        ;;
esac

echo ""
echo "📋 Post-Deployment Checklist:"
echo "  □ Set custom domain: blog.promptmakers.app"
echo "  □ Enable SSL certificate"
echo "  □ Submit sitemap to Google Search Console"
echo "  □ Test search functionality"
echo "  □ Verify analytics tracking"
echo ""
echo "🎉 Ready for deployment!"