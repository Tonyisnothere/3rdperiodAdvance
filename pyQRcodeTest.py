import pyqrcode
import png

def bcps():
    url = pyqrcode.create('https://whttp://www.bcps.org/')
    url.svg('uca-url.svg', scale=8)
    url.eps('uca-url.eps', scale=2)
    url.png('bcps.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    print(url.terminal(quiet_zone=1))
bcps()

def lego():
    url = pyqrcode.create('https://www.lego.com/en-us')
    url.svg('uca-url.svg', scale=8)
    url.eps('uca-url.eps', scale=2)
    url.png('lego.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    print(url.terminal(quiet_zone=1))
lego()