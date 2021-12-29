import qrcode

img = qrcode.make('https://www.instagram.com/codewithbiki/')
img.save('qr_code.png')
img.show()



