from playwright.sync_api import sync_playwright
import time


ALOHA_BINARY= r"C:\Users\Satosi_Nakomoto\AppData\Local\Aloha Mobile\Aloha\Application\aloha.exe" #тут ваш путь к бинарнику

def test_close_active_tab_smoke():
    with sync_playwright() as p:
        #Запускаем aloha  как chromium браузер
        browser = p.chromium.launch(executable_path=str(ALOHA_BINARY), headless=False)
        context = browser.new_context()

        #Открываем три разных вкладки
        page1 = context.new_page()
        page1.goto("https://vk.com")

        page2 = context.new_page()
        page2.goto("https://youtube.com")

        page3 = context.new_page()
        page3.goto("https://yandex.ru")

        time.sleep(1) #оставляем время прогрузится вкладкам

        #Проверяем кол-во вкладок до закрытия
        pages_before_close = context.pages
        print(f"Вкладок до закрытия:", len(pages_before_close))
        assert len(pages_before_close) == 3

        # закрываем третью и вторую вкладки
        page3.close()
        time.sleep(4) #тут таймслип для визуальной наглядности
        page2.close()

        # Проверяем кол-во вкладок после закрытия
        pages_after_close = context.pages
        print(f"Вкладок после закрытия:", len(pages_after_close))
        assert len(pages_after_close) == 1

        time.sleep(5) # Тут так же для визуальной наглядности, что вкладки закрыты
        
        browser.close()


