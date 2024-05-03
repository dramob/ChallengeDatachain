# ChallengeDatachain
# Chatbot d'assistance pour le support client

Ce projet est un chatbot d'assistance pour le support client, basé sur l'API GPT-3 d'OpenAI et les modèles de sentence-transformers pour la recherche de similarité sémantique. Le chatbot renvoie des réponses pertinentes en fonction de la requête de l'utilisateur, en utilisant des articles pré-chargés pour fournir un contexte supplémentaire.

## Fonctionnalités

* Recherche de similarité sémantique entre la requête de l'utilisateur et les articles disponibles
* Génération de réponses pertinentes à l'aide de l'API GPT-3 d'OpenAI
* Interface utilisateur simple et conviviale pour interagir avec le chatbot
* Prise en charge de plusieurs formats de données pour les articles, y compris JSON

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Créez un fichier `.env` dans le répertoire racine du projet et ajoutez votre clé d'API OpenAI.
3. Installez les dépendances requises en utilisant `pip install -r requirements.txt`.
4.Lire le notebook de configuration du RAG pour plus de détail sur chaque étapes et tester les query .
5. Modifiez l'url 'https://didactic-winner-j9p5wwgv4rv2pjr6-5001.app.github.dev/query' dans le front.htm pour `http://localhost:5001` .# L'app ne run pas sur un github codespace sinon
6. Lancez l'application Flask en utilisant `python app.py`.
7. Accédez à l'interface utilisateur du chatbot en ouvrant `http://localhost:5001` dans votre navigateur.


## Utilisation

1. Saisissez votre requête dans la zone de texte prévue à cet effet.
2. Cliquez sur le bouton "Envoyer" ou appuyez sur Entrée pour soumettre votre requête.
3. Le chatbot recherchera l'article le plus similaire à votre requête et générera une réponse pertinente à l'aide de l'API GPT-3 d'OpenAI.
4. La réponse s'affichera dans la zone de conversation.

## Technologies utilisées

* Flask pour l'API RESTful
* Sentence-transformers pour la recherche de similarité sémantique
* OpenAI API pour la génération de réponses
* jQuery pour les requêtes AJAX
* HTML/CSS pour l'interface utilisateur

## Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez ouvrir une pull request avec vos modifications.

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.