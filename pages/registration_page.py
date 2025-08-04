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

    def register_user(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()  # .. это вверх подняться
        browser.element('#userNumber').type(user.mobile)
        browser.element('#dateOfBirthInput').click()  # открыли календарь
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(f'.react-datepicker__day--0{user.day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()  # Subjects
        browser.all('#hobbiesWrapper label').element_by(have.exact_text(user.hobbies)).click()

        file_path = Path(__file__).parent / user.picture
        browser.element('#uploadPicture').send_keys(str(file_path))

        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click()
        # ^id начинается с react-select и внутри есть option, выбираем из них по тексту(exact)
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user.city)).click()
        browser.element("#submit").click()

    def should_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.mobile,
            f'{user.day} {user.month},{user.year}',
            user.subject,
            user.hobbies,
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        )
        )
