from playwright.sync_api import sync_playwright, Playwright
# from playwright.async_api import async_playwright, Playwright
import asyncio
import pytest
from pprint import pprint
import json
from pathlib import Path

from tests.deneme.steps import * # important part of framework. Having more module like this is better for organisation.
                                 # You can either create one file or more file to keeps steps.
                                 # And "*" seymbols  means import everything. 


@pytest.fixture
def context_config(scope ="session", autouse = True):
    """Create and return a context for page creation."""
    preferences_path = Path("./tests/user_data_directory/Default/Preferences") #This is where we try to configure our browser via
                                                                               #preferences json file
    # with preferences_path.open("r", encoding="utf-8") as file: # In case you need to change browser settings.
    #         preferences = json.load(file)
            # preferences["translate_blocked_languages"] = "tr", "en"
            # print(json.dumps(preferences, indent=4))

    user_data_dir="../github_denemesi/tests/user_data_directory" 
    options = { "headless" : True, 
                "no_viewport": True, 
                "args":["--start-maximized"] 
              }
    #, "--disable-translate",  "--disable-features=Translate"
    #  "--disable-features=TranslateToast, TranslateTrigger, LensOverlayTranslateButton, ReadAnythingTranslateEntryPoint"

    return [user_data_dir , options] # We return the configuration for context of browser here.


@pytest.fixture
def browser(playwright: Playwright, context_config : list, scope="session", autouse = True):
    """Create and return a browser"""
    browser_set = playwright.chromium
    browser = browser_set.launch_persistent_context(context_config[0], **context_config[1])
    yield browser
    browser.close()

# @pytest.fixture # SPARE BROWSER SETUP IN CASE OF  ANY ERROR ARISE
# def browser(context_config : list, scope="session", autouse = True):
#     """Create and return a browser"""
#     playwright =sync_playwright().start()
#     browser_set = playwright.chromium
#     browser = browser_set.launch_persistent_context(context_config[0], **context_config[1])
#     yield browser
#     browser.close()
#     playwright.stop()

@pytest.fixture
def yeni_sayfa(playwright:Playwright, autouse = True):#autouse make fixture executed when the code run.
    """Create and return a new browser page."""
    browser_set = playwright.chromium
    browser = browser_set.launch(
        headless = False,
        args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    return  page

@pytest.fixture
def sayfa(browser,scope ="session", autouse = True):
    """Create and return a new browser page using context."""
    page = browser.pages # We create many Tabs here
    for i in page[1:]: # We delete all the Tabs except one of them
        page[i].close()
    yield page[0]
    page[0].close()
    # page = browser.new_page()
    # yield page
    # page.close()



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
    print("\n" + scenario.name + " ---> ", end="")
    print (step, end="") 
    # request.getfixturevalue("sayfa").screenshot(path="../github_denemesi/tests/screenshot.png", full_page = True)

def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    # print(f"before_step_call is active for {step}")
    # request.getfixturevalue("sayfa").screenshot(path="../github_denemesi/tests/screenshot.png", full_page = True)
    pass

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    # print(f"\nafter_step is active for {step_func}")
    # request.getfixturevalue("sayfa").screenshot(path="../github_denemesi/tests/screenshot.png", full_page = True)
    pass

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    # print(f"\nstep_error is active for {step}")
    pass

def pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception):
    # print(f"\nstep_function_lookup_error is active for {step}")
    pass
