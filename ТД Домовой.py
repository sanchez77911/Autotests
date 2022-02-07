from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

# Переходим на сайт ТД Домовой
driver.get("https://tddomovoy.ru/")

# Ищем интересующие нас обои "Обои Sonet"
sleep(1)
driver.find_element_by_xpath("//*[@id='title-search-input']").send_keys("Обои Sonet")

# Вводим интером набранный текст
sleep(1)
driver.find_element_by_xpath("//*[@id='title-search-input']").send_keys(Keys.ENTER)

# В найденном списке выбираем вторые обои и кликаем на них
sleep(1)
driver.find_element_by_id("rslides2_s0").click()

# Вводим количество выбранных обоев (а если точнее, то задаем количество кликов на знак "+")
sleep(1)
basket_button = driver.find_element_by_id("bx_117848907_128136_quant_up")
counter = 0
while True:
    basket_button.click()
    if counter == 98:
        break
    counter += 1

# Жмем на кнопку "добавить в корзину"
sleep(3)
driver.find_element_by_id("bx_117848907_128136_add_basket_link").click()

# Переходим в корзину
sleep(1)
driver.find_element_by_css_selector("[href='/personal/cart/']").click()

# Жмем кнопку "оформить заказ"
sleep(1)
driver.find_element_by_xpath("//input[@value='Оформить заказ']").click()

# Жмем кнопку "продолжить без регистрации"
sleep(1)
driver.find_element_by_css_selector("[class='btn btn-light-grey']").click()

# Вводим имя
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Введите имя']").send_keys("Иван")

# Вводим фамилию
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Введите фамилию']").send_keys("Иванов")

# Вводим отчество
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Введите отчество']").send_keys("Иванович")

# Вводим номер телефона
sleep(1)
driver.find_element_by_xpath("//*[@id='tel-mask-on']").send_keys("9313365525")

# Вводим электронную почту
sleep(1)
driver.find_element_by_xpath("//input[@placeholder='example@mail.ru']").send_keys("ivanoviiqwerty@bk.ru")

# Жмем кнопку "далее"
sleep(1)
driver.find_element_by_xpath("//*[@id='in_name']/div[2]/button").click()

# Функционал проверен - работает исправно, вернемся обратно в корзину
sleep(1)
driver.find_element_by_css_selector("[rel=nofollow]").click()

# Удаляем из корзины весь добавленный ранее товар, после чего сайт автоматически выкидывает нас на главную страницу
sleep(1)
driver.find_element_by_css_selector("[class=goods_delete]").click()

# А теперь закрываем браузер
sleep(5)
driver.close()
