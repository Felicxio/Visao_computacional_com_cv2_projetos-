import cv2

print(f"Usando OpenCV versão: {cv2.__version__}")

# Tenta abrir a câmera no índice 1 primeiro, depois no 0
cap = cv2.VideoCapture(0) 
if not cap.isOpened():
    print("Índice 1 falhou. Tentando abrir câmera no índice 0...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERRO FATAL: Não foi possível abrir a câmera em nenhum índice (0 ou 1).")
        exit()

print("Câmera aberta com sucesso!")
print("Pressione 'q' na janela da câmera para sair.")

while True:
    # Tenta ler um frame
    ret, frame = cap.read()

    # Se a leitura falhar, encerra o loop
    if not ret:
        print("Falha ao ler o frame da câmera.")
        break

    # Se a leitura for bem-sucedida, mostra o frame
    cv2.imshow('Teste da Webcam', frame)

    # Espera pela tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpeza final
print("Encerrando...")
cap.release()
cv2.destroyAllWindows()