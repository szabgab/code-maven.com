from __future__ import print_function, division
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import unittest

class TestSearch(unittest.TestCase):
    def test_search(self):

        url = 'http://dbs.bh.org.il/'
        driver = webdriver.Chrome()
        driver.get(url)

        assert driver.title == 'BHS'

        # check the GitHub ribbon
        ribbon = driver.find_element_by_class_name('github-fork-ribbon')
        assert ribbon
        assert ribbon.get_attribute('href') == 'https://github.com/Beit-Hatfutsot/dbs-front/blob/dev/README.md'

        assert re.search(r'My Jewish Story', driver.page_source)

        #check the popup
        assert re.search(r'Welcome!', driver.page_source)

        # hide the popup
        button = driver.find_element_by_class_name('beta-notification__close')
        assert button
        button.click()
        assert not re.search(r'Welcome!', driver.page_source)


        # At first I directly selected the element with the 'title' class and the 'icon' class,
        # but then I found out that each menu item has both of those.
        # Then I went to the parent elements and there I found uniqueness.
        museum = driver.find_element_by_class_name('museum')
        assert museum.text == 'Museum'

        # Museum link
        elem = museum.find_element_by_class_name('title')
        assert elem.is_displayed()
        assert elem.text == 'Museum'

        # After a lot of sweating, I found that there is an 'icon' class which is replacing the 'title'
        icon = museum.find_element_by_class_name('icon')
        assert not icon.is_displayed()

        ActionChains(driver).move_to_element(elem).perform()

        time.sleep(1)
        elem = museum.find_element_by_class_name('title')
        #print(elem)
        assert not elem.is_displayed()
        icon = museum.find_element_by_class_name('icon')
        assert icon.is_displayed()

#        time.sleep(5)
        # TODO: click on the element when it is not in hover mode
        icon.click()
        assert driver.title == 'Home | Beit Hatfutsot'
        assert driver.current_url == 'http://www.bh.org.il/'

        driver.back()
        assert driver.title == 'BHS'
        assert driver.current_url == url


        #language_selector = driver.find_element_by_css_selector('img[alt="Select Language"]')
        language_selector = driver.find_element_by_class_name('language-icon')
        #print(language_selector)
        language_selector.click()
        # TODO: check the Hebrew version
        time.sleep(3)
        assert re.search(r'My Jewish Story', driver.page_source)
        driver.back()
        time.sleep(3)
        # TODO: hmm, why does this match while the browser still show the Hebrew version?
        assert re.search(r'My Jewish Story', driver.page_source)

        #time.sleep(5)
        #print(driver.content)
        #assert True

        driver.close()

if __name__ == "__main__":
    unittest.main()

