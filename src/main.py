from gen import options
from gen import ftlGenerator, eastbayGenerator, champsGenerator, ftaGenerator
import pyfiglet


banner = pyfiglet.figlet_format('Cookie-Gen', font = "slant")
print(banner)
site = input('Select A Site: / Footlocker / Eastbay / Champs / Footaction   ')
if site == 'Footlocker':
    ftlGenerator()
elif site == 'Eastbay':
    eastbayGenerator()
elif site == 'Champs':
    champsGenerator()
elif site == 'Footaction':
    ftaGenerator()
else:
    print('Site Input Invalid')