from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import json
import os
from fuzzywuzzy import process
import wikipedia
from duckduckgo_search import DDGS

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# === Updated Admin Credentials ===
ADMIN_USERNAME = "taha "
ADMIN_PASSWORD = "1234567890"

# === Utility Functions ===

def load_faq_data():
    with open('data/faq.json', 'r') as f:
        return json.load(f)

def find_best_match(query, faq_data):
    questions = [item['question'] for item in faq_data]
    match, score = process.extractOne(query, questions)
    if score >= 90  :
        return next(item for item in faq_data if item['question'] == match)
    else:
        return None

def log_unknown_query(query):
    with open('data/unknown_queries.log', 'a') as log_file:
        log_file.write(query + '\n')

def fetch_duckduckgo_answer(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=1)
            for result in results:
                return result['body']
    except Exception:
        return None

def generate_google_link(query):
    base_url = "https://www.google.com/search?q="
    query_encoded = query.replace(' ', '+')
    return f"{base_url}{query_encoded}"

def fetch_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"According to Wikipedia: {summary}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Suggestions: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return None

# === Routes ===

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("message")
    
    # Load fresh FAQ every time
    faq_data = load_faq_data()
    
    # Check FAQ first
    best_match = find_best_match(user_query, faq_data)
    if best_match:
        return jsonify({"answer": best_match['answer']})
    
    # Log unknown query
    log_unknown_query(user_query)
    
    # DuckDuckGo Answer
    ddg_ans = fetch_duckduckgo_answer(user_query)
    google_link = generate_google_link(user_query)
    if ddg_ans:
        combined = f"{ddg_ans}<br><br>🔗 <a href='{google_link}' target='_blank'>Check more on Google</a>"
        return jsonify({"answer": combined})
    
    # Wikipedia fallback
    wiki_ans = fetch_wikipedia_summary(user_query)
    if wiki_ans:
        return jsonify({"answer": wiki_ans})
    
    return jsonify({"answer": "Sorry, I don't have info on that. Please contact Prof. Vikas Chavan at 9404018414."})

# === Admin Routes ===

@app.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error="Invalid credentials")
    return render_template('admin_login.html')

@app.route("/admin/dashboard", methods=['GET', 'POST'])
def admin_dashboard():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    
    faq_data = load_faq_data()  # Load fresh FAQ
    
    if os.path.exists('data/unknown_queries.log'):
        with open('data/unknown_queries.log', 'r') as f:
            unknown_queries = f.readlines()
    else:
        unknown_queries = []
    
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')
        if question and answer:
            new_entry = {"question": question, "answer": answer}
            faq_data.append(new_entry)
            with open('data/faq.json', 'w') as f:
                json.dump(faq_data, f, indent=4)
            return redirect(url_for('admin_dashboard'))
    
    return render_template('admin_dashboard.html', unknown_queries=unknown_queries)

@app.route("/admin/logout")
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('index'))  # Redirect to chatbot home page after logout

if __name__ == "__main__":
    app.run(debug=True)
