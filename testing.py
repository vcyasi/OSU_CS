# https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/

import pyqrcode
from pyqrcode import QRCode

# URI name
# site = "www.reddit.com"
uri = "otpauth://totp/YasiCorp:yasiv@google.com?secret=JBSWY3DPEHPK3PXP&issuer=YasiCorp"

# Create a QR code
# url = pyqrcode.create(site)
code = pyqrcode.create(uri)

# Save QR code as svg file
# url.svg("reddit.svg", scale = 8)
code.svg("login.svg", scale = 8)