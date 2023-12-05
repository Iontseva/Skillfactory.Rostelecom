from urllib.parse import urlparse

class BasePage(object):
    # Базовый класс страницы с объектами: веб-драйвер, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_redirect_uri_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

