# Import modułu pygame
import pygame

# inicjalizacja modułu pygame
pygame.init()

# Utworzenie okna o określonych wymiarach

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# nadanie nazwy oknu
pygame.display.set_caption("Pierwsza gra")

# utworzenie zegara, który nadzoruje stałe wartości fps
clock = pygame.time.Clock()

# zmienna określająca, czy należy zamknąć okno
game_status = True

# kod wykonywany póki aplikacja jest uruchomiona
while game_status:

      # odczytywanie zdarzeń zarejestrowanych przez komputer
      events = pygame.event.get() 

      for event in events:
            # Naciśnięto X - zamykanie aplikacji
            if event.type == pygame.QUIT:
                  game_status = False

      # Odświeżanie wyświetlanego okna
      pygame.display.update()

      # ustawiamy fps
      clock.tick(60)

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()

