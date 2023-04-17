import os
from selene import have, command
from selene.support.shared import browser

def test_successful_input_registration_form():
    browser.open('/automation-practice-form')

    browser.element('[id = firstName]').type('Michael')
    browser.element('[id = lastName]').type('Kors')
    browser.element('[id = userEmail]').type('Michael@Kors.com')
    browser.element('[name = gender][value=Male]').double_click()
    browser.element('[id = userNumber]').type('8667095677')

    browser.element('#dateOfBirthInput').press()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1959"]').click()
    browser.element('div[aria-label="Choose Sunday, August 9th, 1959"]').click()

    browser.element('#subjectsInput').type("Chemistry").press_enter()
    browser.element('#subjectsInput').type("Maths").press_enter()
    browser.element('#subjectsInput').type("Physics").press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').type(os.getcwd()+"/solution.png")
    browser.element('[id = currentAddress]').type('Rodriguez side, LA 93111')

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Uttar Pradesh')).click()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    browser.element('#submit').perform(command.js.click)
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))


    browser.all('tbody tr').should(
        have.exact_texts('Student Name Michael Kors', 'Student Email Michael@Kors.com', 'Gender Male',
                         'Mobile 8667095677', 'Date of Birth 09 August,1959', 'Subjects Chemistry, Maths, Physics', 'Hobbies Sports, Reading',
                         'Picture solution.png', 'Address Rodriguez side, LA 93111', 'State and City Uttar Pradesh Agra'))


    browser.element('[id =closeLargeModal]').click()
