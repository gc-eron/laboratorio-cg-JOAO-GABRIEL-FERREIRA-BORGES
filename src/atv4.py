import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

col1.image(img)
col2.text(img.shape)
col2.text(img[100, 100]) #pixel [100,100]

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)

#col1: RGB em cinza
col1.image(img[:, :, 0], caption="R")
col1.image(img[:, :, 1], caption="G")
col1.image(img[:, :, 2], caption="B")

#col2: RGB separados
so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col2.image(so_r, caption="só R")

so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0
col2.image(so_g, caption="só G")

so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0
col2.image(so_b, caption="só B")


# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

#1º vértice - já feito
quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="amarelo")

#2º vértice - ciano
quad_ciano = np.zeros((80, 80, 3), dtype=np.uint8)
quad_ciano[:, :] = (0, 255, 255)
col1.image(quad_ciano, caption="ciano")

#3º vértice - magenta
quad_magenta = np.zeros((80, 80, 3), dtype=np.uint8)
quad_magenta[:, :] = (255, 0, 255)
col1.image(quad_magenta, caption="magenta")

#4º vértice - verde
quad_verde = np.zeros((80, 80, 3), dtype=np.uint8)
quad_verde[:, :] = (0, 255, 0)
col1.image(quad_verde, caption="verde")

#imagem lida em  BGR na col2
col2.image(img, channels="BGR", caption="trocado (BGR)")


# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)

#conversão para float
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

#col1 cálculo do cinza com média simples
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")

#col2 cálculo do cinza com média ponderada
ponderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col2.image(ponderada, caption="ponderada")
