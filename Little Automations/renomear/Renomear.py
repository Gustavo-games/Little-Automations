import os
import shutil
import tkinter
from tkinter import messagebox

nomeTrocar = input("Digite o nome para substituir para: ")

nomeDoScript = os.path.basename(__file__)

NOMEBASESCRIPT, _ = os.path.splitext(nomeDoScript)

if nomeTrocar == NOMEBASESCRIPT or nomeTrocar == NOMEBASESCRIPT+".py":
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showerror("Error", "NÃO")
    exit() 

arquivosNaPasta = os.listdir()

if nomeDoScript in arquivosNaPasta:
    arquivosNaPasta.remove(nomeDoScript)

arquivosNaPasta.sort()

nomeTrocar, novaExt = os.path.splitext(nomeTrocar)

i = 0

for arquivo in arquivosNaPasta:
    i += 1
    _, tempExt = os.path.splitext(arquivo)
    os.rename(arquivo, f"TEMPNAME{i}{tempExt}")

arquivosNaPasta = os.listdir()

if "main.py" in arquivosNaPasta:
    arquivosNaPasta.remove(nomeDoScript)

arquivosNaPasta.sort()

i = 0
for arquivo in arquivosNaPasta:
    nomeBase, ext = os.path.splitext(arquivo)
    if i == 0:
        if novaExt == "":
            os.rename(arquivo, f"{nomeTrocar}{ext}")
        else:
            os.rename(arquivo, f"{nomeTrocar}{novaExt}")
    elif novaExt == "":
        os.rename(arquivo, f"{nomeTrocar}({i}){ext}")
    else:
        os.rename(arquivo, f"{nomeTrocar}({i}){novaExt}")
    i += 1
    