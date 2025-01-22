import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_seleccionar_opcion_free_range_testers(driver):
    # Abrir la página
    driver.get('https://jxcehanp1uulmfid.vercel.app/?utm_source=podia&utm_medium=broadcast&utm_campaign=2279334')

    # Buscar todos los elementos dropdown
    dropdowns = driver.find_elements(By.CSS_SELECTOR, 'button[role="combobox"]')
    print(f'Total de dropdowns en la página: {len(dropdowns)}')

    # Iterar sobre los dropdowns para encontrar el correcto
    opcion_encontrada = False
    for i, dropdown in enumerate(dropdowns, start=1):
        #icono_dropdown = driver.find_element(By.XPATH, f"/html/body/div/div/button[{i}]/svg")
        icono_dropdown = dropdown.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-chevron-down h-4 w-4 opacity-50"]')
        # Hacer clic en el ícono para desplegar el dropdown
        icono_dropdown.click()

        # Esperar a que las opciones se desplieguen
        aria_controls = dropdown.get_attribute('aria-controls')
        print(f'aria-controls: {aria_controls}')
        if aria_controls:
            # Obtener todas las opciones del dropdown
            opciones_dropdown = driver.find_elements(By.CSS_SELECTOR, f'#{aria_controls.replace(":", "\\:")} [role="option"]')
            print(f'Total de opciones en el dropdown número {i}: {len(opciones_dropdown)}')

            # Iterar sobre las opciones del dropdown
            for j, opcion_dropdown in enumerate(opciones_dropdown, start=1):
                texto_opcion_dropdown = opcion_dropdown.text
                print(f'Opción {j}: {texto_opcion_dropdown}')
                if texto_opcion_dropdown == 'FreeRangeTesters':
                    print(f'Opción "FreeRangeTesters" encontrada en el dropdown número {i}')
                    opcion_dropdown.click()  # Seleccionar la opción
                    opcion_encontrada = True

                    # Verificar el popup emergente
                    popup = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="radix-:R3jsq:"]'))
                    )
                    assert '¡Lo lograste!' in popup.text
                    assert 'FreeRangeTesters' in popup.text

                    # Esperar 2 segundos antes de cerrar el popup
                    time.sleep(2)

                    # Hacer click en el botón 'Close' del popup emergente
                    btn_cerrar = driver.find_element(By.XPATH, '//*[@id="radix-:R3jsq:"]/div[2]/button')
                    btn_cerrar.click()
                    break


            # Si se encontró la opción Free Range Testers, salir del bucle principal
            if opcion_encontrada:
                break
            else:
                print(f'No se encontró el atributo aria-controls para el dropdown número {i}')
                #icono_dropdown.click()
                actions = ActionChains(driver)
                actions.move_to_element(icono_dropdown).click().perform()
                continue


    # Manejar el error si no se encontró la opción
    if not opcion_encontrada:
        raise Exception('No se encontró la opción "Free Range Testers" en ningún dropdown.')