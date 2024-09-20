from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  


driver = webdriver.Chrome()  
driver.implicitly_wait(10)  

try:  
    
    driver.get('https://www.qa-practice.com/elements/button/simple')  

    
    element = driver.find_element(By.ID, 'submit-id-submit')  
    print(element.text)  
      
    wait = WebDriverWait(driver, 10)   
    button = wait.until(EC.element_to_be_clickable((By.ID, 'submit-id-submit')))  
    button.click()  

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn btn-primary')))  

finally:  
    driver.quit()  


    
    

    



