from qa_guru_python_8_14.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()

    # GIVEN
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Vasya')
    registration_page.fill_last_name('Vasilyev')
    registration_page.fill_email('example@example.com')
    registration_page.choose_a_gender()
    registration_page.fill_telephone_number('7999999999')
    registration_page.choose_date_of_birth(month='5', year='20', day='012')
    registration_page.choose_a_subject('Computer Science')
    registration_page.choose_a_hobby()
    registration_page.upload_a_picture('avatar.png')
    registration_page.type_current_address('Palace Square, 2, St Petersburg, 190000')
    registration_page.choose_state('NCR')
    registration_page.choose_city('Delhi')
    registration_page.submit_form()

    # THEN
    registration_page.student_should_by_registred(
        'Vasya Vasilyev',
        'example@example.com',
        'Male',
        '7999999999',
        '12 May,1919',
        'Computer Science',
        'Sports, Reading, Music',
        'avatar.png',
        'Palace Square, 2, St Petersburg, 190000',
        'NCR Delhi'
    )
