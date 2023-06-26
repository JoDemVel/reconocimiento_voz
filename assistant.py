from modules.listener_whisper import Listener
from modules.processor import Processor
import time
import threading

def main():
    processor = Processor()
    listener = Listener()
    threading.Thread(target=listener.start).start()
    time.sleep(5)
    print("Detener")
    res = listener.stop()
    res = listener.save()
    print(res)
    print(processor.process(res))
    
    """
    processor = Processor()
    print(processor.process('kevin avanzar 2 cuadras por calle deberes hechos'))
    print(processor.process('kevin avanzar 3 cuadras por calle de los errores'))
    print(processor.process('kevin ir a la calle del vocabulario esquina calle de las dudas'))
    print(processor.process('kevin ir a panaderia por calle del vocabulario'))
    print(processor.process('kevin ir a la calle de la gramatica esquina calle del me gusta'))
    """
if __name__ == '__main__':
    main()
