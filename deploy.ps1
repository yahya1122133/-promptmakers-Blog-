# Promptmakers Blog - Windows Deployment Script
# Usage: .\deploy.ps1 [platform]
# Platforms: netlify, vercel, github

param(
    [string]$Platform = "netlify"
)

Write-Host "🚀 Promptmakers Blog Deployment Script" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green

$DistDir = "dist"

# Check if dist directory exists
if (-not (Test-Path $DistDir)) {
    Write-Host "❌ Error: dist directory not found!" -ForegroundColor Red
    Write-Host "Please run this script from the project root." -ForegroundColor Red
    exit 1
}

$FileCount = (Get-ChildItem -Path $DistDir -Recurse -File).Count
$DirSize = [math]::Round((Get-ChildItem -Path $DistDir -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB, 2)

Write-Host ""
Write-Host "📦 Deployment package ready:" -ForegroundColor Cyan
Write-Host "   Files: $FileCount" -ForegroundColor White
Write-Host "   Size: $DirSize MB" -ForegroundColor White

switch ($Platform.ToLower()) {
    "netlify" {
        Write-Host ""
        Write-Host "🌐 NETLIFY DEPLOYMENT" -ForegroundColor Magenta
        Write-Host "===================="
        Write-Host "Option 1 - Drag & Drop (Fastest):" -ForegroundColor Yellow
        Write-Host "  1. Open: https://netlify.com/drop" -ForegroundColor White
        Write-Host "  2. Drag the 'dist' folder to the browser" -ForegroundColor White
        Write-Host "  3. Set custom domain: blog.promptmakers.app" -ForegroundColor White
        Write-Host ""
        Write-Host "Option 2 - CLI:" -ForegroundColor Yellow
        Write-Host "  npm install -g netlify-cli" -ForegroundColor Gray
        Write-Host "  netlify deploy --prod --dir=dist" -ForegroundColor Gray
        
        # Open Netlify in browser
        Write-Host ""
        $answer = Read-Host "Open Netlify deploy page now? (y/n)"
        if ($answer -eq 'y' -or $answer -eq 'Y') {
            Start-Process "https://netlify.com/drop"
            Write-Host "✅ Browser opened. Drag the dist folder to deploy!" -ForegroundColor Green
        }
    }
    
    "vercel" {
        Write-Host ""
        Write-Host "▲ VERCEL DEPLOYMENT" -ForegroundColor Blue
        Write-Host "=================="
        Write-Host "1. Install Vercel CLI:" -ForegroundColor Yellow
        Write-Host "   npm install -g vercel" -ForegroundColor Gray
        Write-Host ""
        Write-Host "2. Deploy:" -ForegroundColor Yellow
        Write-Host "   cd dist && vercel --prod" -ForegroundColor Gray
    }
    
    "github" {
        Write-Host ""
        Write-Host "🐙 GITHUB PAGES DEPLOYMENT" -ForegroundColor DarkGreen
        Write-Host "========================="
        Write-Host "1. Create gh-pages branch:" -ForegroundColor Yellow
        Write-Host "   git checkout -b gh-pages" -ForegroundColor Gray
        Write-Host "   git add dist/*" -ForegroundColor Gray
        Write-Host "   git commit -m 'Deploy to GitHub Pages'" -ForegroundColor Gray
        Write-Host "   git push origin gh-pages" -ForegroundColor Gray
        Write-Host ""
        Write-Host "2. Enable Pages in repository settings" -ForegroundColor Yellow
    }
    
    "ftp" {
        Write-Host ""
        Write-Host "📁 FTP DEPLOYMENT" -ForegroundColor DarkYellow
        Write-Host "================"
        Write-Host "1. Connect to your web server via FTP/SFTP" -ForegroundColor Yellow
        Write-Host "2. Upload contents of 'dist' folder to web root" -ForegroundColor Yellow
        Write-Host "3. Ensure proper file permissions (644 for files, 755 for folders)" -ForegroundColor Yellow
    }
    
    default {
        Write-Host "❌ Unknown platform: $Platform" -ForegroundColor Red
        Write-Host "Available platforms: netlify, vercel, github, ftp" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "📋 Post-Deployment Checklist:" -ForegroundColor Cyan
Write-Host "  □ Set custom domain: blog.promptmakers.app" -ForegroundColor White
Write-Host "  □ Enable SSL certificate" -ForegroundColor White
Write-Host "  □ Submit sitemap to Google Search Console" -ForegroundColor White
Write-Host "  □ Test search functionality" -ForegroundColor White
Write-Host "  □ Verify analytics tracking" -ForegroundColor White
Write-Host ""
Write-Host "🎉 Ready for deployment!" -ForegroundColor Green

# Show deployment URLs for quick access
Write-Host ""
Write-Host "🔗 Quick Deploy Links:" -ForegroundColor Cyan
Write-Host "  Netlify Drop: https://netlify.com/drop" -ForegroundColor Blue
Write-Host "  Vercel: https://vercel.com/new" -ForegroundColor Blue
Write-Host "  GitHub Pages: https://github.com/settings/pages" -ForegroundColor Blue