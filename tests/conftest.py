from playwright.sync_api import sync_playwright
import pytest
from pprint import pprint

from tests.deneme.steps import * # important part of framework. Having more module like this is better for organisation.
                                 # You can either create one file or more file to keeps steps.
                                 # And "*" seymbols  means import everything. 



# @pytest.fixture
# def yeni_sayfa(autouse = True):#autouse make fixture executed when the code run.
#     playwright = sync_playwright().start()
#     browser = playwright.chromium.launch()
#     page = browser.new_page()
#     return  page

@pytest.fixture
def sayfa(autouse = True):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir="../github_denemesi/tests/user_data_directory",
        headless=False,
        no_viewport= True,
        args=["--start-maximized"]
        )
    context =browser
    page = context.new_page()
    return page

# ----------------------HOOKs for PYTEST-BDD------------------------ WARNING : pytest also has its own hooks.

def pytest_bdd_before_scenario(request, feature, scenario):
    # print(f"\n\nbefore_scenario is active for {scenario.name}\n\n")
    pass
    
def pytest_bdd_after_scenario(request, feature, scenario):
    # print(f"\n\nafter_scenario is active for {feature.name}\n")
    # print("\n\n")
    # pprint("after_scenario is active for: " + feature.name + " ---> " + scenario.name)
    pass
    

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    # print(f"\nbefore_step is active for {step}")
    print(step)
    # request.getfixturevalue("sayfa").screenshot(path="../github_denemesi/tests/screenshot.png", full_page = True)

def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    # print(f"before_step_call is active for {step}")
    # request.getfixturevalue("sayfa").screenshot(path="../github_denemesi/tests/screenshot.png", full_page = True)
    pass

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    # print(f"\nafter_step is active for {step_func}")
    request.getfixturevalue("sayfa").screenshot(path="../github_denemesi/tests/screenshot.png", full_page = True)
    pass

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # print(f"\nstep_error is active for {step}")
    pass

def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    # print(f"\nstep_function_lookup_error is active for {step}")
    pass
