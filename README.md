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

## ⚙️ Configuração

### 🔹 Clone o repositório

<pre>git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo</pre>

---

### 🛠️ Tecnologias
- 🐍 **Python 3**
- 📸 **PyAutoGUI** → captura da tela  
- 🖼️ **Pillow (PIL)** → manipulação de imagens  
- 🔎 **pytesseract** → OCR para reconhecimento de texto  
- 🤖 **discord.py** → integração com o Discord  

---

### 🔹 Instale as dependências
<pre>pip install -r requirements.txt</pre>

---

### 🔹 Instale o Tesseract OCR

* Baixe e instale: Tesseract OCR

* Copie o caminho do executável e configure no código:

<pre>pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'</pre>

---

### 🔹 Configure o Bot do Discord

1. Crie um bot no Discord Developer Portal

2. Pegue o TOKEN e substitua no código:

<pre>TOKEN = "SEU_TOKEN_AQUI"</pre>

3. Copie o ID do canal do Discord e substitua:

<pre>CANAL_ID = 123456789012345678</pre>

---

### 🔹 Ajuste a região da tela

Defina a área onde aparecem os bosses:

<pre>REGIAO_BOSS = (x, y, largura, altura)</pre>

---

### ▶️ Executando o Bot

Após tudo configurado, basta rodar:

<pre>python bot.py</pre>

---

### 🖥️ Exemplo de funcionamento

A cada 10 segundos, o bot faz a leitura da tela.
Se encontrar um Boss, envia para o Discord:

<pre>⚔️ Boss Queen Ant is alive! @everyone</pre>

---

### 📜 Licença

📌 Este projeto é para uso pessoal.
Sinta-se livre para modificar e adaptar conforme suas necessidades.

## ✨ Desenvolvido com dedicação para ajudar no farm de bosses no Lineage 2!
