# English to Spanish Translator

A web application that translates English text to Spanish using the NLLB-200 neural machine translation model from Facebook.

## Features

- Modern, responsive UI
- Real-time translation of English text to Spanish
- Uses state-of-the-art neural machine translation model
- Built with FastAPI and Transformers library
- Properly renders line breaks in translated text

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all necessary packages including FastAPI, Uvicorn, PyTorch, and Transformers.

### 2. Run the Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8001
```

The application will be available at http://localhost:8001

### 3. Using the Translator

1. Open your browser and navigate to http://localhost:8001
2. Enter English text in the input field
3. Click "Translate to Spanish" button
4. View the translated Spanish text in the output box

## Deployment

### Deploying to Render

1. Create a free Render account at https://render.com
2. Connect your GitHub repository
3. Create a new Web Service
4. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables: Add `PYTHON_VERSION=3.9`

### Deploying to Heroku

1. Create a free Heroku account
2. Install the Heroku CLI and login
3. Navigate to your project directory and run:

```bash
heroku create your-app-name
git add .
git commit -m "Ready for deployment"
git push heroku main
```

## Technical Details

- Backend: FastAPI
- Translation Model: facebook/nllb-200-distilled-600M
- Frontend: HTML, CSS, JavaScript

## Notes

- The first run will download the translation model (approximately 1.2GB), which may take some time depending on your internet connection
- Subsequent runs will use the cached model and be much faster to start
- When deployed to platforms like Render or Heroku, the initial startup may be slow due to model downloading
