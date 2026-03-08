import pygame


BG_TOP = (135, 206, 235)
BG_BOTTOM = (25, 130, 200)


def make_sky_gradient_surface(w, h):

    surf = pygame.Surface((w, h)).convert()

    for i in range(h):

        t = i / h

        r = int(BG_TOP[0] * (1 - t) + BG_BOTTOM[0] * t)
        g = int(BG_TOP[1] * (1 - t) + BG_BOTTOM[1] * t)
        b = int(BG_TOP[2] * (1 - t) + BG_BOTTOM[2] * t)

        pygame.draw.line(surf, (r, g, b), (0, i), (w, i))

    return surf
