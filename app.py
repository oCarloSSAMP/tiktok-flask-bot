from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

nomes_para_spawnar = []

@app.route("/comentario", methods=["POST"])
def receber_comentario():
    data = request.get_json()
    nome = data.get("nome", "")
    if nome:
        print(f"📥 Novo nome recebido do TikTok: {nome}")
        nomes_para_spawnar.append(nome)
        return {"status": "ok"}, 200
    return {"status": "erro"}, 400

@app.route("/spawns", methods=["GET"])
def enviar_para_roblox():
    global nomes_para_spawnar
    if nomes_para_spawnar:
        nomes = nomes_para_spawnar.copy()
        nomes_para_spawnar.clear()
        return {"nomes": nomes}, 200
    return {"nomes": []}, 200

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
