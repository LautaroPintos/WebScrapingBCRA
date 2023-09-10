# Cargamos las librerias para procesar la información
import pandas as pd
import time
from datetime import datetime, timedelta

# Cargamos las librerías para realizar la conexión con Google Chrome via Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Seteamos las opciones de Chrome que queremos aplicar
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# Chequeamos la versión de selenium por las dudas
print(selenium.__version__)

# utilizamos esta dirección para usar selenium driver: https://chromedriver.chromium.org/downloads
# Para saber que versión de Chrome tenemos actualmente tenemos que ir nuestro navegador de google chrome, tocar
# los tres puntos y hacer click en ayuda ("Información de google chrome"). Otra forma de realizar lo mismo es:
# Chequeamos la versión de chrome que tenemos en nuestro sistema operativo. El Comando Wmic nos sirve para
# consultar la infraestructura de administración de Windows. Cuando viene seguido de datafile es que vamos a
# estar consultando sobre archivos del sistema.
# !wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version

#Diccionario con nombres de la variables y links donde encontrarlas
variables = {'CER': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=3540&detalle=CER%A0(Base%202.2.2002=1)', 
            'BADLAR': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=1222&detalle=BADLAR%20en%20pesos%20de%20bancos%20privados%20(en%20%%20n.a.)',
            'TCA3500': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=272&detalle=Tipo%20de%20Cambio%20Mayorista%20($%20por%20US$)%20Comunicaci%F3n%20A%203500%A0-%20Referencia',
            'PaseP': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=7921&detalle=Tasas%20de%20inter%E9s%20de%20las%20operaciones%20de%20pase%20pasivas%20para%20el%20BCRA,%20a%201%20d%EDa%20de%20plazo%20(en%20%%20n.a.)',
            'TPM': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=7935&detalle=Tasa%20de%20Pol%EDtica%20Monetaria%20(en%20%%20n.a.)',
            'PFmin': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=7938&detalle=Tasa%20m%EDnima%20para%20plazos%20fijos%20de%20personas%20humanas%20hasta%20$30%20millones%20(en%20%%20n.a.)',
            'TM20': 'https://www.bcra.gob.ar/PublicacionesEstadisticas/Principales_variables_datos.asp?serie=7922&detalle=TM20%20en%20pesos%20de%20bancos%20privados%A0(en%20%%20n.a.)'}


# Creamos la función para extraer los datos
def extraer_data(fecha_inicio, fecha_fin, nombre_variable):
    '''
    Función que entra a la url asignada a la variable, selecciona fecha desde y hasta, extrae la data y devuelve un dataframe con columnas de fecha y valores
    '''
    
    #Excepción en caso de que no esté definida la variable en el diccionario
    if nombre_variable not in variables:
        print("El nombre de la variable no se encuentra en el diccionario.")
        #return None
    
    #Traemos la URL
    url = variables[nombre_variable]

    service = Service()

    #Utilizamos el driver para abrir chrome
    #driver = webdriver.Chrome(service=service, options=chrome_options)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    
    #Seleccionamos en la página las fechas que definimos 
    desde = driver.find_element("xpath", "//input[@name='fecha_desde']")
    fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y").strftime("%m/%d/%Y")
    desde.send_keys(fecha_inicio)

    hasta = driver.find_element("xpath", "//input[@name='fecha_hasta']")
    fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y").strftime("%m/%d/%Y")
    hasta.send_keys(fecha_fin)
    
    #Seleccionamos el botón que devuelve la tabla
    buscar = driver.find_element("xpath", "//button[@class='btn btn-primary btn-sm']")
    buscar.click()
    
    #Damos unos segundos para que cargue la página en caso de que sean muchos datos
    time.sleep(5)

    #Traemos los datos de esa tabla
    data = driver.find_elements(By.TAG_NAME, 'tr')
    lista = []
    for x in data:
        lista.append(x.text)
        
    #Cerramos el driver
    driver.quit()
    
    #Armo el dataframe
    nombresCol = lista[0].split()
    aux = [elem.split() for elem in lista[1:]]
    df_variable = pd.DataFrame(aux, columns=nombresCol)
    
    #Devuelvo el dataframe
    return df_variable