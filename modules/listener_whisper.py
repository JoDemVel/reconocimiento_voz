import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import tempfile
import os

import pyaudio
import wave

temp_file = tempfile.mkdtemp()
save_path = os.path.join(temp_file, "temp.wav")

listener = sr.Recognizer()

class Listener:
    

    def __listen_from_mic(self):
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                data = io.BytesIO(voice.get_wav_data())
                audio_clip = AudioSegment.from_file(data)
                audio_clip.export(save_path, format="wav")
        except Exception as e:
            print(e)
        return save_path

    def __recognize_audio(self, save_path):
        audio_model = whisper.load_model('base')
        transcript = audio_model.transcribe(save_path, language='spanish', fp16 = False)
        return transcript['text']

    def listen_mic(self):
        print('Escuchando...')
        return self.__recognize_audio(self.__listen_from_mic()).lower()

    def listen(self):
        response = self.__recognize_audio(self.__listen_from_mic()).lower()
        while True:
            if 'kevin' in response:
                print('Escuchando')
                response = response.replace('kevin', '')
                while True:
                    response = self.__recognize_audio(self.__listen_from_mic()).lower()
                    if 'gracias' in response:
                        break
                break
            else:
                response = self.__recognize_audio(self.__listen_from_mic()).lower()
        
        return response

    def __init__(self):
        self.frames = []
        self.is_recording = False
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
        self.chunk = 1024

    def start(self):
        self.is_recording = True
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.audio_format,
                            channels=self.channels, 
                            rate=self.sample_rate, 
                            input=True, 
                            frames_per_buffer=self.chunk)
        print("Grabando...")

        while self.is_recording:
            data = stream.read(self.chunk)
            self.frames.append(data)

        stream.stop_stream()
        stream.close
        audio.terminate()
        self.save()
    
    def save(self):
        audio = pyaudio.PyAudio()
        wf = wave.open(save_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        return self.__recognize_audio(save_path)

    def stop(self):
        self.is_recording = False
        print("Grabación finalizada")