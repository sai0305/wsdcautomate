#created by Sai0305
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestOnesub():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_onesub(self):
    self.driver.get("https://wsdc.nitw.ac.in/")
    self.driver.set_window_size(1366, 728)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.LINK_TEXT, "Fill Feedback").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "courseFeedback1").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback1")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback1").click()
    self.driver.find_element(By.ID, "courseFeedback2").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback2")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback2").click()
    self.driver.find_element(By.ID, "courseFeedback3").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback3")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback3").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12").click()
    self.driver.find_element(By.ID, "courseFeedback4").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback4")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback4").click()
    self.driver.find_element(By.ID, "courseFeedback5").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback5")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback5").click()
    self.driver.find_element(By.ID, "courseFeedback6").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback6")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback6").click()
    self.driver.find_element(By.ID, "courseFeedback7").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback7")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback7").click()
    self.driver.find_element(By.ID, "courseFeedback8").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback8")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback8").click()
    self.driver.find_element(By.ID, "courseFeedback9").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback9")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback9").click()
    self.driver.find_element(By.ID, "courseFeedback10").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback10")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback10").click()
    self.driver.find_element(By.ID, "courseFeedback11").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback11")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback11").click()
    self.driver.find_element(By.ID, "courseFeedback12").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback12")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback12").click()
    self.driver.find_element(By.ID, "courseFeedback13").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback13")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback13").click()
    self.driver.find_element(By.ID, "courseFeedback14").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback14")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback14").click()
    self.driver.find_element(By.ID, "courseFeedback15").click()
    dropdown = self.driver.find_element(By.ID, "courseFeedback15")
    dropdown.find_element(By.XPATH, "//option[. = 'Good']").click()
    self.driver.find_element(By.ID, "courseFeedback15").click()
  
