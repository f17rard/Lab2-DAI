from flask import Flask, jsonify, request

app = Flask(__name__)

catalogo = {
    201: {"id":201,"producto": "Teclado mecanico RGB", "precio": 45.00, "stock": 12},
    202: {"id":202,"producto": "Mouse inalambrico", "precio": 18.00, "stock": 25},
    203: {"id":203,"producto": "Monitor LED 24\"", "precio": 165.00, "stock": 8}
}

@app.route("/")
def inicio():
    pass

@app.get("/productos")
def obtener_catalogo():
    pass

@app.get("/productos/<int:id>")
def consultar_producto_id(id: int):
    pass

app.post("/productos")
def registrar_producto():
    pass

if __name__ == "__main__":
    app.run(debug=True)