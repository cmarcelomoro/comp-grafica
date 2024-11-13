import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import trimesh
import numpy as np

# Classe para carregar o modelo .obj
class ModelLoader:
    def __init__(self, file_path):
        self.mesh = trimesh.load(file_path, force='mesh')
    
    def get_mesh_data(self):
        vertices = np.array(self.mesh.vertices)
        faces = np.array(self.mesh.faces)
        return vertices, faces

# Função para desenhar o modelo na tela
def draw_model(vertices, faces):
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex_index in face:
            glVertex3fv(vertices[vertex_index])  # Vértice
    glEnd()

# Função principal que roda a janela e controla o loop de renderização
def main():
    # Caminho do modelo 3D
    model_path = "C:/Users/Pichau/trab_importacao/models/MissileAGM-65/Files/Missile AGM-65.obj"
    
    # Inicializa o carregador de modelo
    loader = ModelLoader(model_path)
    vertices, faces = loader.get_mesh_data()

    # Inicia Pygame e OpenGL
    pygame.init()
    display = (1400, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Defini parâmetros da câmera
    gluPerspective(45, (display[0] / display[1]), 0.1, 150.0)
    glTranslatef(0.0, -4.0, -100)

    # Controle da rotação
    rotation_x = 0

    # Loop principal do PyGame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Aplica a rotação no eixo X
        rotation_x += 1
        glPushMatrix()  # Salva o estado atual da transformada
        glRotatef(rotation_x, 1, 0, 0)  # Aplica rotação no eixo X

        # Desenha o modelo
        draw_model(vertices, faces)

        # Restaura a matriz de transformada
        glPopMatrix()

        # Atualiza a tela
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
