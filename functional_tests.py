from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
#What about doing a cool new online to-do app
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Let's check if the title and header mention to-do lists
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        

#Bad thought that he should enter a to-do item right now
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribut('placeholder'),
                        'Enter a To-Do item')
#He types "Continue with Node.js"
        inputbox.send_keys('Continue with Node.js')
# after entering enter, the page is being refreshed and
        inputbox.send_keys(Keys.ENTER)
#the new item is being shown.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Continue with Node.js' for row in rows)
        )

#That's cool, so bad decide to add another one:
#This time he chooses "Go go go with Golang but don't forget
# the python's goat!"

#another update of the page and it's now showing both items.

#Bad is now being suspicious, does the web page will remember his list?
#Apparently, a unique URL has been generated, let's try out

#Indeed, visiting this URL show me my to-do list.

#satisfied, Bad decides to go back to it's python's goat.
        self.fail('Finish the test')
if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()
