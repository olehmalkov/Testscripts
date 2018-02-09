# -*- coding: utf-8 -*-

import urllib
import os
import sys
import logging

from selenium import webdriver


def save_content(driver, extension):

    logging.info("DOWNLOAD %s ... ", extension)

    if extension not in ["jpg", "png", "gif", "js"]:
        raise Exception("Not supported!")

    tag = None
    if extension in ["jpg", "png", "gif"]:
        tag = 'img'
    elif extension == "js":
        tag = "script"

    #####################################################################

    if not os.path.exists("./download/" + extension):
        os.makedirs("./download/" + extension)

    #####################################################################

    elements = driver.find_elements_by_tag_name(tag)

    all_links = set([element.get_attribute("src") for element in elements])

    for link in all_links:

        file_name = str(link.split("/")[-1])

        if file_name.endswith(extension):

            try:
                urllib.urlretrieve(link, "./download/" + extension + "/" + file_name)
                logging.info("Downloaded successful = %s" % link)
            except IOError:
                logging.warning("CAN'T DOWNLOAD = %s" % link)


if __name__ == "__main__":

    assert len(sys.argv) == 2, "Please run script with argument. Example: task2.py http://www.walla.co.il"

    website = sys.argv[1]

    ###############################################################################

    logging.basicConfig(format='%(levelname)s: %(message)s', filename='task_log2.log', level=logging.INFO)

    ###############################################################################

    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    
    website = sys.argv[1]
    
    if "http://" not in website:
        website = "http://" + website
        
    browser.get(website)

    logging.info("Start to download...")

    save_content(driver=browser, extension="png")
    save_content(driver=browser, extension="jpg")
    save_content(driver=browser, extension="gif")
    save_content(driver=browser, extension="js")

    browser.quit()

    logging.info("Finish!")
