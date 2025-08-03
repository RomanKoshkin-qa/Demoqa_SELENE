from selene import browser
from pages.registration_page import RegistrationPage


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
    registration_page.fill_hobbies('Sports')
    registration_page.fill_uploadPicture('ones.png')
    browser.element('#currentAddress').type('Moscow Guena Street')
    registration_page.fill_state('Haryana')
    registration_page.fill_city('Karnal')
    browser.element("#submit").click()
    # THEN
    registration_page.should_registred_user_with('Roman Koshkin', 'Roman@gmail.com',
                                                 'Male', '9031234567', '11 May,1999', 'Maths', 'Sports',
                                                 'ones.png', 'Moscow Guena Street', 'Haryana Karnal')

    browser.quit()
