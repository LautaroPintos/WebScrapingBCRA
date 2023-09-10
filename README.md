# WebScrapingBCRA

### Código para poder descargar las series temporales de distintas variables publicadas por el BCRA.

Las variables actualmente incluidas y testeadas son:

	- CER
	- BADLAR
	- TC3500 
	- PaseP: Pases Pasivos
	- TPM: Tasa de política monetaria
	- PFmin: Tasa de plazo fijo minorista
	- TM20: TM20

Algunas consideraciones importantes a tener en cuenta es que siempre debemos testear la versión de Selenium
para utilizar una versión posterior a la 4.10. Para chequear la versión de selenium podemos hacer:

import selenium
print(selenium.__version__)

Para chequear la versión de Chrome en nuestro ordenador podemos utilizar (en windows):
!wmic datafile where name="C:\\......\\chrome.exe" get Version

Trabajo hecho en colaboración con @AldanaRuscitti

Citations: Mr Fugu Data Science