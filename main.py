import urllib.parse

import qrcode

msg="Your device has been hacked just now!!!"
encoded=urllib.parse.quote(msg)
url=f"data:text/plain,{encoded}"
qr=qrcode.make(url)
