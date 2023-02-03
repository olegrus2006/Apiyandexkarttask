import os
import sys

import pygame
import requests

print("--------------------------------------------------")
print("Введите координаты в формате таком: 'coord1,coord2'")
coords = [str(float(i)) for i in input().split(",")]
print("Введите масштаб карты в формате таком: 'число,число'")
size = [str(float(i)) for i in input().split(",")]
try:
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&spn={size[0]},{size[1]}&l=map"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запишем полученное изображение в файл.
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    pygame.display.set_caption("API Big TASK")
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

    # Удаляем за собой файл с изображением.
    os.remove(map_file)
except Exception:
    print("Упс.. Что-то пошло не так... Проверь коррекность ввода")
