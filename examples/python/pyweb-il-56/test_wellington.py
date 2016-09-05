from __future__ import print_function, division
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import unittest

class TestSearch(unittest.TestCase):
    def test_search(self):

        url = 'http://wellington.govt.nz/'
        driver = webdriver.Chrome()
        driver.get(url)

        size0 = driver.get_window_size()
        print(size0)
        #print(driver.get_window_size()) # {u'width': 1050, u'height': 829}
        #print(driver.get_window_position()) # {u'y': 45, u'x': 22}
        driver.maximize_window()
        size1 = driver.get_window_size()  # {u'width': 1050, u'height': 873}
        #print(size1)

        time.sleep(5)
        self.assertEqual(driver.title, 'Wellington City Council')

        header = driver.find_element_by_class_name('nav-header-aux')
        #print(header.text)
        assert header.is_displayed()
        a = header.find_element_by_css_selector('a[href="/do-it-online"]')
        self.assertEqual(a.text, 'Do it Online')


        driver.set_window_size(895, size1['height'])  # width, height
        time.sleep(5)
        header = driver.find_element_by_class_name('nav-header-aux')
        #print(header.text)
        assert not header.is_displayed()

        menu = driver.find_element_by_class_name('menu-title')
        assert not menu.is_displayed()


        driver.set_window_size(749, size1['height'])  # width, height
        time.sleep(5)
        header = driver.find_element_by_class_name('nav-header-aux')
        #print(header.text)
        assert not header.is_displayed()

        menu = driver.find_element_by_class_name('menu-title')
        assert menu.is_displayed()


        #a = driver.find_element_by_css_selector('a[href="/do-it-online"]')
        #print(a.text)

        driver.set_window_size(300, size1['height'])  # width, height
        time.sleep(5)

        driver.close()

if __name__ == "__main__":
    unittest.main()