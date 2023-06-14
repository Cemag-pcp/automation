# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# while True:

#     link1 = "https://app10.ploomes.com/login"
#     nav = webdriver.Chrome()
#     nav.get(link1)

#     wait = WebDriverWait(nav, 10)

#     # Email
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/div/input').click()
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[1]/div/input').send_keys("luan@cemag.com.br")

#     # Password
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[2]/div/input').click()
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[2]/div/input').send_keys('cemag2023')

#     # Entrar
#     nav.find_element(By.ID, 'centerRender').click()

#     button_novo = ''
#     while button_novo == '':
#         try:
#             print("carregando")
#             button_novo = nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/section/div/aside[2]/horizontal-menu/div/button')
#         except:
#             pass

#     # Clicar em Negócios
#     nav.find_element(By.XPATH, '//*[@id="modules"]/div[3]/div[2]/button').click()

#     # Clicar em funil de vendas
#     nav.get('https://app10.ploomes.com/Deals/funnel')
#     time.sleep(5)

#     # Clicar em nova venda
#     wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div[2]/main-wrapper/app-wrapper/div/section/div/aside[2]/div/div/aside/div/header/div/aside[3]/a'))).click()
#     # nav.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/main-wrapper/app-wrapper/div/section/div/aside[2]/div/div/aside/div/header/div/aside[3]/a').click()
#     time.sleep(5)

#     # Nome cliente
#     nav.find_element(By.CSS_SELECTOR, 'input[id^="select-fk-dealcontact-"]').send_keys("A coriolano")
#     time.sleep(2)

#     # Enter no cliente
#     nav.find_element(By.CSS_SELECTOR, 'input[id^="select-fk-dealcontact-"]').send_keys(Keys.ENTER)

#     # Nome contato
#     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="select-fk-dealperson-"]'))).click()
#     # nav.find_element(By.CSS_SELECTOR, 'input[id^="select-fk-dealperson-"]').click()
#     time.sleep(2)
#     wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id^="select-fk-dealperson-"]'))).send_keys(Keys.DOWN)
#     # nav.find_element(By.CSS_SELECTOR, 'input[id^="select-fk-dealperson-"]').send_keys(Keys.DOWN)
#     nav.find_element(By.CSS_SELECTOR, 'input[id^="select-fk-dealperson-"]').send_keys(Keys.ENTER)

#     # Salvar
#     nav.find_element(By.CSS_SELECTOR, 'button.button.button-action.pull-right').click()

#     button_propostas = ''
#     while button_propostas == '':
#         try:
#             print("Carregando")
#             button_propostas = nav.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/main-wrapper/app-wrapper/div/section/div/aside[2]/div/deal-page-wrapper/div/new-deal-page/div/div/section/div/aside[2]/div/div/deal-page-tabs/div/ul/li[2]')
#         except:
#             pass
#     time.sleep(2)

#     # Propostas
#     nav.find_element(By.XPATH, '//*[@id="react-root"]/div/div[2]/main-wrapper/app-wrapper/div/section/div/aside[2]/div/deal-page-wrapper/div/new-deal-page/div/div/section/div/aside[2]/div/div/deal-page-tabs/div/ul/li[2]').click()
#     time.sleep(2)

#     # Nova proposta
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/section/div/aside[2]/div/deal-page-wrapper/div/new-deal-page/div/div/section/div/aside[2]/div/deal-page-main/div/div/deal-page-entity-table/div/div/div[1]/div/aside[2]').click()
#     time.sleep(2)

#     # Toggle button atualizar dados
#     toggle_button = ''
#     while toggle_button == '':
#         try:
#             print("Carregando")
#             toggle_button = nav.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/ng-transclude/div[1]/ng-transclude/div[2]/section/forms/form/span[2]/div/div/div/new-field/span/div/div/aside/div").click()
#         except:
#             pass
        
#     # Adicionar produto
#     nav.find_element(By.XPATH, '//*[@id="proposalProducts_quote_sections_0_0"]/div/div[1]/a').click()
#     time.sleep(1)

#     # Adicionar código do produto
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/product-select/form/div/div[1]/input').click()
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/product-select/form/div/div[1]/input').send_keys('CBH5 FO SS T M21')
#     time.sleep(5)

#     # Clique no item 
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/product-select/form/div/div[2]/div/section/table/tbody/tr[1]').click()
#     time.sleep(1.5)

#     # Quantidade
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[1]/div/div/div/new-field/span/input').click()
#     time.sleep(1.5)

#     # Inputar quantidade
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[1]/div/div/div/new-field/span/input').send_keys(Keys.CONTROL + 'A')
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[1]/div/div/div/new-field/span/input').send_keys(Keys.DELETE)
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[1]/div/div/div/new-field/span/input').send_keys('2')
#     time.sleep(1.5)

#     # Escolhendo cor
#     # Lista de cores
#     # Amarelo
#     # Azul
#     # Laranja
#     # Vermelho
#     # Verde
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/product-slide/div/div[1]/div/div[2]/section/form/div/forms/form/span[2]/div/div/div/new-field/span/select-fk/div/div/span/a/div/i').click()
#     time.sleep(1.5)
#     nav.find_element(By.XPATH, '/html/div/div/div/div/ul/li[1]').click()
#     time.sleep(1.5)

#     # Valor praticado
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[4]/div/div/div/new-field/span/input').click()
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[4]/div/div/div/new-field/span/input').send_keys(Keys.CONTROL + 'A')
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[4]/div/div/div/new-field/span/input').send_keys(Keys.DELETE)
#     nav.find_element(By.XPATH, '//*[@id="size-slide-5"]/div/div[2]/section/form/div/forms/form/span[4]/div/div/div/new-field/span/input').send_keys('31.057,00')
#     time.sleep(1.5)

#     # Clicar em Inserir Produto
#     button_inserir = ''
#     while button_inserir == '':
#         try:
#             print('carregando')
#             button_inserir = nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/product-slide/div/div[1]/div/div[3]/div/aside[2]/a[2]').click()
#         except:
#             pass

#     time.sleep(1)

#     # Clicar em condições de pagamento
#     condicao_pagamento = ''
#     while condicao_pagamento == '':
#         try:
#             print('carregando')
#             condicao_pagamento = nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/ng-transclude/div[1]/ng-transclude/div[2]/section/forms/form/span[7]/div/div/div/new-field/span/select-fk/div/div/input[2]').click()
#         except:
#             pass

#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/ng-transclude/div[1]/ng-transclude/div[2]/section/forms/form/span[7]/div/div/div/new-field/span/select-fk/div/div/input[2]').click()
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/ng-transclude/div[1]/ng-transclude/div[2]/section/forms/form/span[7]/div/div/div/new-field/span/select-fk/div/div/input[2]').send_keys('À prazo - 3x')
#     time.sleep(2)
#     nav.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/main-wrapper/app-wrapper/div/new-quote-outside-modal/div/div/ng-transclude/div[1]/ng-transclude/div[2]/section/forms/form/span[7]/div/div/div/new-field/span/select-fk/div/div/input[2]').send_keys(Keys.ENTER)
#     time.sleep(1.5)
#     # À prazo 5x 
#     # mudar a posição na lista[6]