import qrcode

url = "http://192.168.1.190:8000/"
img = qrcode.make(url)
img.save("qr_asistencia.png")



