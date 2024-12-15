from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_number: str
    birthday_date: dict[str:str]
    subject: str
    hobbies: dict[str:bool]
    file: str
    address: str
    state: str
    city: str


user_for_registration = User(
    first_name="Maxim",
    last_name="Titov",
    email="test@test.ru",
    gender="Male",
    user_number="7777777777",
    birthday_date={'year': '1983', 'month': 'February', 'day': '19'},
    subject="Maths",
    hobbies={"Sports": True, "Reading": False, "Music": False},
    file="image.jpg",
    address="City Name, Street Name",
    state="NCR",
    city="Noida"
)
