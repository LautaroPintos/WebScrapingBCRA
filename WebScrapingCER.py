import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Definir el rango de fechas a descargar
fecha_inicio = '01/03/2023'
fecha_fin = '13/03/2023'

# utilizamos esta dirección para usar selenium driver: https://chromedriver.chromium.org/downloads
url = 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=3540&detalle=CER%A0(Base%202.2.2002=1)'

# utilizamos el driver para abrir chrome
driver = webdriver.Chrome()
driver.get(url)

# Ahora buscamos la fecha desde
lala = driver.find_element("xpath", "//input[@name='fecha_desde']")
lala.send_keys(fecha_inicio)

# Ahora buscamos la fecha desde
pepe = driver.find_element("xpath", "//input[@name='fecha_hasta']")
pepe.send_keys(fecha_fin)

# Ahora buscamos la fecha desde
buscar = driver.find_element("xpath", "//button[@class='btn btn-primary btn-sm']")
buscar.click()

# Ahora accedemos a la tabla resultante fila por fila para luego guardarlo en un DataFrame
Datin = driver.find_elements(By.TAG_NAME, 'tr')

# Guardamos la información en una lista
listaCER = []
for x in Datin:
    listaCER.append(x.text)

# Acá lo que hacemos es cerrar el driver
driver.quit()

# Separamos los nombres de las columnas
nombresCol = listaCER[0].split()

# Separamos las filas por espacio
aux = [elem.split() for elem in listaCER[1:]]

# Creamos el DataFrame Final
DatosCER = pd.DataFrame(aux, columns=nombresCol)
