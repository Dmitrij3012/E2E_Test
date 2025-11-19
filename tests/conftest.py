import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--incognito')
        browser = webdriver.Chrome(options=chrome_options)
        browser.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()
