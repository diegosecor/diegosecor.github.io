# 📦 GitHub Pages Deployment Guide

Follow these steps to host your Crossy Road game on GitHub Pages for FREE!

## Step 1: Initialize Git Repository

```powershell
git init
git add .
git commit -m "Initial commit - Crossy Road game"
```

## Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository (e.g., "crossy-road-game")
3. **DO NOT** initialize with README (we already have files)
4. Click "Create repository"

## Step 3: Push to GitHub

Replace `YOUR-USERNAME` and `YOUR-REPO-NAME` with your actual values:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source":
   - Select branch: **main**
   - Select folder: **/ (root)**
5. Click **Save**

## Step 5: Wait & Play! 🎉

- GitHub will build your site (takes 1-2 minutes)
- Your game will be live at: `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`
- Share the link with friends!

## 🔄 Making Updates

After any changes:

```powershell
git add .
git commit -m "Description of changes"
git push
```

Your site will automatically update in 1-2 minutes!

## ✅ Checklist

- [ ] Repository created on GitHub
- [ ] Files pushed to main branch
- [ ] GitHub Pages enabled in Settings
- [ ] Game is live and playable
- [ ] Updated README.md with your actual game URL

## 🎮 Your Live Game URL

After deployment, update this in README.md:

```
https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/
```

## 💡 Tips

- The game works on mobile browsers too!
- No server required - it's 100% static
- Free hosting forever on GitHub Pages
- Can use a custom domain if you want

---

**Need help?** Check [GitHub Pages documentation](https://docs.github.com/en/pages)
