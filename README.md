# 🤖 Detector de Formas com OpenCV

## Sobre o Projeto
Este é um projeto de Visão Computacional desenvolvido em Python com a biblioteca OpenCV. O programa utiliza a webcam para capturar vídeo em tempo real, processar os frames e identificar formas geométricas básicas como triângulos, quadrados, retângulos e círculos.

O objetivo deste projeto foi aplicar conceitos fundamentais de processamento de imagem para reconhecer padrões em um ambiente ao vivo.

---

## 📸 Demonstração

![b8ae3cad-96f0-4e72-8c5d-641ec606cced](https://github.com/user-attachments/assets/bbf9c6c0-3445-4832-a005-b0c37f9e0a04)

---

## ✨ Funcionalidades
-   Captura de vídeo em tempo real pela webcam.
-   Processamento de imagem para isolar formas (conversão para escala de cinza, desfoque e binarização).
-   Detecção de contornos das formas.
-   Classificação de formas com base no número de vértices (triângulo, quadrado, retângulo, círculo).
-   Exibição visual com o nome e o contorno da forma desenhados sobre o vídeo original.

---

## 🛠️ Tecnologias Utilizadas
-   **Python 3**
-   **OpenCV** - Para todas as funcionalidades de visão computacional.
-   **NumPy** - Para manipulação eficiente de arrays de imagem.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em sua máquina local.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Felicxio/Visao_computacional_com_cv2_projetos-.git](https://github.com/Felicxio/Visao_computacional_com_cv2_projetos-.git)
    ```
2.  **Navegue até a pasta do projeto:**
    ```bash
    cd Visao_computacional_com_cv2_projetos-
    ```
3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar
    python -m venv venv
    # Ativar (Windows)
    .\venv\Scripts\activate
    # Ativar (macOS/Linux)
    source venv/bin/activate
    ```
4.  **Instale as dependências:**
    ```bash
    pip install opencv-python numpy
    ```
5.  **Execute o script principal:**
    ```bash
    python main.py
    ```
Pressione 'q' na janela da webcam para encerrar o programa.
