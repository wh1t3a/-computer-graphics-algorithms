# GitHub Setup Guide

## Prerequisites

- GitHub account
- Git installed on your machine
- GitHub CLI (optional but recommended)

## Step-by-Step Setup

### 1️⃣ Create GitHub Repository

**Option A: Using GitHub Web UI**

1. Go to https://github.com/new
2. Fill in repository details:
   - **Repository name**: `-computer-graphics-algorithms`
   - **Description**: Interactive sandbox for computational geometry algorithms
   - **Public** (to share with world)
   - **Add .gitignore**: Python (we already have this)
   - **Add license**: MIT (we already have this)
   - **Do NOT initialize with README** (we have one)
3. Click "Create repository"
4. Copy the URL (HTTPS or SSH)

**Option B: Using GitHub CLI**

```bash
gh repo create -computer-graphics-algorithms \
  --public \
  --source=. \
  --remote=origin \
  --push
```

### 2️⃣ Initialize Local Git Repository

```bash
cd d:\cg\-computer-graphics-algorithms

# Initialize git
git init

# Configure git (if not done globally)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Computational geometry library with Graham Scan, Delaunay, and curve algorithms"
```

### 3️⃣ Connect to GitHub

```bash
# Add remote repository (replace USERNAME and REPO_URL)
git remote add origin https://github.com/YOUR-USERNAME/-computer-graphics-algorithms.git

# Verify remote
git remote -v
# Should show:
# origin  https://github.com/YOUR-USERNAME/-computer-graphics-algorithms.git (fetch)
# origin  https://github.com/YOUR-USERNAME/-computer-graphics-algorithms.git (push)
```

### 4️⃣ Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main

# Verify push
git status
# On branch main
# Your branch is up to date with 'origin/main'.
```

## Common Git Commands

```bash
# Check status
git status

# View commits
git log --oneline

# Create new branch for features
git checkout -b feature/new-algorithm
git push origin feature/new-algorithm

# Update from remote
git pull origin main

# Undo last commit (before push)
git reset --soft HEAD~1

# View changes
git diff
git diff --cached
```

## GitHub Pages Documentation (Optional)

### Enable GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Select **Branch: main**, **Folder: /docs**
3. Wait for deployment
4. Access at: `https://YOUR-USERNAME.github.io/-computer-graphics-algorithms/`

### Add to Pages (optional)

Create `docs/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Computational Geometry Sandbox</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        code { background: #f4f4f4; padding: 2px 6px; }
    </style>
</head>
<body>
    <h1>🎨 Computational Geometry Sandbox</h1>
    <p>Interactive algorithms library for geometric computing</p>
    <ul>
        <li><a href="https://github.com/YOUR-USERNAME/-computer-graphics-algorithms">GitHub Repo</a></li>
        <li><a href="../README.md">Documentation</a></li>
    </ul>
</body>
</html>
```

## Add Badges to README

Update README.md to show status:

```markdown
![Build](https://github.com/YOUR-USERNAME/-computer-graphics-algorithms/actions/workflows/python-tests.yml/badge.svg)
![License MIT](https://img.shields.io/badge/License-MIT-green)
![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)
```

## Enable GitHub Actions CI/CD

1. Go to **Actions** tab
2. GitHub automatically detects `.github/workflows/python-tests.yml`
3. Click "I understand my workflows, go ahead and enable them"
4. Tests run automatically on every push!

## Add Topics to Repository

**Settings** → **Topics**

Suggested topics:
- `computational-geometry`
- `algorithms`
- `delaunay-triangulation`
- `convex-hull`
- `curves`
- `python`
- `graphics`
- `education`

## Setup Publishing to PyPI (Optional)

### 1. Create PyPI Account
- Go to https://pypi.org/account/register/
- Verify email

### 2. Create PyPI Token
- Account Settings → API tokens
- Create token (scoped to `-computer-graphics-algorithms`)
- Save token securely

### 3. Add GitHub Secret
- Go to repository **Settings** → **Secrets and variables** → **Actions**
- Add new secret: `PYPI_API_TOKEN`
- Paste your token

### 4. Create Release Workflow
Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [created]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - run: pip install build
    - run: python -m build
    - uses: pypa/gh-action-pypi-publish@release/v1
      with:
        password: ${{ secrets.PYPI_API_TOKEN }}
```

### 5. Create Release
- Go to **Releases** → **Create new release**
- Tag: `v1.0.0`
- Publish release
- Workflow automatically builds and publishes to PyPI!

## Troubleshooting

### Error: "fatal: not a git repository"
```bash
cd /path/to/-computer-graphics-algorithms
git init
```

### Error: "fatal: could not read Username"
Use personal access token instead of password:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (with `repo` scope)
3. Use token as password when prompted

### Want to Reset Repository?
```bash
# Remove git history
rm -rf .git

# Start fresh
git init
git add .
git commit -m "Initial commit"
git remote add origin <URL>
git push -u origin main
```

## What to Do After Publishing

1. **Pin repository** (makes it appear on your GitHub profile)
2. **Add to project portfolio** on your resume/website
3. **Share with friends** - Tell them about it!
4. **Monitor issues** - Respond to user feedback
5. **Accept pull requests** - Review and merge contributions
6. **Keep updated** - Add new features and fix bugs

## Recommended README Badges

```markdown
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Tests Passing](https://github.com/YOUR-USERNAME/-computer-graphics-algorithms/actions/workflows/python-tests.yml/badge.svg)](https://github.com/YOUR-USERNAME/-computer-graphics-algorithms/actions)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](CONTRIBUTING.md)
```

## Next Steps

- [ ] Create GitHub repository
- [ ] Push code to GitHub
- [ ] Enable GitHub Actions
- [ ] Add repository topics
- [ ] Write first blog post about the project
- [ ] Share with computational geometry community
- [ ] Consider PyPI publication
- [ ] Monitor for issues and PRs

---

**Congratulations! Your project is now on GitHub! 🚀**

Feel free to reach out to the community and ask for feedback!
