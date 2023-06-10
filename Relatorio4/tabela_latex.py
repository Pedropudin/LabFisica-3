import pyperclip
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

LIMITE_PAGINA = 40


def getFilename():
    Tk().withdraw()
    filename = askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
    return filename

def createTable(edited_columns,edited_lines, Ncolumns):
    text = r'''
        \begin{table}[H]
            \centering
            \begin{tabular}{|''' + "c|"*Ncolumns + '''}
                \hline
                '''
    text += edited_columns
   
    for line in edited_lines: 
        text += line

    text += '''
        \end{tabular}
        \caption{COLOCAR DESCRICAO}
        \label{tab: COLOCAR LABEL}
    \end{table}
    '''
    
    return text

def editAllLines(file):
    lines = []
    for i in range(1,len(file[file.columns[0]])): 
        row_i= '\n        '
        row_i += " & ".join(str(b) for b in list(file.T[i].values)) + r" \\ \hline"
        lines.append(row_i)
    return lines

def readFile(filename):
    try:
        file = pd.read_csv(filename)
        columns = file.columns
        filesWithEditedLines = []

        eLines = editAllLines(file)
        
        contador = 0
        new_rows = []
        for k in range(len(eLines)):
            if (contador>=LIMITE_PAGINA or k == len(eLines)-1):
                filesWithEditedLines.append(new_rows)
                contador=0
                new_rows = []
            else:
                new_rows.append(eLines[k])
            contador+=1

        
        finalText = ""
        for f in filesWithEditedLines:
            finalText += '\n \n \n' + createTable(" & ".join(list(columns)) + r" \\ \hline",f,len(columns)) + '\n \n \n' + r'\newpage'
        print(finalText)
        pyperclip.copy(finalText)

        return finalText
    except:
        return "jae entao mlk"

name = getFilename()
readFile(name)