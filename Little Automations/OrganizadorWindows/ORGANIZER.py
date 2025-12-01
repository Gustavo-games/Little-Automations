import os
import shutil
from pathlib import Path

DesktopPath = ""
DocumentsPath = ""
PicturesPath = ""
VideosPath = ""
MusicPath= ""

if os.path.exists(Path.home() / "Desktop"):
    DesktopPath = Path.home() / "Desktop"
    DocumentsPath = Path.home() / "Documents"
    PicturesPath = Path.home() / "Pictures"
    VideosPath = Path.home() / "Videos"
    MusicPath = Path.home() / "Music"
elif os.path.exists( Path.home() / "Área de Trabalho"):
    DesktopPath = Path.home() / "Área de Trabalho"
    DocumentsPath = Path.home() / "Documentos"
    PicturesPath = Path.home() / "Imagens"
    VideosPath = Path.home() / "Vídeos"
    MusicPath = Path.home() / "Música"
else:
    exit()

Arquivos = os.listdir()

NOMESCRIPT, EXTSCRIPT = os.path.splitext(os.path.basename(__file__))

try:
    Arquivos.remove(NOMESCRIPT)
except ValueError:
    print("ERRO: O nome do script foi alterado, impossibilitando a execução.")
    exit()

NotasPath = DocumentsPath / "BLOCO_DE_NOTAS"
NotasPath.mkdir(parents=True, exist_ok=True)

Outros = DocumentsPath / "OUTROS"
Outros.mkdir(parents=True, exist_ok= True)

PDFPath = DocumentsPath / "PDF"
PDFPath.mkdir(parents=True, exist_ok= True)

ZIPPath = DocumentsPath / "ZIP"
ZIPPath.mkdir(parents=True, exist_ok= True)

RARPath = DocumentsPath / "RAR"
RARPath.mkdir(parents=True, exist_ok= True)

APPSPath = DocumentsPath / "APPS"
APPSPath.mkdir(parents=True, exist_ok= True)

WORDPath = DocumentsPath / "WORD"
WORDPath.mkdir(parents=True, exist_ok= True)

PNGPath = PicturesPath / "PNG"
PNGPath.mkdir(parents=True, exist_ok= True)

JPGPath = PicturesPath / "JPG"
JPGPath.mkdir(parents=True, exist_ok= True)

WAVPath = MusicPath / "WAV"
WAVPath.mkdir(parents=True, exist_ok= True)

MP3Path = MusicPath / "MP3"
MP3Path.mkdir(parents=True, exist_ok= True)

MP4Path = VideosPath / "MP4"
MP4Path.mkdir(parents=True, exist_ok= True)

WEBMPath = VideosPath / "WEBM"
WEBMPath.mkdir(parents=True, exist_ok= True)

dupli = Path.cwd() / "DUPLICADOS"
dupli.mkdir(parents=True, exist_ok=True)

def MovarPara(Path, arq):
    dir = Path / arq
    if dir.exists():
        shutil.move(arq, dupli)    
    else: 
        shutil.move(arq, Path)

for arq in Arquivos:

    nome, ext = os.path.splitext(arq)
    match ext:
        case ".png":
            MovarPara(PNGPath, arq)
        case ".txt":
            MovarPara(NotasPath, arq)
        case ".pdf":
            MovarPara(PDFPath, arq)
        case ".doc" | ".docx":
            MovarPara(WORDPath, arq)
        case ".jpg":
            MovarPara(JPGPath, arq)
        case ".zip":
            MovarPara(ZIPPath, arq)
        case ".rar":
            MovarPara(RARPath, arq)
        case ".wav":
            MovarPara(WAVPath, arq)
        case ".mp3":
            MovarPara(MP3Path, arq)
        case ".mp4":
            MovarPara(MP4Path, arq)
        case ".exe":
            MovarPara(APPSPath, arq)
        case _:
            MovarPara(Outros, arq)

if dupli.exists():
    if not os.listdir(dupli):
        os.rmdir(dupli)