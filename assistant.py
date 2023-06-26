from modules.listener_whisper import Listener
from modules.processor import Processor
import time
import threading

def main():
    #listener = Listener()
    #print(listener.listen_mic())
    """
    listener = Listener()
    threading.Thread(target=listener.start).start()
    time.sleep(2)
    listener.stop()
    path = listener.save()
    print(path)
    """

    """    
    processor = Processor()
    response = listener.listen()
    comandos = processor.process(response)
    print(response)
    print(comandos)
    """
    
    processor = Processor()
    print(processor.process('kevin avanzar 2 cuadras por calle deberes hechos'))
    print(processor.process('kevin avanzar 3 cuadras por calle de los errores'))
    print(processor.process('kevin ir a la calle del vocabulario esquina calle de las dudas'))
    print(processor.process('kevin ir a panaderia por calle del vocabulario'))
    print(processor.process('kevin ir a la calle de la gramatica esquina calle del me gusta'))
if __name__ == '__main__':
    main()
