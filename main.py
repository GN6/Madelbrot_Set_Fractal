from interface import get_iterations, Complex
import pygame


COLORS = ['black', 'red', 'red', 'black']
DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 1000, 800
MAX_ITERS = 300
FIDELITY = 4

def get_color(value):
    if value == MAX_ITERS: return pygame.Color(COLORS[-1])
    color, r = divmod(value * (len(COLORS) - 1), MAX_ITERS)
    return pygame.Color(COLORS[color]).lerp(pygame.Color(COLORS[color + 1]), r / MAX_ITERS)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    
    for i in range(DISPLAY_WIDTH):
        for j in range(DISPLAY_HEIGHT):
            x = get_iterations(Complex((i - 740) / 320, (j - 400) / 320), MAX_ITERS, FIDELITY)
            screen.set_at((i, j), get_color(x))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
