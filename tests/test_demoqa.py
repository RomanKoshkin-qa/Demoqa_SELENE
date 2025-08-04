from pages.data import users
from pages.registration_page import RegistrationPage


def test_tasks_demoqa():
    registration_page = RegistrationPage()
    registration_page.open()
    roma = users.roma
    registration_page.register_user(roma)
    registration_page.should_registered_user_with(roma)
