import numpy as np
import streamlit as st
def ampliar(imagem, fator=4):
    return imagem.repeat(fator, axis=0).repeat(fator, axis=1)


st.title("Fractal: Triângulo de Sierpinski")

k = st.slider("k", 1, 20, 4)

y, x = np.indices((64, 64))

#vértices do triângulo principal
x1, y1 = 32, 4
x2, y2 = 4, 60
x3, y3 = 60, 60


def padrao(x, y, k):
    denominador = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)

    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominador
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominador
    c = 1 - a - b

    dentro = (a >= 0) & (b >= 0) & (c >= 0)
    nivel = np.floor(-np.log2(np.maximum(a * b * c, 1e-9)) * k / 10)

    return np.where(dentro, (nivel * 32) % 256, 0)

imagem = padrao(x, y, k)
imagem = np.clip(imagem, 0, 255).astype(np.uint8)
st.image(ampliar(imagem, 4))
