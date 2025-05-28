import os
from docx import Document
import tkinter as tk
from tkinter import filedialog

def load_txt_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def load_docx_file(path):
    doc = Document(path)
    return '\n'.join([para.text for para in doc.paragraphs])

def load_file(path):
    if path.endswith('.txt'):
        return load_txt_file(path)
    elif path.endswith('.docx'):
        return load_docx_file(path)
    else:
        raise ValueError("Tipo de archivo no soportado")

def load_files_from_folder(folder_path):
    contents = []
    for file in os.listdir(folder_path):
        if file.endswith(('.txt', '.docx')):
            try:
                contents.append(load_file(os.path.join(folder_path, file)))
            except Exception as e:
                print(f"Error al cargar {file}: {e}")
    return contents

def list_text_files(directory="data"):
    files = [f for f in os.listdir(directory) if f.endswith(('.txt', '.docx'))]
    if not files:
        print("No se encontraron archivos en la carpeta.")
        return []
    print(f"\nArchivos disponibles en '{directory}':")
    for idx, f in enumerate(files):
        print(f"{idx + 1}. {f}")
    return files

def select_file_from_list(directory="data"):
    files = list_text_files(directory)
    if not files:
        return None
    try:
        choice = int(input("Seleccione el número del archivo a cargar: ")) - 1
        if 0 <= choice < len(files):
            return os.path.join(directory, files[choice])
        else:
            print("Selección inválida.")
    except ValueError:
        print("Entrada inválida.")
    return None

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Archivos de texto", "*.txt"), ("Documentos Word", "*.docx")]
    )
    root.destroy()
    return file_path