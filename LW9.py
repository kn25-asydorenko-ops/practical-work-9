import math

def min_steps(x: int, y: int) -> int:
    # Обчислюємо загальну відстань
    distance = y - x
    
    # Якщо початкова і кінцева точки збігаються, кроків не потрібно
    if distance == 0:
        return 0
        
    # Знаходимо цілу частину квадратного кореня з відстані
    k = int(math.isqrt(distance))
    
    # Визначаємо кількість кроків залежно від діапазону відстані
    if distance == k ** 2:
        return 2 * k - 1
    elif distance <= k ** 2 + k:
        return 2 * k
    else:
        return 2 * k + 1

# Перевірка на прикладах із зображення
examples = [(45, 48), (45, 49), (45, 50), (45, 51)]

for x, y in examples:
    print(f"x = {x}, y = {y} -> Кількість кроків: {min_steps(x, y)}")