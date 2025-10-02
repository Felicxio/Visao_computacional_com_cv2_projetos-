# DETECTOR DE FORMAS GEOMÉTRICAS COM OPENCV E WEBCAM
#Passo 1: Importação de bibliotecas para o projeto
import cv2
import numpy as np
import time 

#Passo 2: Inicialização da Webcam

print('Iniciando a Webcam...')

cap = cv2.VideoCapture(0) # OBJETO PARA CAPTURAR O VÍDEO, 0 SIGNIFICA A PRIMEIRA WEBCAM CONECTADA AO PC
time.sleep(1.0) #2 segundos para a câmera iniciar

#Passo 3: Loop principal, while true para criar um loop infinito que a cada iteração captura um frame da webcam e o processa.

while True:
    ret, frame = cap.read() # 'ret' é um retorno true ou false da leitura e 'frame' é a imagem (numpy array capturado).
    if not ret:
        print('Não foi possível capturar o frame. Encerrando...')
        break

# ---------- INÍCIO DO PROCESSAMENTO DA IMAGEM ----------

#1. Pré Processamento
#Convertendo o frame colorido para a escala de cinza com o intuito de simplificar a imagem.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#Aplicando desfoque para suavizar a imagem e reduzir ruído
    blur = cv2.GaussianBlur(gray, (5,5), 0)
#Binarizando a imagem: pixel abaixo de 127 ficam pretos, acima ficam brancos
#THRESH_BINARY_INV inverte isso

    _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)


#2. Encontrar Contornos: findContours busca por sequências de pontos que formam os contornos das formas brancas.

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#3. Analisar e desenhar cada contorno: Iteramos sobre a lista de todos os contornos encontrados.

    for cnt in contours:
        #filtrando contornos pequenos para evitar ruídos
        if cv2.contourArea(cnt) > 400:
            #aproximando o contorno para um polígono
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
            #obtemos as coordenadas para posicionar o texto com o nome da forma
            x, y, w, h = cv2.boundingRect(approx)

            #classificamos a forma pelo número de vértices do polígono aproximado.

            if len(approx) == 3:
                shape_name = 'Triangulo'
                color = (0, 255, 0) #verde
            elif len(approx) == 4:
                aspect_ratio = float(w)/ h
                if 0.95 <= aspect_ratio <= 1.05:
                    shape_name = 'Quadrado'
                else:
                    shape_name = 'Retangulo'
                color = (0, 150, 255) #laranja
            elif len(approx) > 7:
                shape_name = 'Circulo'
                color = (255, 0, 255) #magenta
            else:
                continue
            
            #Desenhamos o contorno e o nome da forma no frame original (colorido).
            cv2.drawContours(frame , [approx], 0, color, 3)
            cv2.putText(frame, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

# --- FIM DO PROCESSAMENTO DA IMAGEM ---

#4. Exibição dos resultados
#Mostramos o frame final com as detecções.
    cv2.imshow("Detector de Formas", frame)
#Também mostramos a imagem binarizada para entender o que o algoritmo está vendo
    cv2.imshow('Imagem processada', thresh)

#verificiamos se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Encerrando o programa...')
        break
    

#-------------------------------------------------------------------------------------
#Passo 4: Limpeza Final
#-------------------------------------------------------------------------------------

#Libera o dispositivo da webcam para que outros programas possam usá-lo
cap.release()
#fecha todas as janelas abertas pelo openCV
cv2.destroyAllWindows()

            