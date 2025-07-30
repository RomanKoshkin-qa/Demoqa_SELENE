from selene import browser, be, have
from pathlib import Path


def test_tasks_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Roman')
    browser.element('#lastName').type('Koshkin')
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
    browser.element('.table').all('td').should(
        have.texts(
            ('Student Name', 'Roman Koshkin'),
            ('Student Email', 'Roman@gmail.com'),
            ('Gender', 'Male'),
            ('Mobile', '9031234567'),
            ('Date of Birth', '11 May,1999'),
            ('Subjects', 'Maths'),
            ('Hobbies', 'Sports'),
            ('Picture', 'ones.png'),
            ('Address', 'Moscow Guena Street'),
            ('State and City', 'Haryana Karnal'),
        )
    )

    browser.quit()
