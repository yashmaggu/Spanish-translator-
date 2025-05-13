from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import uvicorn

app = FastAPI()

# Enable CORS so frontend can access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the translation model
model_name = "facebook/nllb-200-distilled-600M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

@app.post("/translate")
async def translate_text(request: Request):
    try:
        data = await request.json()
        english_text = data.get("text", "")
        print(f"Received text for translation: {english_text}")

        if not english_text:
            return {"translated_text": "", "error": "No text provided"}

        # Enhanced approach to preserve structure with batch processing
        if '\n' in english_text:
            # Split the text by line breaks
            lines = english_text.split('\n')
            translated_lines = []
            
            tokenizer.src_lang = "eng_Latn"
            
            # Process lines in batches to reduce inference calls
            batch_size = 5  # Adjust based on your performance needs
            non_empty_lines = []
            line_indices = []
            
            # Step 1: Collect non-empty lines and their indices
            for i, line in enumerate(lines):
                if line.strip():
                    non_empty_lines.append(line)
                    line_indices.append(i)
            
            # Step 2: Process lines in batches
            translated_batch_results = []
            for i in range(0, len(non_empty_lines), batch_size):
                # Get the current batch
                current_batch = non_empty_lines[i:i+batch_size]
                
                # Batch process the lines
                inputs = tokenizer(current_batch, return_tensors="pt", padding=True, truncation=True)
                translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["spa_Latn"])
                
                # Decode each result in the batch
                for j in range(len(translated_tokens)):
                    translation = tokenizer.decode(translated_tokens[j], skip_special_tokens=True)
                    translated_batch_results.append(translation)
            
            # Step 3: Reconstruct the original format with translations
            result_index = 0
            for i in range(len(lines)):
                if i in line_indices:
                    # This was a non-empty line, use the translation
                    translated_lines.append(translated_batch_results[result_index])
                    result_index += 1
                else:
                    # This was an empty line, preserve it
                    translated_lines.append("")
            
            # Join the translated lines with original line breaks
            translated_text = '\n'.join(translated_lines)
        else:
            # For single-line text, translate as usual
            tokenizer.src_lang = "eng_Latn"
            inputs = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)
            translated_tokens = model.generate(**inputs, forced_bos_token_id=tokenizer.lang_code_to_id["spa_Latn"])
            translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        print(f"Translation result: {translated_text}")
        return {"translated_text": translated_text}
    except Exception as e:
        print(f"Error in translation: {str(e)}")
        return {"translated_text": "", "error": str(e)}

# Serve the static HTML file
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
