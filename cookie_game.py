import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

SLEEP_TIME_SECONDS = 1


def click_cookie(driver):
    driver.find_element_by_id('cookie').click()


def check_cookies_stache(driver):
    res = driver.find_element_by_id('money').text
    try:
        return int(res)
    except ValueError:
        return int(''.join(res.split(',')))


def get_cookie_classes(driver):
    total_items_list = []
    store_elements = driver.find_element_by_id('store')
    for elements in store_elements.text.split('\n'):
        if '-' in elements:
            total_items_list.append(elements.split(' -')[0])
    return dict.fromkeys(total_items_list, 0)


def check_what_to_buy(driver):
    buy_options = []
    for i in total_items_dict.keys():
        try:
            item = driver.find_element_by_id(f'buy{i}')
            if 'grayed' != item.get_attribute('class') and i != 'Cursor':
                buy_options.append(i)
        except:
            continue
    return buy_options


def buy(driver, buy_options):
    item_to_buy = random.randint(0, len(buy_options) - 1)
    # print(driver.find_element_by_id('buyElder Pledge').get_attribute('class'))
    try:
        if driver.find_element_by_id('buyElder Pledge').get_attribute('class') != 'grayed':
            item_to_buy = 'Elder Pledge'
            print('it appeared!')
        else:
            item_to_buy = random.randint(0, len(buy_options) - 1)
    except:
        pass
    finally:
        try:
            driver.find_element_by_id(('buy' + buy_options[item_to_buy])).click()
            print(f'bought: {buy_options[item_to_buy]}')
        except:
            pass


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
total_items_dict = get_cookie_classes(driver=driver)

while True:
    click_cookie(driver=driver)
    # print(check_cookies_stache(driver=driver))
    buy_available = check_what_to_buy(driver=driver)
    if buy_available:
        buy(driver=driver, buy_options=buy_available)

driver.quit()
