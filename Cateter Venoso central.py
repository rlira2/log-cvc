import csv
import ctypes
import tkinter as tk
from tkinter import filedialog
from openpyxl import load_workbook

#To use openFile dialog
root = tk.Tk()
root.withdraw()

#Messages for user interaction
OPEN_TXT_MESSAGE = "Selecciona un archivo .txt para incluir en el LOG"
OPEN_TXT_TITLE = "Cargar nueva ejecución"
OPEN_XLSX_MESSAGE = "Selecciona el archivo Excel con el LOG de las ejecuciones anteriores"
OPEN_XLSX_TITLE = "LOG ejecuciones"
OPEN_NO_FILE_ERROR_MESSAGE = "No se ha seleccionado un archivo válido"
OPEN_NO_PERMISSION_ERROR_MESSAGE = "Debe cerrar el archivo Excel para poder modificarlo"
OPEN_ERROR_TITLE = "¡ERROR!"
SUCCESS_MESSAGE = "Ejecución añadida correctamente al LOG"
SUCCES_TITLE = "LOG Actualizado"

#Variables for reading and writing .txt and .xlsx documents
TXT_AS_CSV = 'txtAsCSV'
TXT_ROW_SPLIT = ' '
LOG_WORKBOOK = "Log videos CVC.xlsx"
LOG_WORKSHEET = "Log videos CVC"



#Function to load a .txt file, it returns an array of an array
def loadText():
    ctypes.windll.user32.MessageBoxW(0, OPEN_TXT_MESSAGE, OPEN_TXT_TITLE, 0)
    txt_file_path = filedialog.askopenfilename(filetypes=(('Text files', 'txt'),))
    txt_log = []
    try:
        csv.register_dialect(TXT_AS_CSV, delimiter = TXT_ROW_SPLIT)
        with open(txt_file_path, 'r') as f:
            reader = csv.reader(f, dialect=TXT_AS_CSV)
            for row in reader:                
                txt_log.append(row)
        return txt_log
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, OPEN_NO_FILE_ERROR_MESSAGE, OPEN_ERROR_TITLE, 0)

#Function to read existing .xlsx log file and add the new .txt rows
def writeExcel (txt_log):
    ctypes.windll.user32.MessageBoxW(0, OPEN_XLSX_MESSAGE, OPEN_XLSX_TITLE, 0)
    excel_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")]) 
    if excel_file_path:
        pass
    else:
        pass
    try:        
        wb = load_workbook(excel_file_path)
        ws = wb[LOG_WORKSHEET]
        for row in txt_log:
            ws.append(row)
        wb.save(excel_file_path)
        ctypes.windll.user32.MessageBoxW(0, SUCCESS_MESSAGE, SUCCES_TITLE, 0)

    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, OPEN_NO_FILE_ERROR_MESSAGE, OPEN_ERROR_TITLE, 0)
    except PermissionError:
        ctypes.windll.user32.MessageBoxW(0, OPEN_NO_PERMISSION_ERROR_MESSAGE, OPEN_ERROR_TITLE, 0)

#Main program
txt_log = loadText()
if txt_log is not None:
    writeExcel(txt_log)
