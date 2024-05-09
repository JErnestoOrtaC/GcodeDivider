import tkinter as tk
from tkinter import filedialog
import os

def split_gcode(input_file, output_dir, max_lines=4999):
    with open(input_file, 'r') as f:
        gcode = f.readlines()

    num_files = (len(gcode) - 1) // max_lines + 1

    # Creamos la carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_files):
        output_file = os.path.join(output_dir, f"gcode{i + 1}.nc")
        with open(output_file, 'w') as f:
            start = i * max_lines
            end = min((i + 1) * max_lines, len(gcode))
            f.writelines(gcode[start:end])

def select_file_and_output_dir():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Solicitamos al usuario que seleccione la ubicación de la carpeta
        output_dir = filedialog.askdirectory()
        if output_dir:
            # Solicitamos al usuario que ingrese el nombre de la carpeta
            folder_name = tk.simpledialog.askstring("Input", "Enter folder name:")
            if folder_name:
                # Creamos la carpeta con el nombre proporcionado dentro de la ubicación seleccionada
                folder_path = os.path.join(output_dir, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                split_gcode(file_path, folder_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    select_file_and_output_dir()
