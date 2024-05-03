from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Permettre toutes les origines, tous les en-têtes et méthodes.

# Supposons que vous avez un fichier JSON 'articles.json' contenant vos articles.
def load_articles():
    with open('articles.json', 'r', encoding='utf-8') as file:
        return json.load(file)

articles = load_articles()

def find_most_similar_article(query, articles):
    # Ici, ajoutez votre logique pour trouver l'article le plus similaire.
    # Pour simplifier, retournons le premier article.
    return articles[0]

def generate_response_with_gpt3(article, query):
    # Simuler une réponse, remplacer par un appel API ou une autre logique.
    return f"Réponse simulée pour l'article: {article['title']}"

@app.route('/query', methods=['POST'])
def handle_query():
    query = request.json.get('query', '')
    most_similar_article = find_most_similar_article(query, articles)
    response = generate_response_with_gpt3(most_similar_article, query)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Utiliser un port spécifique pour faciliter le port forwarding.
