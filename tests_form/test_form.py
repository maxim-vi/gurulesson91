from pages.form_page import PracticeFormPage
from sources.user_data import user_for_registration


def test_form():
    practice_form_page = PracticeFormPage()

    practice_form_page.open_browser()
    practice_form_page.register_user(user_for_registration)
    practice_form_page.should_registered_user_with(user_for_registration)
