import random
import pygame

CLOUD_COLOR = (255, 255, 255)


def create_cloud(w, h):

    x = random.randint(-w // 4, w)
    y = random.randint(50, h - 250)

    parts = []

    for _ in range(random.randint(3, 6)):

        ew = random.randint(60, 120)
        eh = random.randint(35, 70)

        dx = random.randint(-40, 40)
        dy = random.randint(-20, 20)

        parts.append((x + dx, y + dy, ew, eh))

    speed = random.uniform(0.4, 1.2)

    return {"parts": parts, "speed": speed}


def update_clouds(clouds, width):

    for cloud in clouds:

        new_parts = []

        for (x, y, ew, eh) in cloud["parts"]:

            x += cloud["speed"]

            if x - ew > width:
                x = -ew

            new_parts.append((x, y, ew, eh))

        cloud["parts"] = new_parts


def draw_clouds(screen, clouds):

    for cloud in clouds:

        for (x, y, ew, eh) in cloud["parts"]:

            pygame.draw.ellipse(screen, CLOUD_COLOR, (x, y, ew, eh))
