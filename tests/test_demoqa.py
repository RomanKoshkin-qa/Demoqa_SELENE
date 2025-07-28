from selene import browser, be
from pathlib import Path


def test_tasks_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Роман')
    browser.element('#lastName').type('Кошкин')
    browser.element('#userEmail').type('Roman@ya.ru')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('9031234567')
    # # работа с  календарем
    browser.element('#dateOfBirthInput').click()  # открыли календарь
    # #выбрали год
    browser.element('.react-datepicker__year-select').click()  # Кликнуть по селекту года
    option_element = browser.element('.react-datepicker__year-select option[value="2007"]')
    option_element.wait_until(be.present)
    option_element.click()
    # #выбираем месяц
    browser.element('.react-datepicker__month-select').click()  # Кликнуть по селекту года
    option_element = browser.element('.react-datepicker__month-select option[value="2"]')  # март
    option_element.wait_until(be.present)
    option_element.click()
    # #выбор дня
    browser.element('.react-datepicker__day--004').click()  # 4 марта
    browser.element('#subjectsInput').type("maths").press_enter()  # Выбор Maths
    # клик по hobbies
    hobby_label = browser.element('label[for="hobbies-checkbox-1"]')
    browser.execute_script("arguments[0].click();", hobby_label.locate())
    # загрузка файла
    file_path = Path(__file__).parent / "ones.png"  # Укажите правильный путь
    browser.element('#uploadPicture').send_keys(str(file_path))
    # адрес
    browser.element('#currentAddress').type('hello')
    browser.element("#react-select-3-input").type("NCR").press_enter()
    browser.element("#react-select-4-input").type("Delhi").press_enter()
    browser.element("#submit").click()

    browser.quit()
