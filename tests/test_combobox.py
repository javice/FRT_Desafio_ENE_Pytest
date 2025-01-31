# tests/test_combobox.py
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

def test_seleccionar_opcion_free_range_testers(driver):
    main_page = MainPage(driver)
    main_page.open()

    dropdowns = main_page.get_dropdowns()
    print(f'Total de dropdowns en la página: {len(dropdowns)}')

    opcion_encontrada = False
    for i, dropdown in enumerate(dropdowns, start=1):
        icono_dropdown = dropdown.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-chevron-down h-4 w-4 opacity-50"]')
        icono_dropdown.click()

        aria_controls = dropdown.get_attribute('aria-controls')
        print(f'aria-controls: {aria_controls}')
        if aria_controls:
            opciones_dropdown = main_page.get_dropdown_options(aria_controls)
            print(f'Total de opciones en el dropdown número {i}: {len(opciones_dropdown)}')

            for j, opcion_dropdown in enumerate(opciones_dropdown, start=1):
                texto_opcion_dropdown = opcion_dropdown.text
                print(f'Opción {j}: {texto_opcion_dropdown}')
                if texto_opcion_dropdown == 'FreeRangeTesters':
                    print(f'Opción "FreeRangeTesters" encontrada en el dropdown número {i}')
                    opcion_dropdown.click()
                    opcion_encontrada = True

                    popup = main_page.get_popup()
                    assert '¡Lo lograste!' in popup.text
                    assert 'FreeRangeTesters' in popup.text

                    time.sleep(2)
                    main_page.close_popup()
                    break

            if opcion_encontrada:
                break
            else:
                print(f'No se encontró el atributo aria-controls para el dropdown número {i}')
                actions = ActionChains(driver)
                actions.move_to_element(icono_dropdown).click().perform()
                continue

    if not opcion_encontrada:
        raise Exception('No se encontró la opción "Free Range Testers" en ningún dropdown.')