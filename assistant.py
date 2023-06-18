from modules.listener_whisper import Listener
from modules.processor import Processor
import time
import threading

def main():
    #listener = Listener()

    listener = Listener()
    threading.Thread(target=listener.start).start()
    time.sleep(2)
    listener.stop()
    path = listener.save()
    print(path)


    """    
    processor = Processor()
    response = listener.listen()
    comandos = processor.process(response)
    print(response)
    print(comandos)
    """
    
if __name__ == '__main__':
    main()
