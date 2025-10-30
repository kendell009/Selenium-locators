import time


def highlight(element, color="blue", border=4, duration=2):
    """highlights (blinks) a selenium webdriver element"""
    driver = element.parent

    original_style = element.get_attribute("style")
    new_style = f"border: {border}px solid {color}; border-style: solid;"

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)
    time.sleep(duration)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)

