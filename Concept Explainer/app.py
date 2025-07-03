from flask import Flask, render_template, request, jsonify
import wikipedia
import os
import cohere
from dotenv import load_dotenv
import urllib.parse

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the Cohere API key from environment variables
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY) if COHERE_API_KEY else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    concept = request.form.get('concept', '')
    if not concept:
        return jsonify({'wiki_summary': 'Please enter a concept.', 'wiki_options': [], 'ai_example': '', 'wiki_url': '', 'youtube_url': ''})
    wiki_summary = ''
    wiki_options = []
    wiki_url = ''
    youtube_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote_plus(concept)}"
    try:
        page = wikipedia.page(concept, auto_suggest=True)
        wiki_summary = ' '.join(page.summary.split('\n')[0:2])
        wiki_url = page.url
    except wikipedia.DisambiguationError as e:
        wiki_options = e.options[:5]
    except Exception as wiki_e:
        try:
            wiki_summary = wikipedia.summary(concept, sentences=2)
            # Try to get the page URL from search
            search_results = wikipedia.search(concept)
            if search_results:
                try:
                    page = wikipedia.page(search_results[0], auto_suggest=True)
                    wiki_url = page.url
                except Exception:
                    wiki_url = ''
        except Exception:
            wiki_summary = f'Wikipedia error: {wiki_e}'
    ai_example = ''
    if wiki_options == [] and wiki_summary and not wiki_summary.startswith('Wikipedia error:') and co:
        prompt = f"Give a simple, complete example for: {concept}"
        try:
            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=200,
                temperature=0.7
            )
            ai_example = response.generations[0].text.strip()
            if len(ai_example) < 40:
                ai_example += " (The AI example may be incomplete. Try rephrasing or asking again.)"
        except Exception as e:
            ai_example = f"Cohere API exception: {e}"
    return jsonify({'wiki_summary': wiki_summary, 'wiki_options': wiki_options, 'ai_example': ai_example, 'wiki_url': wiki_url, 'youtube_url': youtube_url})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)
