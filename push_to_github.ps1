# GitHub Push Helper Script
# This script will help you push your code to GitHub

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host "=" * 59 -ForegroundColor Cyan
Write-Host "GitHub Push Helper" -ForegroundColor Green
Write-Host "=" * 60 -ForegroundColor Cyan

Write-Host "`nCurrent Git Status:" -ForegroundColor Yellow
git log --oneline -n 3

Write-Host "`n"
Write-Host "To push to GitHub, you need to:" -ForegroundColor Yellow
Write-Host "1. Create a repository on GitHub (https://github.com/new)" -ForegroundColor White
Write-Host "   - Name: ai-pathfinder" -ForegroundColor White
Write-Host "   - Public repository" -ForegroundColor White
Write-Host "   - Don't initialize with README" -ForegroundColor White
Write-Host "`n2. Copy the repository URL" -ForegroundColor White
Write-Host "`n"

$repoUrl = Read-Host "Enter your GitHub repository URL (e.g., https://github.com/username/ai-pathfinder.git)"

if ($repoUrl) {
    Write-Host "`nSetting up remote..." -ForegroundColor Yellow
    git remote add origin $repoUrl
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Remote added successfully!" -ForegroundColor Green
        
        Write-Host "`nRenaming branch to main..." -ForegroundColor Yellow
        git branch -M main
        
        Write-Host "`nPushing to GitHub..." -ForegroundColor Yellow
        git push -u origin main
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "`n" -NoNewline
            Write-Host "=" * 60 -ForegroundColor Green
            Write-Host "SUCCESS! Your code is now on GitHub!" -ForegroundColor Green
            Write-Host "=" * 60 -ForegroundColor Green
            Write-Host "`nView your repository at:" -ForegroundColor Yellow
            Write-Host $repoUrl.Replace(".git", "") -ForegroundColor Cyan
        } else {
            Write-Host "`nPush failed. You may need to authenticate with GitHub." -ForegroundColor Red
            Write-Host "Try running: git push -u origin main" -ForegroundColor Yellow
        }
    } else {
        Write-Host "`nRemote already exists or error occurred." -ForegroundColor Red
        Write-Host "If remote exists, run: git push -u origin main" -ForegroundColor Yellow
    }
} else {
    Write-Host "`nNo URL provided. Please create a GitHub repository first." -ForegroundColor Red
    Write-Host "Visit: https://github.com/new" -ForegroundColor Cyan
}

Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
