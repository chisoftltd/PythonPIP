# Python PIP
import os
import sys
import camelcase

os.system("cls")
c = camelcase.CamelCase()

txt  = "Python PIP"

print(c.hump(txt))
print(os.path.dirname(sys.executable))