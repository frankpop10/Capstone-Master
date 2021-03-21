from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.proxy import Proxy, ProxyType


import webbrowser
import time
import json

def webscrape():
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = "3.114.241.246:8080"
    capabilities = webdriver.DesiredCapabilities.FIREFOX
    prox.add_to_capabilities(capabilities)
    browser = webdriver.Firefox(desired_capabilities=capabilities)
    url = 'https://www.google.com/'
    queryString = 'covid19'
    queryResults = []
    now = datetime.now()
    dt_string = [now.strftime("%m/%d/%Y %H:%M:%S")]
    browser.get(url)
    time.sleep(2)
    browser.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(queryString)
    time.sleep(4)
    results = browser.find_elements_by_xpath("//div[@class='sbtc']")
    count = 0
    # queryResults.append(dt_string)
    for i in results:
        if(i.text == ""):
            pass
        else:
            queryResults.append('Query_' + str(count))
            queryResults.append(i.text)
            count+=1
    queryResults.append("Date")
    b = iter(queryResults)
    queryDict = dict(zip(b, b))
    queryDict["Date/Time"] = dt_string
    li = r"C:/Users/thebr/iCloudDrive/code/python/captones/capstoneData.json"
    with open(li, "w") as f:
        json.dump(queryDict, f)
    browser.close()



if __name__ == '__main__':
    webscrape()
