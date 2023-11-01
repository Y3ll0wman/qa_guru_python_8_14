import allure

from selene import browser, be, have
from qa_guru_python_8_14 import resource


class RegistrationPage:

    def open(self):
        with allure.step('Открыть форму регистрации студента'):
            browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        with allure.step('Заполнить имя'):
            browser.element('#firstName').should(be.visible).type(value)

    def fill_last_name(self, value):
        with allure.step('Заполнить фамилию'):
            browser.element('#lastName').should(be.visible).type(value)

    def fill_email(self, value):
        with allure.step('Заполнить e-mail'):
            browser.element('#userEmail').should(be.visible).type(value)

    def choose_a_gender(self):
        with allure.step('Выбрать пол'):
            browser.element('[for=gender-radio-1]').should(be.visible).click()

    def fill_telephone_number(self, value):
        with allure.step('Заполнить телефонный номер'):
            browser.element('#userNumber').should(be.visible).type(value)

    def choose_date_of_birth(self, month, year, day):
        with allure.step('Заполнить дату рождения'):
            browser.element('#dateOfBirthInput').should(be.visible).click()
            browser.element('.react-datepicker__month-select').should(be.visible).click()
            browser.element(f'.react-datepicker__month-select > option:nth-child({month})').should(be.visible).click()
            browser.element('.react-datepicker__year-select').should(be.visible).click()
            browser.element(f'.react-datepicker__year-select > option:nth-child({year})').should(be.visible).click()
            browser.element(f'.react-datepicker__day.react-datepicker__day--{day}').should(be.visible).click()

    def choose_a_subject(self, value):
        with allure.step('Выбрать направление'):
            browser.element('#subjectsInput').should(be.visible).type(value).press_enter()

    def choose_a_hobby(self):
        with allure.step('Выбрать хобби'):
            browser.element('label[for=hobbies-checkbox-1]').should(be.visible).click()
            browser.element('label[for=hobbies-checkbox-2]').should(be.visible).click()
            browser.element('label[for=hobbies-checkbox-3]').should(be.visible).click()

    def upload_a_picture(self, value):
        with allure.step('Загрузить аватар'):
            browser.element('#uploadPicture').should(be.visible).type(resource.path(value))

    def type_current_address(self, value):
        with allure.step('Указать адрес'):
            browser.element('#currentAddress').should(be.visible).type(value)

    def choose_state(self, value):
        with allure.step('Указать страну'):
            browser.element("#react-select-3-input").should(be.visible).type(value).press_enter()

    def choose_city(self, value):
        with allure.step('Указать город'):
            browser.element("#react-select-4-input").should(be.visible).type(value).press_enter()

    def submit_form(self):
        with allure.step('Отправить форму'):
            browser.element("#submit").should(be.visible).click()

    def student_should_by_registred(self, full_name, email, gender, phone_number, date_of_birth, subject, hobby, picture, state, city):
        with allure.step('Проверить данные студента'):
            browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
                full_name,
                email,
                gender,
                phone_number,
                date_of_birth,
                subject,
                hobby,
                picture,
                state,
                city
            ))
