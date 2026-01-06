import urllib.parse

import qrcode

msg=""
encoded=urllib.parse.quote(msg)
url=f"https://sohelshrestha03.github.io/qrcode/index.html?text={encoded}"
qr=qrcode.make(url)
qr.save("browser1.png")
