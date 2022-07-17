import re
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'book.txt'))
g = open(os.path.join(__location__, 'file.mc'), 'w')
file= f.read()
f.close()

list = re.split(' =====================================', re.sub('=====================================', ' ==========================================================================', file))
list.pop(0)

list_sorted = sorted(list, key=lambda x: x[1:50])

for i in range(len(list_sorted)):
    g.write(list_sorted[i])

os.remove('book.txt')