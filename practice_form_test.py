import os
from selene import have, command
from selene.support.shared import browser
from selenium.webdriver.common.by import By

def test_successful_input_Registration_Form(self=None):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()

    browser.element('[id=firstName]').type('Michael')
    browser.element('[id=lastName]').type('Kors')
    browser.element('[id = userEmail]').type('Michael@Kors.com')
    browser.element('[name=gender][value=Male]').double_click()
    browser.element('[id = userNumber]').type('8667095677')

    # Date of Birth
    browser.element('#dateOfBirthInput').press()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1959"]').click()
    browser.element('div[aria-label="Choose Sunday, August 9th, 1959"]').click()

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').type(os.getcwd()+"/solution.png")
    browser.element('[id = currentAddress]').type('Rodriguez side, LA 93111')

    #State and City
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()

    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Uttar Pradesh')).click()
    # browser.all('[id^=react-select-4-input][id*=option]').click()
    # browser.all('[id^=react-select-4-input][id*=option]').element_by(have.exact_text('Agra'))


    browser.element('[id=submit]').click()
    browser.element('[id =closeLargeModal]').click()


