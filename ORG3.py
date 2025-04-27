import os
import shutil

# Definir la carpeta de descargas
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser("~"), "Downloads")

# Categorías de archivos por extensión
CATEGORIES = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "Audios": [".mp3", ".wav", ".flac", ".aac"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Ejecutables": [".exe", ".msi"],
    "Código": [".py", ".java", ".cpp", ".js", ".html", ".css", ".php", ".json", ".md", ".sh"],
    "Otros": []
}

def get_category(ext):
    """Devuelve la categoría correspondiente a una extensión."""
    for category, extensions in CATEGORIES.items():
        if ext.lower() in extensions:
            return category
    return "Otros"

def clean_empty_folders(folder):
    """Elimina carpetas vacías en un directorio dado."""
    for root, dirs, _ in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Si está vacía
                os.rmdir(dir_path)
                print(f"Eliminada carpeta vacía: {dir_path}")

def organize_downloads():
    """Organiza la carpeta de descargas por extensión."""
    for root, _, files in os.walk(DOWNLOADS_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1]
            if not ext:
                continue  # Saltar archivos sin extensión
            
            category = get_category(ext)
            category_folder = os.path.join(DOWNLOADS_FOLDER, category)
            ext_folder = os.path.join(category_folder, ext[1:].upper())
            
            os.makedirs(ext_folder, exist_ok=True)  # Crear carpeta si no existe
            
            new_path = os.path.join(ext_folder, file)
            shutil.move(file_path, new_path)
            print(f"Movido: {file} -> {new_path}")

    # Eliminar carpetas vacías después de organizar
    clean_empty_folders(DOWNLOADS_FOLDER)

if __name__ == "__main__":
    organize_downloads()
