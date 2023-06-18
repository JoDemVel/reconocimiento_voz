import numpy as np 
import tensorflow as tf

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)

def get_spectrogram(waveform):
    # Convert the waveform to a spectrogram via a STFT.
    spectrogram = tf.signal.stft(
        waveform, frame_length=255, frame_step=128)
    # Obtain the magnitude of the STFT.
    spectrogram = tf.abs(spectrogram)
    # Add a `channels` dimension, so that the spectrogram can be used
    # as image-like input data with convolution layers (which expect
    # shape (`batch_size`, `height`, `width`, `channels`).
    spectrogram = spectrogram[..., tf.newaxis]
    
    return spectrogram

def preprocess_audiobuffer(waveform):
    waveform = waveform / 32768
    waveform = tf.convert_to_tensor(waveform, dtype=tf.float32)
    spectrogram = get_spectrogram(waveform)
    spectrogram = tf.expand_dims(spectrogram, 0)

    return spectrogram