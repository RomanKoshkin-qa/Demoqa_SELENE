import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    year: str
    month: str
    day: str
    subject: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str

    def __init__(self, first_name, last_name, email, gender, mobile, year, month, day, subject, hobbies, picture,
                 address, state, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.year = year
        self.month = month
        self.day = day
        self.subject = subject
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
        self.state = state
        self.city = city


roma = User(first_name='Roman', last_name='Koshkin', email='Roman@gmail.com', gender='Male', mobile='9031234567',
            year='1999', month='May', day='11', subject='Maths', hobbies='Sports', picture='ones.png',
            address='Moscow Guena Street', state='Haryana', city='Karnal')
