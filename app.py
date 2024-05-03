# Importation des bibliothèques nécessaires
import json
import numpy as np
import openai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
from openai.types import Completion, CompletionChoice, CompletionUsage
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Initialisation de l'API Flask
app = Flask(__name__)
CORS(app, origins='*')  # Permettre toutes les origines, tous les en-têtes et méthodes.

# Chargement des variables d'environnement
load_dotenv()

# Initialisation du client OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Fonction pour charger les articles
def load_articles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        articles = json.load(file)
    return articles

# Chargement des articles
articles = load_articles('articles.json')

# Fonction pour vectoriser les articles
def vectorize_articles(articles):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    for article in articles:
        article['embedding'] = model.encode(article['content'][:512], convert_to_tensor=True)
    return articles

# Fonction pour trouver l'article le plus similaire à une requête
def find_most_similar_article(query, articles):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode(query, convert_to_tensor=True)
    similarities = [cosine_similarity(query_embedding.reshape(1, -1), article['embedding'].reshape(1, -1))[0][0] for article in articles]
    most_similar_index = np.argmax(similarities)
    return articles[most_similar_index]

# Fonction pour générer une réponse avec GPT-3
def generate_response_with_gpt3(article, query):
    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Adjust the model as necessary
            messages=[
                {"role": "system", "content": "You are a helpful assistant. The following context should give you better information to answer requests.Use it efficiently and answer."},
                {"role": "user", "content": query},
                {"role": "assistant", "content": article['content'][:1024]}  # Including article context
            ]
        )
        # Utilisation des propriétés directes des objets pour obtenir le contenu
        response_content = "\u200B\n\n" + chat_response.choices[0].message.content
        return response_content
    except Exception as e:
                         print(f"An error occurred: {e}")
    return None

@app.route('/')
def serve_frontend():
    return send_from_directory(os.path.join(os.path.dirname(__file__)), 'Front.html')

@app.route('/query', methods=['POST'])
def handle_query():
    # Traiter la requête
    query = request.json.get('query', '')
    print(query)

    # Vectoriser les articles
    vectorized_articles = vectorize_articles(articles)

    # Trouver l'article le plus similaire
    most_similar_article = find_most_similar_article(query, vectorized_articles)

    # Générer une réponse avec GPT-3
    response = generate_response_with_gpt3(most_similar_article, query)

    # Ajouter l'en-tête Access-Control-Allow-Origin à la réponse
    response_headers = {'Access-Control-Allow-Origin': '*'}

    # Renvoie la réponse JSON avec les en-têtes appropriés
    response_data = {'response': response}
    return jsonify(response_data), 200, response_headers

# Exécution de l'application Flask
if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Utiliser un port spécifique pour faciliter le port forwarding.
