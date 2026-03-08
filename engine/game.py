import pygame

from .sky import make_sky_gradient_surface
from .clouds import create_cloud, update_clouds, draw_clouds
from .hud import draw_hud

# FUNCIONS DELS ALUMNES
from activities.rotation_and_translation import translacio, gir

WIDTH = 1000
HEIGHT = 700


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Activitat 1 - Moviments al pla")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)

        # sky
        self.sky = make_sky_gradient_surface(WIDTH, HEIGHT)

        # clouds
        self.clouds = [create_cloud(WIDTH, HEIGHT) for _ in range(7)]

        # sprite
        self.airplane_original = pygame.image.load(
            "assets/avio_vermell.png"
        ).convert_alpha()

        self.airplane_image = self.airplane_original
        self.airplane_rect = self.airplane_image.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        # estat matemàtic
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.angle = 0


    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return False

        return True


    def update(self):

        update_clouds(self.clouds, WIDTH)

        keys = pygame.key.get_pressed()

        # TRANSLACIÓ

        if keys[pygame.K_w]:

            self.x, self.y = translacio(
                self.x,
                self.y,
                0,
                -5
            )

        if keys[pygame.K_s]:

            self.x, self.y = translacio(
                self.x,
                self.y,
                0,
                5
            )

        # GIR

        if keys[pygame.K_a]:
            self.angle += 3

        if keys[pygame.K_d]:
            self.angle -= 3

        # aplica rotació al sprite

        rotated = pygame.transform.rotate(
            self.airplane_original,
            self.angle
        )

        self.airplane_image = rotated

        self.airplane_rect = rotated.get_rect(
            center=(self.x, self.y)
        )

    def draw(self):

        self.screen.blit(self.sky, (0, 0))

        draw_clouds(self.screen, self.clouds)

        self.screen.blit(self.airplane_image, self.airplane_rect)

        draw_hud(self.screen, self.font, self.angle, 1.0)

        pygame.display.flip()

    def run(self):

        running = True

        while running:

            self.clock.tick(60)

            running = self.handle_events()

            self.update()

            self.draw()

        pygame.quit()
