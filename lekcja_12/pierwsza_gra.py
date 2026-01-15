# Import modułu pygame
import pygame

# inicjalizacja modułu pygame
pygame.init()

# Utworzenie okna o określonych wymiarach

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Funkcje
def load_image(img_path: str, position):
      image = pygame.image.load(img_path)
      surface = image.convert()

      transparent_color = (0, 0, 0)
      surface.set_colorkey(transparent_color)

      rect = surface.get_rect(center=position)

      return [image, surface, rect]

def print_image(img_list):
      # [image, surface, rect]
      image, surface, rect = img_list
      screen_surface.blit(surface, rect)

def set_position_image(img_list, position):
      image, surface, rect = img_list
      rect = surface.get_rect(center=position)

      return [image,surface,rect]

def calculate_player_movement(keys):
      # Poruszanie postacią
      speed = 10
      delta_x = 0
      delta_y = 0

      if keys[pygame.K_w]:
            delta_y -= speed
      if keys[pygame.K_s]:
            delta_y += speed
      if keys[pygame.K_d]:
            delta_x += speed
      if keys[pygame.K_a]:
            delta_x -= speed

      return [delta_x, delta_y]

def limit_position(position):
      x, y = position
      # # # # # # # # # # # # # #
      # Rozwiązanie wstaw tutaj #
      # # # # # # # # # # # # # #
      return [x,y]


# Zmienne dla gracza
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('lekcja_12\player.png', player_pos)
background_color = [150, 223, 191]

# nadanie nazwy oknu
pygame.display.set_caption("Pierwsza gra")

# utworzenie zegara, który nadzoruje stałe wartości fps
clock = pygame.time.Clock()

# zmienna określająca, czy należy zamknąć okno
game_status = True

# kod wykonywany póki aplikacja jest uruchomiona
# ===== GŁÓWNA PĘTLA GRY ====
while game_status:

      # odczytywanie zdarzeń zarejestrowanych przez komputer
      events = pygame.event.get() 

      for event in events:
            # Naciśnięto X - zamykanie aplikacji
            if event.type == pygame.QUIT:
                  game_status = False

      pressed_keys = pygame.key.get_pressed()
      delta_x, delta_y = calculate_player_movement(pressed_keys)

      player_pos[0] += delta_x
      player_pos[1] += delta_y

      player = set_position_image(player, player_pos)

      # Uzupełnianie tła
      screen_surface.fill(background_color)

      # Wyświetlanie gracza
      print_image(player)

      # Odświeżanie wyświetlanego okna
      pygame.display.update()

      # ustawiamy fps
      clock.tick(60)

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()

