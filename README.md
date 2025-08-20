# ⚔️ Boss Alert OCR Bot  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)  
![Discord.py](https://img.shields.io/badge/discord.py-latest-5865F2?logo=discord&logoColor=white)  
![Status](https://img.shields.io/badge/status-active-success?style=flat)  

---

## 👾 Sobre o projeto
Um **bot para Discord** que monitora a tela do jogo **Lineage 2** e envia alertas automáticos no servidor sempre que um **Boss** estiver vivo.  
O bot utiliza **OCR (Tesseract)** para ler a tela e detectar os nomes dos bosses em tempo real.
Deverá utilizar um auto-clique do mouse para ficar carregando o status do Boss no mapa do L2.

---

## ✨ Funcionalidades
✔️ Captura automática de uma região da tela.  
✔️ Reconhecimento de texto via **Tesseract OCR**.  
✔️ Detecta bosses específicos definidos na lista `bosses_alvo`.  
✔️ Envia alertas para o Discord com menção `@everyone`.  
✔️ Cooldown de **5 minutos** para evitar spam do mesmo Boss.  
✔️ Logs no terminal mostrando o status do bot.  

---

## 🛠️ Tecnologias
- 🐍 **Python 3**
- 📸 **PyAutoGUI** → captura da tela  
- 🖼️ **Pillow (PIL)** → manipulação de imagens  
- 🔎 **pytesseract** → OCR para reconhecimento de texto  
- 🤖 **discord.py** → integração com o Discord  

---

##🔹 3. Instale o Tesseract OCR

Baixe e instale: Tesseract OCR

Copie o caminho do executável e configure no código:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

---

## ⚙️ Configuração

### 🔹 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
