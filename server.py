from flask import Flask, render_template, request

import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    archivos = request.files.getlist('archivos')
    for archivo in archivos:
        # Hacer algo con cada archivo, por ejemplo, guardarlos en el servidor
        archivo.save(archivo.filename)
        ruta_original = '.\\'+archivo.filename
        carpeta_destino = '.\\PC1-upload'
        nombre_archivo = os.path.basename(ruta_original)
        ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
        os.rename(ruta_original, ruta_destino)
    return 'Archivos subidos exitosamente.'

@app.route('/execute')
def execute():
    # Aquí puedes escribir el código Python que deseas ejecutar
    result = '¡Código Python ejecutado!'
    return result

if __name__ == '__main__':
    app.run()