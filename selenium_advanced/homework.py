import os
import time
import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Advanced Selenium")
@allure.title("Test#1 - Checkbox clicks")
@allure.description("Checking the empty box and clicking on the checked box")
def test_checkbox(driver):
    url = "https://the-internet.herokuapp.com/checkboxes"
    driver.get(url)
    checkboxes = driver.find_elements(By.TAG_NAME, "input")
    for checkbox in checkboxes:
        initial_view = checkbox.is_selected()
        checkbox.click()
        assert checkbox.is_selected() != initial_view, "Checkbox position did not change after clicking"
        print(f"Checkbox selected? {checkbox.is_selected()}")
        time.sleep(2)


@allure.feature("Advanced Selenium")
@allure.title("Test#2 - JavaScript clicks")
@allure.description("Hovering over the blocks")
def test_javascript_clicks(driver):
    url = "https://the-internet.herokuapp.com/hovers"
    driver.get(url)
    hovers = driver.find_elements(By.CSS_SELECTOR, ".figure img")
    actions = ActionChains(driver)
    for i, img in enumerate(hovers):
        actions.move_to_element(img).perform()
        print(f"Hovered over image number {i + 1}")
        assert img.is_displayed(), f"The Hover {i + 1} is not performing!"
        time.sleep(2)


@allure.feature("Advanced Selenium")
@allure.title("Test#3 - Mouse Clicks")
@allure.description("Right-clicking the element and seeing the alert message")
def test_mouse_clicks(driver):
    url = "https://the-internet.herokuapp.com/context_menu"
    driver.get(url)
    right_click_element = driver.find_element(By.ID, "hot-spot")
    actions = ActionChains(driver)
    actions.context_click(right_click_element).perform()
    print("We just right-clicked")
    time.sleep(2)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    assert alert_text == "You selected a context menu", f"Different alert text: {alert_text}"
    alert.accept()
    print("Alert closed.")


@allure.feature("Advanced Selenium")
@allure.title("Test#4 - Keyboard Clicks")
@allure.description("Keyboard click in the input panel")
def test_keyboard_clicks(driver):
    url = "https://the-internet.herokuapp.com/key_presses"
    driver.get(url)
    form = driver.find_element(By.ID, "target")
    form.send_keys(Keys.SHIFT)
    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    assert "You entered: SHIFT" in result


@allure.feature("Advanced Selenium")
@allure.title("Test#5 - Input")
@allure.description("Inputting a specific number")
def test_input(driver):
    url = "https://the-internet.herokuapp.com/inputs"
    driver.get(url)
    field = driver.find_element(By.XPATH, "//input[@type='number']")
    number = "1000"
    field.send_keys(number)
    time.sleep(2)
    entered_text = field.get_attribute("value")
    print(f"Entered text: {entered_text}")
    assert entered_text == number, f"Expected '{number}', but got '{entered_text}'"


@allure.feature("Advanced Selenium")
@allure.title("Test#6 - Clearing the text")
@allure.description("Clearing the text inputted")
def test_input(driver):
    url = "https://the-internet.herokuapp.com/inputs"
    driver.get(url)
    field = driver.find_element(By.XPATH, "//input[@type='number']")
    number = "1000"
    field.send_keys(number)
    time.sleep(1)
    field.clear()
    assert field.get_attribute("value") == ""
    time.sleep(1)


