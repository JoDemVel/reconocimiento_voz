import numpy as np

from tensorflow.keras import models

from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

comandos = set()

commands = ['abajo', 'adjetivo', 'arriba', 'avanzar', 'calle', 'cervantes', 'cinco',
 'cuadra', 'cuatro', 'deberes', 'dele', 'derecha', 'dos', 'dudas', 'eñe',
 'errores', 'español', 'estar', 'gramatica', 'hablo', 'hechos', 'indicativo',
 'inolvidable', 'instituto', 'izquierda', 'kevin', 'plaza', 'profe', 'seis',
 'ser', 'siele', 'sustantivo', 'tres', 'uno', 'verbos', 'vocabulario']

loaded_model = models.load_model("saved_model")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    #print("Predicted label:", command)
    return command

if __name__ == "__main__":
    while True:
        command = predict_mic()
        if command not in comandos:
            comandos.add(command)
            print("Predicted label:", command)
        if command == "gracias":
            terminate()
            break