from pygame import*
window = display.set_mode((700,500))
display.set_caption("Ping")
background = transform.scale(image.load("venti.png"), (700, 500))
window.blit(background,(0, 0))
game = True
clock = time.Clock()
FPS = 120