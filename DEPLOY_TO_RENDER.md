# Deploying Spanish Translator to Render

This guide will help you deploy your Spanish Translation application to Render, which provides excellent support for Python applications with ML models.

## Prerequisites

- A Render account (sign up at https://render.com if you don't have one)
- Git installed on your computer (to push your code to a repository)

## Step 1: Create a Git Repository

You need a Git repository for your code:

```bash
# Initialize Git (if not already done)
git init

# Add all files
git add .

# Commit the changes
git commit -m "Initial commit"
```

## Step 2: Create a GitHub/GitLab Repository

- Create a new repository on GitHub or GitLab
- Push your local repository to the remote:

```bash
git remote add origin <your-repository-url>
git push -u origin main
```

## Step 3: Deploy to Render

1. Log in to your Render account
2. Click "New +" and select "Web Service"
3. Connect your Git repository
4. Configure the service:
   - Name: spanish-translator
   - Environment: Python
   - Region: Choose a region close to your users
   - Branch: main
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Plans: Choose the Free plan (or more resources if needed)
   - Advanced Settings:
     - Add environment variable: PYTHON_VERSION = 3.9.0

5. Click "Create Web Service"

## Step 4: Monitor the Deployment

The initial build and deployment will take some time (approximately 5-10 minutes) since Render needs to download and cache the ML model (about 1.2GB).

Once deployment is complete, Render will provide a URL for your application (usually in the format `https://spanish-translator.onrender.com`).

## Important Notes

1. **Cold Starts**: Free tier services on Render spin down after 15 minutes of inactivity. The first request after inactivity will take longer as the service restarts.

2. **Model Loading**: The first load will download the NLLB translation model (~1.2GB), which takes time.

3. **Memory Limitations**: If you encounter memory issues, you might need to upgrade to a paid plan with more resources.

4. **Multiple Instances**: For production use, consider setting up multiple instances for reliability.

## Troubleshooting

If you encounter issues:

1. Check the logs in the Render dashboard
2. Ensure all dependencies are correctly specified in requirements.txt
3. Verify the start command is correct
4. Test your application locally before deploying
