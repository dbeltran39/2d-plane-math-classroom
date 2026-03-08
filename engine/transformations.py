import pygame


def apply_translation(rect, dx, dy):

    cx, cy = rect.center

    rect.center = (cx + dx, cy + dy)

    return rect


def apply_rotation_scale(surface, rect, angle, scale, flip_h, flip_v):

    transformed = pygame.transform.rotozoom(surface, angle, scale)

    if flip_h or flip_v:
        transformed = pygame.transform.flip(transformed, flip_h, flip_v)

    new_rect = transformed.get_rect(center=rect.center)

    return transformed, new_rect


def apply_symmetry(flip_h, flip_v, axis):

    if axis == "x":
        flip_v = not flip_v

    if axis == "y":
        flip_h = not flip_h

    return flip_h, flip_v
