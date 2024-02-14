import pytz
from datetime import datetime, timezone
tz = pytz.timezone('Europe/Moscow')
moscow_datetime = datetime.now(tz)


import pytest_html

import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function")
def driver_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_html_report_title(report):
    ''' modifying the title  of html report'''
    report.title = "Autocurse QA"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extras = extras


def pytest_html_results_table_header(cells):
    cells.insert(1, "<th>Description</th>")
    cells.insert(2, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(1, f"<td>{report.description}</td>")
    cells.insert(2, f'<td class="col-time">{moscow_datetime}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)