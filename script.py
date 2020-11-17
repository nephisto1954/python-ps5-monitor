import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ps5Email import send_email_alert


def job():
    # basic variables
    url = "https://www.johnlewis.com/sony-playstation-5-console-with-dualsense-controller/white/p5115192"
    path = "./chromedriver"

    # set the browser
    driver = webdriver.Chrome(path)
    # make a call using the driver
    driver.get(url)

    # to remove the cookie spam
    search = driver.find_element_by_xpath(
        '//*[@id="pecr-cookie-banner-wrapper"]/div/div[1]/div/div[2]/button[1]'
    )
    search.send_keys(Keys.RETURN)

    # look for add to basket
    available = driver.find_elements_by_id("button--add-to-basket")
    if available:
        # add email sending method
        print("email me")
        send_email_alert()
    else:
        print("still unavailable")

    time.sleep(60)
    driver.close()


# scheduling process/setup
# schedule.every(10).seconds.do(job)
schedule.every(1).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
