import pyautogui
import pytesseract
from PIL import Image
import discord
import asyncio
import time

# Caminho para o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Configurações do Discord
TOKEN = 'DISCORD_TOKEN'
CANAL_ID = 123456789  # Substitua pelo ID do canal

# Região da tela onde os bosses aparecem (x, y, largura, altura)
REGIAO_BOSS = (780, 395, 250, 90)  # Ajuste conforme sua tela  (x, y, altura, largura)

# Frequência de checagem (em segundos)
INTERVALO_CHECAGEM = 10  # Checagem a cada 10 segundos

# Lista dos bosses que queremos detectar
bosses_alvo = ["queen ant", "core", "zaken", "orfen"]

# Dicionário para controlar última notificação
ultima_notificacao = {}

# Função para tirar print da área dos bosses
def capturar_area_boss():
    imagem = pyautogui.screenshot(region=REGIAO_BOSS)
    imagem.save("bosses.png")
    return "bosses.png"


# Função para verificar quais bosses estão vivos
def verificar_bosses_vivos():
    caminho_img = capturar_area_boss()
    imagem = Image.open(caminho_img)
    texto = pytesseract.image_to_string(imagem)
    print("Texto OCR:\n", texto)

    bosses_vivos = []

    for linha in texto.split("\n"):
        linha_limpa = " ".join(linha.strip().split()).lower()

        for boss in bosses_alvo:
            if boss in linha_limpa:
                partes = linha_limpa.split(boss)
                depois_do_nome = partes[1].strip() if len(partes) > 1 else ""

                # Se não tiver nada depois do nome do boss
                if depois_do_nome == "":
                    bosses_vivos.append(linha.strip())  # Mantém o texto original

    return bosses_vivos


# Bot do Discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Set para manter controle dos bosses notificados recentemente
bosses_notificados = set()


@client.event
async def on_ready():
    print(f"🤖 Bot conectado como {client.user}")
    canal = client.get_channel(CANAL_ID)

    global bosses_notificados

    while True:
        print("🔍 Verificando bosses...")
        vivos = verificar_bosses_vivos()

        # Converter a lista para set para facilitar comparação
        vivos_set = set(vivos)

        for boss_linha in vivos_set:
            if boss_linha not in bosses_notificados:
                nome_detectado = None
                for nome_boss in bosses_alvo:
                    if nome_boss in boss_linha.lower():
                        nome_detectado = nome_boss.title()  # Use .title() só a primeira letra maiúscula
                        break

                if nome_detectado:
                    agora = time.time()
                    if (nome_detectado not in ultima_notificacao) or (agora - ultima_notificacao[nome_detectado] > 300): # 5min cooldown do mesmo boss para evitar que repita o alerta do mesmo boss a cada 10seg
                        await canal.send(f"⚔️ Boss **{nome_detectado}** is alive! @everyone")
                        ultima_notificacao[nome_detectado] = agora
                        print(f"✅ Notificado: {nome_detectado}")
                    else:
                        print(f"⏳ Ignorando {nome_detectado}, notificado há pouco tempo.")
        if not vivos:
            print("Nenhum boss vivo detectado.")

        await asyncio.sleep(INTERVALO_CHECAGEM)


client.run(TOKEN)
