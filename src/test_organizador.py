import unittest
from pathlib import Path

# Importamos la lógica, aunque por ahora solo probaremos la estructura
class TestOrganizador(unittest.TestCase):
    
    def test_verificar_ruta_raiz(self):
        """Verifica que el script localice la carpeta principal correctamente"""
        ruta_actual = Path(__file__).resolve().parent.parent
        # Si existe el archivo .gitignore en esa ruta, es la correcta
        archivo_control = ruta_actual / ".gitignore"
        self.assertTrue(archivo_control.exists(), "No se encontró el archivo .gitignore en la raíz")

if __name__ == "__main__":
    unittest.main()