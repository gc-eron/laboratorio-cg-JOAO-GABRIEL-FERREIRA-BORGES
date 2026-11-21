import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)


st.header("2. Brilho")
col1, col2 = st.columns(2)
fator_v = col1.slider("Brilho", 0.0, 2.0, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
v = hsv[:, :, 2].astype(float)
v = v * fator_v
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
nova = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
col1.image(img, caption="original")
col2.image(nova, caption="brilho")


st.header("7. Inspetor de pixel")
col1, col2 = st.columns(2)
altura, largura = img.shape[0], img.shape[1]
linha = col1.slider("Linha", 10, altura-11, altura//2)
coluna = col1.slider("Coluna", 10, largura-11, largura//2)
marcada = img.copy()
marcada[linha-10:linha+11, coluna] = (255, 0, 0)
marcada[linha, coluna -10:coluna +11] = (255, 0, 0)
col1.image(marcada, caption="pixel marcado")
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
col2.text(f"RGB: {img[linha, coluna]}")
col2.text(f"HSV: {hsv[linha, coluna]}")
vizinhanca = img[linha -5:linha +6, coluna -5:coluna +6]
ampliada = vizinhanca.repeat(20, axis=0).repeat(20, axis=1)
col2.image(ampliada, caption="vizinhança ampliada")


st.header("10. Negativo numa região")
col1, col2 = st.columns(2)
altura, largura = img.shape[0], img.shape[1]
y = col1.slider("y", 0, altura-1, altura//4)
x = col1.slider("x", 0, largura-1, largura//4)
t = col1.slider("tamanho", 10, largura, largura//3)
nova = img.copy()
regiao = nova[y:y + t, x:x + t]
negativo = 255 - regiao
nova[y:y + t, x:x + t] = negativo
col1.image(img[y:y +t, x:x +t], caption="região")
col2.image(nova, caption="negativo na região")


st.header("14. Só uma cor")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h_min, h_max = col1.slider("Faixa de H (só uma cor)", 0, 179, (100, 130))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
so_cor = img.copy()
fora = mascara == 0
so_cor[fora] = 0
col1.image(mascara, caption="máscara")
col2.image(so_cor, caption="só uma cor")


st.header("18. Padrão colorido")
col1, col2 = st.columns(2)
k = col1.slider("k", 1, 20, 4)
peso = col1.slider("Peso do padrão", 0.0, 1.0, 0.3)
altura, largura = img.shape[0], img.shape[1]
y, x = np.indices((altura, largura))
padrao = np.zeros((altura, largura, 3), dtype=np.uint8)
padrao[:, :, 0] = ((x // 2 + y) * k) % 256
padrao[:, :, 1] = ((x ** 2 - y) * k) % 256
padrao[:, :, 2] = ((x + y // 2) * k) % 256
mistura = np.clip(peso * padrao.astype(float) + (1 - peso) * img.astype(float), 0, 255).astype(np.uint8)
col1.image(padrao, caption="padrão")
col2.image(mistura, caption="mistura")


st.header("20. Pixel art")
col1, col2 = st.columns(2)
passo = col1.slider("Passo", 2, 40, 10)
reduzida = img[::passo, ::passo]
pixel_art = reduzida.repeat(passo, axis=0).repeat(passo, axis=1)
col1.image(img, caption="original")
col2.image(pixel_art, caption="pixel art")
