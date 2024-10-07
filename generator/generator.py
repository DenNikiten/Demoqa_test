import os
import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('en_US')


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        last_name=faker_ru.last_name(),
        first_name=faker_ru.first_name(),
        age=random.randint(10, 80),
        salary=random.randint(18000, 250000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile_number=faker_ru.msisdn()
    )


def generated_file():
    path = os.getcwd() + rf'\file_test_{random.randint(0, 999)}.txt'
    with open(path, "w+") as file:
        file.write(f"Hello World{random.randint(0, 999)}")
    return file.name, path


def generated_subject():
    dict_subjects = {1: "Hindi", 2: "English", 3: "Maths",
                     4: "Physics", 5: "Chemistry", 6: "Biology",
                     7: "Computer Science", 8: "Commerce", 9: "Accounting",
                     10: "Economics", 11: "Arts", 12: "Social Studies",
                     13: "History", 14: "Civics"}
    return dict_subjects[random.randint(1, 14)]


def generated_color():
    colors = ["Red", "Blue", "Green", "Yellow", "Purple",
              "Black", "White", "Voilet", "Indigo",
              "Magenta", "Aqua"]
    data = random.sample(colors, random.randint(1, len(colors)))
    return data


def generated_colors():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple",
                    "Black", "White", "Voilet", "Indigo",
                    "Magenta", "Aqua"]
    )


def generated_time():
    hours = str(random.randint(0, 23)).rjust(2, '0')
    minute = str(random.randrange(0, 61, 15)).rjust(2, '0')
    return f"{hours}:{minute}"


def generated_date():
    yield Date(
        day=faker_en.day_of_month(),
        month=faker_en.month_name(),
        year=faker_en.year(),
        time=generated_time()
    )


