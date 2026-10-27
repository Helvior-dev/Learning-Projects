import requests
import csv
import io

url = "https://raw.githubusercontent.com/toUpperCase78/formula1-datasets/refs/heads/master/Formula1_2025Season_Drivers.csv"
response = requests.get(url)

reader = list(csv.DictReader(io.StringIO(response.text)))

MENU = """Меню
1. Показать всех пилотов
2. Фильтр по команде
3. Фильтр по стране
4. Пилоты рождённые после 2000
5. Топ N пилотов по очкам
0. Выход

Введите цифру для продолжения: """


def all_pilots():  # Функция показа всех пилотов
    drivers = [driver["Driver"] for driver in reader]
    return drivers


def teams_pilots():  # Функция для показа пилотов по фильтру их команды
    com = set()
    for i in reader:
        com.add(i["Team"])
    teams = (
        input(
            f"Команды в пелетоне:\n{"\n".join(sorted(com))}\nВведите команду для фильтра пилотов (для показа названия всех команд введите - commands): "
        )
        .strip()
        .title()
    )
    if not teams or teams not in com:
        raise ValueError("Введеной команды нету в пелетоне!")
    team = [driver["Driver"] for driver in reader if driver["Team"] == teams]
    return team


def country_pilots():  # Функция для показа пилотов по фильтру страны их проживания
    cnt_pil = set()
    for i in reader:
        cnt_pil.add(i["Country"])
    country_settings = (
        input(
            f"Страны пилотов в пелетоне:\n{"\n".join(sorted(cnt_pil))}\nВведите страну для фильтра пиолотов: "
        )
        .strip()
        .title()
    )
    if not country_settings or country_settings not in cnt_pil:
        raise ValueError("Пилота с этой страной нету в пелетоне!")
    country = [
        [driver["Driver"], driver["Team"], driver["Career Points"]]
        for driver in reader
        if driver["Country"] == country_settings
    ]
    return country


def pilots_born_2000():  # Функция показа пилотов рожденных после 2000
    born = [
        driver["Driver"]
        for driver in reader
        if int(driver["Date of Birth"][-4:]) >= 2000
    ]
    return born


def top_points_pilots():  # Функция сортировки пилотов по очкам с выбором кол-ва пилотов
    num = int(input("Топ сколько пилотов: "))
    if num < 0 or num > 20:
        raise ValueError("Количество пилотов не может быть отрицательным или больше 20")
    points = sorted(reader, key=lambda x: float(x["Career Points"]), reverse=True)
    return [[p["Driver"], p["Team"], p["Career Points"]] for p in points[:num]]


n = int(input(MENU))
while n != 0:
    try:
        if n == 1:
            print(" - ".join(all_pilots()), "\n")
        elif n == 2:
            print(" - ".join(teams_pilots()), "\n")
        elif n == 3:
            for pilot_country in country_pilots():
                print(" - ".join(pilot_country), "\n")
        elif n == 4:
            print(" - ".join(pilots_born_2000()), "\n")
        elif n == 5:
            for point in top_points_pilots():
                print(" - ".join(point))
        else:
            print("Ошибка, повторите ввод ещё раз!")
    except ValueError as e:
        print(f"Ошибка: {e}")
    n = int(input(MENU))
