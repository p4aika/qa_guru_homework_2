import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def set_browser_size():
    browser.config.window_width = 1900
    browser.config.window_height = 1080

def test_google_should_finde_text(set_browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_shuld_not_finde_text():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('testgoogleshuldnotfindetext').press_enter()
    browser.element('#topstuff').should(have.text('По запросу testgoogleshuldnotfindetext ничего не найдено.'))