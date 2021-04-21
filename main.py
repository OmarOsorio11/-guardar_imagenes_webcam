import cv2


def captura_video(camera):
    capt = cv2.VideoCapture(camera)
    return capt


def show_video(captura, num_img, name, inicial, extension):
    count = inicial
    clave = False
    while captura.isOpened():
        ret, imagen = captura.read()
        if ret:
            cv2.imshow('Video', imagen)
            if cv2.waitKey(1) & 0xFF == ord('g'):
                clave = True
            if clave:
                cv2.imwrite(name+str(count)+extension, imagen)
                clave = False
                count += 1
            if count > (num_img+inicial-1):
                break

        else:
            break
    captura.release()
    cv2.destroyAllWindows()


def get_extension():
    ext = str(input('Ingrese la extension de las imagenes (.jpg): '))
    return ext


def get_cantidad_imagenes():
    cant = int(input("Ingrese la cantidad de imagenes a tomar (1): "))
    return cant


def get_name():
    name= str(input("Ingrese el nombre de las imagenes (imagen): "))
    return name


def get_valor_inicial():
    val=int(input("Ingrese el valor inicial de los indices (1): "))
    return val


def print_Instrucciones():
    print("Para guardar una imagen, presione a tecla G")


def main():
    print_Instrucciones()
    extension = get_extension()
    cantidad_imagenes = get_cantidad_imagenes()
    name = get_name()
    val_inicial = get_valor_inicial()
    cap = captura_video(0)
    show_video(cap, cantidad_imagenes, name, val_inicial, extension)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()