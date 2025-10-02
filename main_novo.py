# VERSÃO CORRIGIDA E VERIFICADA

import cv2
import numpy as np
import time

print('Iniciando a Webcam...')
# Tente com 0 primeiro, se não funcionar, o teste provou que 1 deve funcionar.
cap = cv2.VideoCapture(0)
time.sleep(1.0) # Espera 1 segundo para a câmera iniciar

# Verifica se a câmera realmente abriu
if not cap.isOpened():
    print("Erro ao abrir a câmera no índice 0. TENTANDO ÍNDICE 1...")
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("ERRO FATAL: Não foi possível abrir a câmera. Verifique a conexão e os drivers.")
        exit() # Encerra o script se nenhuma câmera for encontrada

print("Câmera iniciada com sucesso!")

while True:
    ret, frame = cap.read()
    if not ret:
        print('Não foi possível capturar o frame. Encerrando...')
        break

    # ---------- INÍCIO DO PROCESSAMENTO DA IMAGEM ----------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 400:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)

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
            
            cv2.drawContours(frame , [approx], 0, color, 3)
            cv2.putText(frame, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # --- FIM DO PROCESSAMENTO DA IMAGEM ---

    cv2.imshow("Detector de Formas", frame)
    cv2.imshow('Imagem processada', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Encerrando o programa...')
        break

# Limpeza Final
cap.release()
cv2.destroyAllWindows()