from flask import Flask, request, jsonify
from flask_cors import CORS
from logic.solver import LogicSolver

app = Flask(__name__)
CORS(app)  # Permet toutes les origines

@app.route('/truth_table', methods=['POST', 'OPTIONS'])
def truth_table():
    print(request.method)
    if request.method == 'OPTIONS':
        # Gérer la requête preflight
        response = app.make_default_options_response()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    try:
        hypothese = request.json['hypothese']
        solver = LogicSolver(hypothese)
        B, variables = solver.solve()
        tableaux = transpose_table(B)
        
        response = jsonify({'variables': variables, 'tableaux': tableaux})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
        return response
    except Exception as e:
        print("Erreur :", str(e))
        return jsonify({'error': str(e)}), 500

def transpose_table(mat):
        if not mat or not mat[0]:
            return []
        
        rows = len(mat[0])
        cols = len(mat)

        transposed = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(mat[j][i])
            transposed.append(row)
            
        return transposed

if __name__ == '__main__':
    app.run(port=5000, debug=True)