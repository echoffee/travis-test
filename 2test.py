import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

br = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
br.get("http://webserver:80")
t = br.find_element_by_id("title")
print(t.text)
assert t.text == "Hello World"
f = br.find_element_by_id("fact")
print(f.text)
assert f.text == "OCaml > Python"
br.quit()
sys.exit(0)
