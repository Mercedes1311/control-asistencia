import qrcode

url = "https://jeboho3393.pythonanywhere.com/"
img = qrcode.make(url)
img.save("qr_asistencia.png")

