from selenium import webdriver


class test_Selenium:

    def test_demo1(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
