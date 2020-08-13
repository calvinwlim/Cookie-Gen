from gen import options
from gen import generator
import pyfiglet


banner = pyfiglet.figlet_format('Cookie-Gen', font = "slant")
print(banner)
generator()