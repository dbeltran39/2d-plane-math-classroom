def draw_hud(screen, font, angle, scale):

    text1 = f"Angle: {angle}°"
    text2 = f"Scale: {scale:.2f}"

    txt1 = font.render(text1, True, (0, 0, 0))
    txt2 = font.render(text2, True, (0, 0, 0))

    screen.blit(txt1, (20, 20))
    screen.blit(txt2, (20, 50))
