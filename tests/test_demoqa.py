from pathlib import Path

from selene import browser, have
from selene import command


class RegistrationPage:  # ШАБЛОН

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')
        '''
        # might be also needed:
        '''
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()  # открыли календарь
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def should_registred_user_with(self, first_and_second_name, email, gender, mobile, date_of_birth, subjects, hobbies,
                                   picture, address, state_and_city):
        browser.element('.table').all('td').should(
            have.texts(
                ('Student Name', f'{first_and_second_name}'),
                ('Student Email', f'{email}'),
                ('Gender', f'{gender}'),
                ('Mobile', f'{mobile}'),
                ('Date of Birth', f'{date_of_birth}'),
                ('Subjects', f'{subjects}'),
                ('Hobbies', f'{hobbies}'),
                ('Picture', f'{picture}'),
                ('Address', f'{address}'),
                ('State and City', f'{state_and_city}'),
            )
        )

    def fill_second_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)


    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()


def test_tasks_demoqa():
    registration_page = RegistrationPage()
    registration_page.open()
    # WHEN
    registration_page.fill_first_name('Roman')  # fill заполнить
    registration_page.fill_second_name('Koshkin')
    registration_page.fill_email('Roman@gmail.com')
    registration_page.fill_gender('Male')



    browser.element('#userNumber').type('9031234567')

    registration_page.fill_date_of_birth('1999', 'May', 11)

    browser.element('#subjectsInput').type("Maths").press_enter()  # Subjects
    hobby_label = browser.element('label[for="hobbies-checkbox-1"]')  # Hobbies
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
    registration_page.should_registred_user_with('Roman Koshkin', 'Roman@gmail.com',
    'Male', '9031234567','11 May,1999', 'Maths', 'Sports',
    'ones.png', 'Moscow Guena Street','Haryana Karnal')


    browser.quit()
