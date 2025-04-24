def is_weekend(day):
    return day == 6 or day == 7

def get_discount(amount):
    return amount * 0.10 * (amount >= 5000) + amount * 0.05 * (amount >= 1000 and amount < 5000)

# print(get_discount(5500))
# print(get_discount(1500))
# print(get_discount(500))
def describe_number(n):
    parity = ["четное", "нечетное"][n % 2]
    digits = ["однозначное", "двузначное", "трехзначное"][min(len(str(n)) - 1, 2)]
    return f"{parity} {digits} число"

# print(describe_number(24))

def convert_to_meters(unitNumber, lengthInUnits):
    coefficients = {1: 0.1, 2: 1000, 3: 1, 4: 0.001, 5: 0.01}
    return lengthInUnits * coefficients[unitNumber]

# print(convert_to_meters(3, 10))

def describe_age(age):
    names = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tired_af = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", 
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    ten, unit = divmod(age, 10)
    
    # Формируем текст числа
    num_text = (tired_af[ten] + " " + names[unit]).strip()
    
    # Выбираем окончание
    endings = ["лет", "год", "года", "года", "года", "лет", "лет", "лет", "лет", "лет"]
    ending = endings[unit] if unit != 1 or ten == 1 else endings[age % 10]
    
    return f"{num_text} {ending}"

# print(describe_age(32))
# print(describe_age(20))