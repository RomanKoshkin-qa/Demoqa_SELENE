from selene import browser, be, have,command
from pathlib import Path

from pages.data import users
from pages.data.users import User


class RegistrationPage:  # ШАБЛОН
    def __init__(self):
        self.registered_user_data=browser.element('.table').all('td').even
        self.submit_button=browser.element("#submit")

    # def fill_first_name(self, value):
    #     browser.element('#firstName').type(value)
    #
    # def fill_second_name(self, value):
    #     browser.element('#lastName').type(value)

    def open(self):
        browser.open('/automation-practice-form')

        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.7)"')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)




    # browser.element('.table').all('td').should(
    #     have.texts(
    #         ('Student Name', 'Roman Koshkin'),
    #         ('Student Email', 'Roman@gmail.com'),
    #         ('Gender', 'Male'),
    #         ('Mobile', '9031234567'),
    #         ('Date of Birth', '11 May,1999'),
    #         ('Subjects', 'Maths'),
    #         ('Hobbies', 'Sports'),
    #         ('Picture', 'ones.png'),
    #         ('Address', 'Moscow Guena Street'),
    #         ('State and City', 'Haryana Karnal'),
    #     )
    # )
    def register(self, user:User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.submit()

    def submit(self):
        self.submit_button.click()

    def should_have_submited(self, first_name, last_name):
        pass


def test_tasks_demoqa():
    registration_page = RegistrationPage()
    registration_page.open()
    roma= users.roma
    # WHEN
    registration_page.register(roma)

    registration_page.submit()

    registration_page.should_have_submited(roma.first_name, roma.last_name)

    browser.element('#userEmail').type('Roman@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()  #.. это вверх подняться
    browser.element('#userNumber').type('9031234567')
    browser.element('#dateOfBirthInput').click()  # открыли календарь
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1999')
    browser.element(f'.react-datepicker__day--0{11}').click()
    browser.element('#subjectsInput').type("Maths").press_enter()  # Subjects
    hobby_label = browser.element('label[for="hobbies-checkbox-1"]') #Hobbies
    browser.execute_script("arguments[0].click();", hobby_label.locate())
    file_path = Path(__file__).parent / "ones.png"
    browser.element('#uploadPicture').send_keys(str(file_path))
    browser.element('#currentAddress').type('Moscow Guena Street')
    browser.element('#state').click()
    # ^id начинается с react-select и внутри есть option, выбираем из них по тексту(exact)
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()
    browser.element("#submit").click()

    # THEN

    registration_page.registered_user_data.should(
         have.exact_texts(
        'Roman Koshkin',
        'Roman@gmail.com',
        'Male',
        '9031234567',
        '11 May,1999',
        'Maths',
        'Sports',
        'ones.png',
        'Moscow Guena Street',
        'Haryana Karnal',
    )
     )


    browser.quit()