@allure.feature("Advanced Selenium")
@allure.title("Test#7 - JavaScript Alerts")
@allure.description("Receiving the alert")
def test_alert(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    actions = ActionChains(driver)
    actions.click(button).perform()
    print("We just clicked the button")
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    assert alert_text == "I am a JS Alert", f"Different alert text: {alert_text}"
    alert.accept()
    print("Alert closed.")


@allure.feature("Advanced Selenium")
@allure.title("Test#8 - JavaScript Confirmation Alert")
@allure.description("Accepting and cancelling the confirmation alert")
def test_confirmation_alert(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    button.click()
    print("We just clicked the confirmation button")
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    assert alert_text == "I am a JS Confirm", f"Different alert text: {alert_text}"
    alert.accept()
    print("Alert closed.")


def test_cancel_confirmation_alert(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    button.click()
    print("We just clicked the confirmation button")
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    assert alert_text == "I am a JS Confirm", f"Different alert text: {alert_text}"
    alert.dismiss()
    time.sleep(2)
    result = driver.find_element(By.ID, "result")
    assert result.text == "You clicked: Cancel", f"Different result: {result.text}"


@allure.feature("Advanced Selenium")
@allure.title("Test#9 - JavaScript Prompt Alert")
@allure.description("Accepting and cancelling the prompt alert")
def test_prompt_alert(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    button.click()
    print("We just clicked the prompt button")
    time.sleep(1)
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert text: {alert_text}")
    assert alert_text == "I am a JS prompt", f"Different alert text: {alert_text}"
    alert.send_keys('Masha Bodowskaya')
    alert.accept()
    time.sleep(1)
    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: Masha Bodowskaya", f"Different result: {result.text}"


def test_cancel_prompt_alert(driver):
    url = "https://the-internet.herokuapp.com/javascript_alerts"
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    button.click()
    print("We just clicked the prompt button")
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.dismiss()
    time.sleep(1)
    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: null", f"Different result: {result.text}"


@allure.feature("Advanced Selenium")
@allure.title("Test#10 - Working with Tabs")
@allure.description("By clicking on the Click Here link, there new tab will be opened")
def test_working_with_tabs(driver):
    url = "https://the-internet.herokuapp.com/windows"
    driver.get(url)
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    time.sleep(1)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert driver.current_url == "https://the-internet.herokuapp.com/windows/new", \
        f"Expected URL was 'https://the-internet.herokuapp.com/windows/new', but got '{driver.current_url}'"
    print(f"Current URL: {driver.current_url}")



@allure.feature("Advanced Selenium")
@allure.title("Test#11 - Working with Iframe")
@allure.description("Switching to an iframe and verifying text content inside it")
def test_iframe(driver):
    url = "https://the-internet.herokuapp.com/iframe"
    driver.get(url)
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p"))
    )
    expected_text = "Your content goes here."
    actual_text = text.text
    print(f"Expected Text: {expected_text}. But received: {actual_text}")
    assert actual_text == expected_text, \
        f"Text mismatch: Expected '{expected_text}' but got '{actual_text}'"
    driver.switch_to.default_content()


@allure.feature("Advanced Selenium")
@allure.title("Test#12 - File Download")
@allure.description("Downloading the file by clicking on href")
def test_download(driver):
    url = 'https://the-internet.herokuapp.com/download'
    driver.get(url)
    href = driver.find_element(By.XPATH, '//*/a[contains(@href,"youtube_page.png")]')
    href.click()
    download_folder = os.path.expanduser("~/Downloads")
    downloaded_file = os.path.join(download_folder, "youtube_page.png")
    for _ in range(10):
        if os.path.exists(downloaded_file):
            print(f"The file is downloaded: {downloaded_file}")
            break
        time.sleep(1)
    else:
        assert False, f"File {downloaded_file} is not found!"


@allure.feature("Advanced Selenium")
@allure.title("Test#13 - File Upload")
@allure.description("Uploading the file by clicking on href")
def test_upload(driver):
    url = 'https://the-internet.herokuapp.com/upload'
    driver.get(url)
    file_path = os.path.expanduser("~/Downloads/youtube_page.png")
    choose_file_button = driver.find_element(By.ID, "file-upload")
    choose_file_button.send_keys(file_path)
    upload_button = driver.find_element(By.ID, "file-submit")
    upload_button.click()
    time.sleep(1)
    success_message = driver.find_element(By.TAG_NAME, "h3").text
    assert success_message == "File Uploaded!", f"but got '{success_message}'"
    print("File has been uploaded - test is complete!")