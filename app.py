from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bienvenido a Ecanosoft</title>
        <style>
            body { font-family: Arial; background: #f3f3f3; text-align: center; padding-top: 100px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>¡Bienvenido a tu app Flask en Railway, Erasmo!</h1>
        <p>Funciona perfecto con tu dominio personalizado.</p>
    </body>
    </html>
    """)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway asigna el puerto por variable de entorno
    app.run(host='0.0.0.0', port=port)

