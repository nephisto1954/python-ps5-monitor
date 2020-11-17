import os
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ps5Email import send_email_alert


def job():

    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")

    driver = webdriver.Chrome(
        executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op
    )

    driver.get("https://www.youtube.com")
    print(driver.page_source)

    # # basic variables
    # url = "https://www.johnlewis.com/sony-playstation-5-console-with-dualsense-controller/white/p5115192"
    # path = "./chromedriver"

    # # set the browser
    # driver = webdriver.Chrome(path)
    # # make a call using the driver
    # driver.get(url)

    # available = driver.find_elements_by_id("button--add-to-basket")

    # if available:
    #     # add email sending method
    #     print("email me")
    #     send_email_alert()
    # else:
    #     print("still unavailable")

    # # look for add to basket
    # while not available:
    #     Keys.TAB
    #     Keys.RETURN

    #     time.sleep(20)
    #     driver.quit()
    #     # # to remove the cookie spam
    #     # for x in xPaths:
    #     #     search = driver.find_element_by_xpath(x)
    #     #     search.send_keys(Keys.RETURN)


# scheduling process/setup
schedule.every(10).seconds.do(job)
# schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
