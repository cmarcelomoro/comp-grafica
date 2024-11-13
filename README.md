# comp-grafica

No código deste trabalho, você encontrará um programa em python que lê um arquivo .obj e renderiza ele na tela.

### Primeira etapa ###
Baixar o modelo de algum site de modelos 3d, e depois criar o arquivo python em um lugar conveniente.

![{AF1D587F-24C4-4387-934C-988BB81DFC19}](https://github.com/user-attachments/assets/cc876596-826e-4867-970c-ad43e308b878)

### Segunda etapa ###
No código, desenvolver um método que carregue o modelo. Ele precisa ler o arquivo .obj que está dentro da pasta files do modelo.

No caso, a classe ModelLoader é a responsável por isso.

![{2A5C09FD-BD0A-4A92-A350-AE83375BBC81}](https://github.com/user-attachments/assets/e5aaae1f-e8f8-4390-8bcf-86e2d23c1d63)

### Terceira etapa ###
Construir o método que desenha o modelo.
Este método usa vários triângulos, que são posicionados no espaço 3d de acordo com o arquivo .obj.

![{9CBC578F-92D4-4ACA-B159-B413E08D7DA5}](https://github.com/user-attachments/assets/548bccb7-0b33-4d9a-9246-29d0acfc0ee1)

No método main, é definida a localização do arquivo .obj, o tamanho da tela, e configurações de câmera e de movimentação do míssil.
