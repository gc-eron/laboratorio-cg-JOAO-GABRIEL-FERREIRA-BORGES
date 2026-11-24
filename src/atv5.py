import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
col1.image(img, caption="img")

so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255
col2.image(cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB), caption="H")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)

fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

fator_v = col1.slider("Brilho", 0.0, 2.0, 1.5)
v = hsv[:, :, 2].astype(float)
v = v * fator_v
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

giro = col2.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
girada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
col2.image(girada)


# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)

# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)

# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)
