import qrcode

url = "https://wedex59.pythonanywhere.com/"
img = qrcode.make(url)
img.save("qr_asistencia.png")

