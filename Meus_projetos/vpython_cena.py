from vpython import*

box()
while True:
    a = scene.waitfor("keydown")
    if a.event == "keydown":
        scene.delete()
        cena = canvas(width=900, height=1000,
                      align="left", background=color.cyan)
        sphere()
