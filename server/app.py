from flask import Flask, request, jsonify
from flask_cors import CORS
from logic.solver import LogicSolver

app = Flask(__name__)
# CORS(app)  # Cette ligne permet à toutes les origines d'accéder à votre serveur Flask
CORS(app, resources={r"/truth_table": {"origins": "http://localhost:8080"}})  # Limite l'origine à localhost:8080

@app.route('/truth_table', methods=['POST'])
def truth_table():
    try:
        hypothese = request.json['hypothese']
        solver = LogicSolver(hypothese)
        B, variables = solver.solve()
        
        return jsonify({'variables': variables, 'tableaux': B})
    except Exception as e:
        print("Erreur :", str(e))
        return jsonify({'error': str(e)}), 500

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True)