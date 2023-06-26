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
    def __init__(self):
        self.frames = []
        self.is_recording = False
        self.audio_format = pyaudio.paInt16 # 16 bits por muestra
        self.channels = 1 # mono
        self.sample_rate = 44100 # Hz
        self.chunk = 1024 # muestras por buffer

    def __recognize_audio(self, save_path):
        audio_model = whisper.load_model('base')
        transcript = audio_model.transcribe(save_path, language='spanish', fp16 = False)
        return transcript['text']

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

    def stop(self):
        self.is_recording = False
        print("Grabación finalizada")

    def save(self):
        audio = pyaudio.PyAudio()
        wf = wave.open(save_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(audio.get_sample_size(self.audio_format))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        return self.__recognize_audio(save_path).lower()