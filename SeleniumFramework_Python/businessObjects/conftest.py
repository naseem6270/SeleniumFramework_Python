import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from frameworkstuffs.controller.BaseClass import BaseClass

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def classLevelSetUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name.casefold() == "chrome".casefold():
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif browser_name.casefold() == "edge".casefold():
        driver = webdriver.Edge(BaseClass.ROOT_PATH + "/resources/msedgedriver.exe")

    elif browser_name.casefold() == "firefox".casefold():
        driver = webdriver.Firefox(BaseClass.ROOT_PATH + "/resources/geckodriver.exe")

    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture()
def methodLevelSetUp():
    print('Before Method')
    yield
    print('After Method')

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.split("::")[-1]
            #tc_name = re.sub(r'\[.*\]', '', tc_name)
            file_name = BaseClass.ROOT_PATH+"/reports/screenshots/"+tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)