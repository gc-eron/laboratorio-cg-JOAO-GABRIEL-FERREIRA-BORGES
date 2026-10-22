import numpy as np
import streamlit as st
def ampliar(imagem, k=30):
	return imagem.repeat(k, axis=0).repeat(k, axis=1)
st.title("Imagem como matriz")
bandeira = np.ones([15, 21, 3], dtype=np.uint8) * 255

azul = (0, 45, 114)
vermelho = (206, 17, 38)
amarelo = (255, 204, 0)
verde = (0, 154, 68)

bandeira[0:7, :] = azul #metade azul

#linha vermelha do arco-íris
bandeira[3, 5:17] = vermelho
bandeira[4, 4] = vermelho
bandeira[4, 17] = vermelho
bandeira[5, 3] = vermelho
bandeira[5, 18] = vermelho
bandeira[6, 2] = vermelho
bandeira[6, 19] = vermelho
#linha amarela do arco-íris
bandeira[4, 5:17] = amarelo
bandeira[5, 4] = amarelo
bandeira[5, 17] = amarelo
bandeira[6, 3] = amarelo
bandeira[6, 18] = amarelo
#linha verde do arco-íris
bandeira[5, 5:17] = verde
bandeira[6, 4] = verde
bandeira[6, 17] = verde

bandeira[1,10] = amarelo #estrela
bandeira[6, 9:12] = amarelo #sol
bandeira[10, 8:13] = vermelho #cruz, linhas horizontais e verticais
bandeira[8:14,10] = vermelho

st.image(ampliar(bandeira, k=25))
