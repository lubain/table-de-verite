# Table de Vérité - Générateur Logique

Ce projet est un générateur de table de vérité pour les expressions logiques. Il comprend une interface web React et une API Flask pour le traitement des expressions logiques.

## 🚀 Fonctionnalités

- Génération de tables de vérité pour des expressions logiques
- Interface utilisateur intuitive
- Traitement en temps réel des expressions
- Support pour les opérateurs logiques standards

## 🛠️ Technologies Utilisées

### Frontend

- React 18
- TypeScript
- Vite
- Material-UI
- Tailwind CSS
- Axios

### Backend

- Python
- Flask
- Flask-CORS

## 📋 Prérequis

- Node.js (v18 ou supérieur)
- Python (v3.8 ou supérieur)
- npm ou yarn

## 🔧 Installation

### Backend (Flask)

```bash
# Accéder au dossier du serveur
cd server

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows
venv\Scripts\activate
# Sur Unix ou MacOS
source venv/bin/activate

# Installer les dépendances
pip install flask flask-cors
```

### Frontend (React)

```bash
# Accéder au dossier client
cd client

# Installer les dépendances
npm install
```

## 🚀 Démarrage

### Démarrer le Backend

```bash
# Dans le dossier server
python app.py
```

Le serveur démarrera sur `http://localhost:5000`

### Démarrer le Frontend

```bash
# Dans le dossier client
npm run dev
```

L'application sera accessible sur `http://localhost:8080`

## 📝 Utilisation

1. Ouvrez votre navigateur et accédez à `http://localhost:8080`
2. Entrez une expression logique dans le champ de texte
3. La table de vérité sera générée automatiquement

### Syntaxe des Expressions

- `!` pour la négation (NOT)
- `&` pour la conjonction (AND)
- `|` pour la disjonction (OR)
- `=>` pour l'implication
- `<=>` pour l'équivalence

Exemple : `p & !q => r`

## 🔍 Structure du Projet

```
project/
├── client/                 # Frontend React
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── ...
│   ├── package.json
│   └── vite.config.ts
│
└── server/                 # Backend Flask
    ├── app.py
    ├── logic/
    │   ├── solver.py
    │   ├── truth_table.py
    │   └── ...
    └── requirements.txt
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commit vos changements
4. Push sur la branche
5. Ouvrir une Pull Request

## ✨ Auteurs

- ZAFINDRAMANGA Lubain Fadhel

## 📞 Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub.
