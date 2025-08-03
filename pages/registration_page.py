from pathlib import Path

from selene import browser, have, command


class RegistrationPage:  # ШАБЛОН

    def open(self):
        browser.open('/automation-practice-form')

        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.7)"')
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

    def fill_hobbies(self, kind_of_hobbies):
        if kind_of_hobbies == 'Sports':
            hobby_label = browser.element('label[for="hobbies-checkbox-1"]')  # Hobbies
            browser.execute_script("arguments[0].click();", hobby_label.locate())
        elif kind_of_hobbies == 'Reading':
            hobby_label = browser.element('label[for="hobbies-checkbox-2"]')  # Hobbies
            browser.execute_script("arguments[0].click();", hobby_label.locate())
        elif kind_of_hobbies == 'Music':
            hobby_label = browser.element('label[for="hobbies-checkbox-3"]')  # Hobbies
            browser.execute_script("arguments[0].click();", hobby_label.locate())

    def fill_state(self, value):
        # ^id начинается с react-select и внутри есть option, выбираем из них по тексту(exact)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        browser.element('#city').click()

    def fill_city(self, value):
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def fill_uploadPicture(self, name_file):
        file_path = Path(__file__).parent / name_file
        browser.element('#uploadPicture').send_keys(str(file_path))
