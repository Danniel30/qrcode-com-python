# documentação: https://pypi.org/project/qrcode/
# Antes de importar o qrcode é necessário instalar no terminal o 'pip install qrcode'
import qrcode

redes_sociais = {
    "youtube": "https://youtube.com/channel/UC1fYLMmeZKVO1qPeB9K7PVQ",
    "Twich": "https://www.twitch.tv/devsfree?sr=a",
    "Instagram": "https://www.instagram.com/devsfree/",
    "Facebook": "https://www.facebook.com/devsfreeoficial",
    "Twitter": "https://twitter.com/DevsFreeOficial",
    "TikTok": "http://www.tiktok.com/@devsfrre",
    "VK": "https://vk.com/devsfree",
    "Linkedin": "https://www.linkedin.com/company/devsfree/"
}

# utilizando o for, podemos percorrer o dicionário e gerar o qrcode a cada laço
for valor, info in redes_sociais.items():  # A função items do dicionário vai trazer o valor e a informação do dicionário.
    img = qrcode.make(info)  # A função 'make' é responsável por gerar o dado informado em QR Code
    img.save(
        f"{valor}.png")  # A função 'save' salva o arquivo na pasta do projeto, e o '.png' converte o arquivo no formato desejado, pode se utilizar jpg também.

imagem_qrcode = qrcode.make("https://github.com/Danniel30")
img.show()  # A função 'show' exibe o qrcode em uma nova janela
