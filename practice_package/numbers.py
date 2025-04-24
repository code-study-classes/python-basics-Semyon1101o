import math

calculate_distance = lambda x, y: sum(1 for _ in range(x, y)) if x < y else 0
# print(calculate_distance(-3, 2))

calculate_segments = lambda a, b: math.floor(a / b)
# print(calculate_segments(16, 4))

calculate_digit_sum = lambda number: sum(map(int, str(abs(number))))
# print(calculate_digit_sum(47))
# print(calculate_digit_sum(-5))

round_to_multiple = lambda number, multiple: round(number / multiple) * multiple
# print(round_to_multiple(10, 6))

calculate_rect_area = lambda x1, y1, x2, y2: abs(x2 - x1) * abs(y2 - y1)
# print(calculate_rect_area(0, 0, 5, 3))
