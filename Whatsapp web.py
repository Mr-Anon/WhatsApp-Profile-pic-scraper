from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import wget
import base64


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# options.add_argument("user-data-dir=/home/fsociety/.config/chromium/Default")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def scroll_to_end(wd, scroll_point):  
        wd.execute_script(f"window.scrollTo(0, {scroll_point});")
        time.sleep(2) 


driver.get("https://web.whatsapp.com/")
time.sleep(8)
driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div').click()
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# except:
#     driver.quit()

time.sleep(5)
scr1 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]')
myset = set()



i=1


for j in range(100):   
    images = driver.find_elements_by_tag_name("img")
    
    for image in images:
        # scroll_to_end(driver,i*1000)
        try:    
            image_src=image.get_attribute("src")
            print(image_src)
            result = driver.execute_async_script("""
                                var uri = arguments[0];
                                var callback = arguments[1];
                                var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
                                var xhr = new XMLHttpRequest();
                                xhr.responseType = 'arraybuffer';
                                xhr.onload = function(){ callback(toBase64(xhr.response)) };
                                xhr.onerror = function(){ callback(xhr.status) };
                                xhr.open('GET', uri);
                                xhr.send();
                                """, image_src)

            if type(result) == int :
                raise Exception("Request failed with status %s" % result)
                continue
            myset.add(result)
        

        
    
        # try:
        #     wget.download(image.get_attribute("src"),'/home/fsociety/Documents/selenium/images/')
        except:
            pass
    driver.execute_script("arguments[0].scrollTop += 200", scr1)

for result in myset:
    final_image = base64.b64decode(result)
    filename = 'images/'+str(i)+'.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(final_image)
        print("Saving "+filename+", Go To The Next Image")
    i=i+1
        