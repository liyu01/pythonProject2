import pytest
from selenium import webdriver


def test_demo1():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")


if __name__ == "__main__":
    test_demo1()
