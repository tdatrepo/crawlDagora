from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import time
import sys
# Replace 'path_to_chromedriver' with the path to your chromedriver executable
options = Options()
options.add_argument("--headless=new")
options.add_argument('--blink-settings=imagesEnabled=false')
driver = webdriver.Chrome(options=options)
data = []
num_from = int(sys.argv[1])
num_to = int(sys.argv[2])
list_zodiac = ['cat', 'dragon']
for i in range(num_from, num_to):
    url = f'https://dagora.xyz/detail/viction/0xd1C67Eb87DE7567Add0f7aE5C835B2DF07e3D139/{i}'
    try:
        driver.get(url)
        check_name = driver.find_element("xpath", "/html/body/main/div/div[1]/div[2]/h1").text.split('-')
        if len(check_name) > 1:
            name = check_name[1].strip().lower()
            if name in list_zodiac:
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/a"))
                    )
                    address = element.get_attribute('href').split('/')[-1]
                except:
                    pass
                is_own = True if address == '0xBf5fAE4c0B5c0f26320D9c572201D47D4E682b60' else False
                is_monkey = True if name == 'monkey' else False
                result = {"id": i, "name": name, "address":address, "is_own": is_own, "is_monkey": is_monkey}
                data.append(result)
                print(result)
            else:
                print(i, 'not in list zodiac')
    except:
        print(url)
        continue
    time.sleep(0.5)
final = {
    'result': len(data),
    'data': data
}    
    # address = driver.find_element("xpath", "/html/body/main/div/div[1]/div[2]/div[1]/div/a").get_attribute('href').split('/')[-1]
# Now you can interact with the webpage using Selenium methods
# For example, let's print the title of the page
# print("Title of the page:", {"data":data})
# Convert and write JSON object to file
with open(f'dagora\{num_from}-{num_to}.json', "w") as outfile: # folder 'dagora' should existed
    json.dump(final, outfile)

# Close the browser window
driver.quit()