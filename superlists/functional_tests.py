from selenium import webdriver
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
        self.fail('Finish the test')

#Bad thought that he should enter a to-do item right now

#He types "Continue with Node.js"

# after entering enter, the page is being refreshed and 
#the new item is being shown.

#That's cool, so bad decide to add another one:
#This time he chooses "Go go go with Golang but don't forget
# the python¡s goat!"

#another update of the page and it's now showing both items.

#Bad is now being suspicious, does the web page will remember his list?
#Apparently, a unique URL has been generated, let's try out

#Indeed, visiting this URL show me my to-do list.

#satisfied, Bad decides to go back to it's python's goat.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
