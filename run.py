from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
import getpass
from faker import Faker
fake = Faker()
copyrhigtx = """
888b    888 8888888888 88888888888 8888888888 888      8888888 Y88b   d88P 
8888b   888 888            888     888        888        888    Y88b d88P  
88888b  888 888            888     888        888        888     Y88o88P   
888Y88b 888 8888888        888     8888888    888        888      Y888P    
888 Y88b888 888            888     888        888        888      d888b    
888  Y88888 888            888     888        888        888     d88888b   
888   Y8888 888            888     888        888        888    d88P Y88b  
888    Y888 8888888888     888     888        88888888 8888888 d88P   Y88b 

                8888888b.     d8888 Y88b   d88P                            
                888   Y88b   d88888  Y88b d88P                             
                888    888  d88P888   Y88o88P                              
                888   d88P d88P 888    Y888P                               
                8888888P" d88P  888     888                                
                888      d88P   888     888                                
                888     d8888888888     888                                
                888    d88P     888     888                                
                    @author: corrykalam                           
                    @recode by lihdaf                                                            
"""  
print(copyrhigtx)
email = input("Input ur email: ")
password = "0000"
print("@1 Mobile/Phone Plan\n@2 Premium UHD Plan")
bills = input("Input selected plan <1/2>: ")
cvv = getpass.getpass("Input ur cc: ")#6011xxxxxxxxxxx|11|23|649
zipin = input("Use zip code <Y/n>: ")
if zipin == "y":
    zipins = input("Input your zip code: ")
datax = cvv.split("|")
chrome_optionsx = webdriver.ChromeOptions()
chrome_optionsx.add_argument("--incognito")
chrome_optionsx.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_optionsx.add_argument("--headless")
# chrome_optionsx.add_argument("--log-level=3")
driver = webdriver.Chrome("chromedriver path", options=chrome_optionsx) #example C:\\Users\\lihdaf\\Desktop\\chromedriver.exe
driver.get("https://www.netflix.com/")
print("Opening netflix.com")
emails = driver.find_element_by_id("id_email_hero_fuji")
emails.send_keys(email)
driver.find_element_by_class_name("cta-btn-txt").click()
time.sleep(5)
try:
    driver.find_element_by_class_name("nf-btn").click()
except:
    time.sleep(5)
    driver.find_element_by_class_name("nf-btn").click()
time.sleep(5)
try:
    driver.find_element_by_class_name("nf-btn").click()
except:
    time.sleep(5)
    driver.find_element_by_class_name("nf-btn").click()
time.sleep(5)
try:
    driver.find_element_by_class_name("nf-btn").click()
except:
    time.sleep(5)
    driver.find_element_by_class_name("nf-btn").click()
time.sleep(5)
print("Creating email password!!!")
pwd = driver.find_element_by_id("id_password")
pwd.send_keys(password)
pwd.send_keys(Keys.RETURN)
time.sleep(2)
try:
    driver.find_element_by_class_name("nf-btn").click()
except:
    time.sleep(5)
    driver.find_element_by_class_name("nf-btn").click()
time.sleep(5)
try:
    if bills == "1":
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/label[1]/span").click()
        driver.find_element_by_class_name("nf-btn").click()
        if zipin == "y":
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/footer/div/button").click()
    else:
        driver.find_element_by_class_name("nf-btn").click()
except:
    if bills == "1":
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/label[1]/span").click()
        driver.find_element_by_class_name("nf-btn").click()
        if zipin == "y":
            driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[3]/div/footer/div/button").click()
    else:
        driver.find_element_by_class_name("nf-btn").click()
time.sleep(5)
print("Go to payment method")
try:
    driver.find_element_by_class_name("mopNameAndLogos").click()
except:
    time.sleep(5)
    driver.find_element_by_class_name("mopNameAndLogos").click()
time.sleep(5)
b = driver.find_element_by_id("id_firstName")
b.send_keys(fake.name().split(" ")[0])
c = driver.find_element_by_id("id_lastName")
c.send_keys(fake.name().split(" ")[1])
if zipin == "y":
    g = driver.find_element_by_id("id_creditZipcode")
    g.send_keys(zipins)
d = driver.find_element_by_id("id_creditCardNumber")
d.send_keys(datax[0])
e = driver.find_element_by_id("id_creditExpirationMonth")
e.send_keys("%s%s"%(datax[1],datax[2]))
f = driver.find_element_by_id("id_creditCardSecurityCode")
f.send_keys(datax[3])
if zipin == "y":
    f.send_keys(Keys.RETURN)
    time.sleep(5)
else:
    driver.find_element_by_class_name("ui-binary-input").click()
    f.send_keys(Keys.RETURN)
    time.sleep(5)
if "Let's confirm your account." in driver.find_element_by_class_name("stepTitle").text:
    print("Whoops!! you got otp on this order!")
elif driver.find_elements_by_class_name("nf-message-contents"):
    print("There appears to be a problem with the payment method you are trying to use.")
else:
    driver.find_element_by_class_name("nf-btn").click()
    time.sleep(5)
    driver.find_element_by_class_name("nf-btn").click()
    time.sleep(5)
    driver.find_element_by_class_name("nf-btn").click()
    time.sleep(5)
    print("Succes created account and now premium!!")
