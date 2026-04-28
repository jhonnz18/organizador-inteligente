import os
import shutil
from pathlib import Path
import logging

# Configuración de logs para que el proyecto sea profesional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organizar_proyecto():
    # AJUSTE DE RUTA: 
    # Path(__file__) es 'src/main.py'
    # .parent es 'src/'
    # .parent de nuevo es la raíz del proyecto 'Organizador_inteligente/'
    ruta_raiz = Path(__file__).resolve().parent.parent

    # Definimos las categorías
    categorias = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Instaladores": [".exe", ".msi", ".dmg"],
        "Comprimidos": [".zip", ".rar", ".7z", ".tar"],
        "Programacion": [".py", ".js", ".html", ".css", ".json"]
    }

    logging.info(f"Iniciando limpieza en: {ruta_raiz}")

    # Contador para el reporte final
    archivos_movidos = 0

    # Escaneamos los archivos en la raíz
    for archivo in ruta_raiz.iterdir():
        # Regla de oro: No mover carpetas, ni el entorno virtual, ni archivos de config
        if archivo.is_file() and not archivo.name.startswith('.'):
            extension = archivo.suffix.lower()
            
            for nombre_carpeta, extensiones in categorias.items():
                if extension in extensiones:
                    carpeta_destino = ruta_raiz / nombre_carpeta
                    carpeta_destino.mkdir(exist_ok=True)
                    
                    try:
                        shutil.move(str(archivo), str(carpeta_destino / archivo.name))
                        logging.info(f"Movido: {archivo.name} -> {nombre_carpeta}/")
                        archivos_movidos += 1
                    except Exception as e:
                        logging.error(f"No se pudo mover {archivo.name}: {e}")
                    break
    
    logging.info(f"Proceso terminado. Archivos organizados: {archivos_movidos}")

if __name__ == "__main__":
    organizar_proyecto()