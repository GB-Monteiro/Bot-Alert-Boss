⚔️ Boss Alert OCR Bot (Discord)

Um bot para Lineage 2 (ou outros jogos similares) que monitora a tela em busca de Bosses vivos e envia alertas automaticamente em um canal do Discord usando OCR (Tesseract).

📌 Funcionalidades

Captura automática de uma região da tela (configurável).

Reconhecimento de texto com Tesseract OCR.

Detecta bosses específicos configurados na lista bosses_alvo.

Envia alertas no Discord quando um Boss for detectado.

Sistema de cooldown (5 min) para evitar spam do mesmo Boss.

Logs no terminal para acompanhar o funcionamento.

🛠️ Tecnologias utilizadas

Python 3

PyAutoGUI
 → para capturar screenshots da tela.

Pillow (PIL)
 → para manipulação de imagens.

pytesseract
 → integração com o OCR Tesseract.

discord.py
 → integração com o Discord.

⚙️ Configuração
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

2. Instale as dependências
pip install -r requirements.txt

3. Instale o Tesseract OCR

Download Tesseract OCR

Durante a instalação, copie o caminho do executável e substitua no código:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

4. Configure seu Bot do Discord

Crie um bot no Discord Developer Portal
.

Pegue o Token e substitua no código:

TOKEN = "SEU_TOKEN_AQUI"


Copie o ID do canal do Discord e substitua:

CANAL_ID = 123456789012345678

5. Ajuste a região da tela

No código, altere REGIAO_BOSS para capturar corretamente a área onde aparecem os bosses:

REGIAO_BOSS = (x, y, largura, altura)

▶️ Executando o Bot

Após configurar tudo, basta rodar:

python bot.py

🖥️ Exemplo de funcionamento

Bot verifica a tela a cada 10 segundos.

Se detectar algum boss da lista:

Envia mensagem no Discord:

⚔️ Boss Queen Ant is alive! @everyone

📜 Licença

Este projeto é de uso pessoal/educacional.
Sinta-se livre para adaptar às suas necessidades!

✨ Feito com dedicação para facilitar a vida no farm de bosses!
