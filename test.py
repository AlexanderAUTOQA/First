from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  


driver = webdriver.Chrome()  
driver.implicitly_wait(10)  

try:  
    # Открываем страницу  
    driver.get('')  

    
    element = driver.find_element(By.ID, '')  
    print(element.text)  # Работа с элементом  

      
    wait = WebDriverWait(driver, 10)   
    button = wait.until(EC.element_to_be_clickable((By.ID, '')))  
    button.click()  

    # Пример ожидания, пока элемент не станет видимым  
    # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '')))  

finally:  
    driver.quit()  


    
    

    



