# GitHub Setup Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com/new in your browser
2. Fill in the details:
   - **Repository name**: `ai-pathfinder`
   - **Description**: `AI Pathfinder - Uninformed Search Algorithms Visualizer with Pygame GUI`
   - **Visibility**: Public
   - **DO NOT** check "Initialize this repository with a README"
   - **DO NOT** add .gitignore or license (we already have them)
3. Click **"Create repository"**

## Step 2: Copy the Repository URL

After creating the repository, GitHub will show you setup instructions.
Copy the HTTPS URL that looks like:
```
https://github.com/YOUR_USERNAME/ai-pathfinder.git
```

## Step 3: Run These Commands

Once you have the URL, run these commands in PowerShell:

```powershell
cd "c:\Users\noorf\Downloads\artificial intelligence\ai_pathfinder"

# Add the remote (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ai-pathfinder.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Alternative: If You Already Have a Repository

If you already created a repository with a different name, use:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Verify

After pushing, visit your GitHub repository URL to see all your code online!

---

**Current Status:**
- ✅ Git repository initialized
- ✅ All files committed (3 commits total)
- ⏳ Waiting for GitHub repository URL to push
