# simple Qr code generaton program for given text or link

import qrcode as qr
img = qr.make("https://www.youtube.com/channel/UCZyiQd6rV9L8JgOnahkx7tw")
img.save("testqr.png")
