from dataclasses import dataclass

from django.shortcuts import render
from dataclasses import dataclass

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver


# The function defined is called a ds. When this function is called, it will render an HTML file called `app_name.html`)
def ds(request):
    return render(request, 'ds.html', {})

# The function defined is called a **view function**. When this function is called,
# it will render an HTML file called `app_name.html`.
@dataclass
class DjangoScraper:
    def webdriver_setup(self):
        ff_opt = Options()
        ff_opt.add_argument("--windows-size=1920,1080",
                            "--disable-gpu",
                            "--disable-extensions",
                            "--no-sandbox",
                            "--incognito",
                            # "--headless",
                            )
        driver = WebDriver(options=ff_opt)
        return driver

    def auto_login(self, driver, url, username, password):
        driver.get(url)
        password_input = driver.find_element_by_xpath("//input[@type='password']")
        password_input.send_keys(password)
        username_input = password_input.find_element_by_xpath(
            ".//preceding::input[not(@type='hidden')]")
        username_input.send_keys(username)
        form_element = password_input.find_element_by_xpath(".//ancestor::form")
        submit_button = form_element.find_element_by_xpath(
            ".//*[@type='submit']").click()
        return driver

    def scrap(request):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)

        USERNAME = os.getenv("USERNAME")
        PASSWORD = os.getenv("PASSWORD")

        autologin(driver, 'https://maya.um.edu.my/sitsvision/wrd/siw_lgn',
                  USERNAME, PASSWORD)