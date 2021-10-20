import qrcode

img = qrcode.make('https://linktr.ee/vaibhav024')
img.save('portfo.jpg')

img = qrcode.make('This project was for fun')
img.save('info.jpg')
