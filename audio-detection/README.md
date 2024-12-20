# fake-audio-detection

## Data Generation
### Open Source Models for Synthetic AI-Generated Voices
To build a robust dataset for deepfake audio detection, we'll utilize a variety of state-of-the-art, open-source text-to-speech (TTS) models:
- **[Coqui TTS](https://github.com/coqui-ai/TTS):** TTS library offering pretrained models in over 1,100 languages. 
- **[Parler-TTS](https://github.com/huggingface/parler-tts):** lightweight TTS model developed by Hugging Face, capable of generating high-quality, natural-sounding speech.
- **[MeloTTS](https://github.com/myshell-ai/MeloTTS):** high-quality multilingual TTS library supporting many languages.
- **[Piper](https://github.com/rhasspy/piper):** fast, local neural TTS system optimized for devices like the Raspberry Pi 4, suitable for real-time applications.
- **[WhisperSpeech](https://github.com/WhisperSpeech/WhisperSpeech):** open-source TTS system built by inverting OpenAI's Whisper model, aiming to provide a powerful and customizable speech synthesis tool.
- **[RealtimeTTS](https://github.com/KoljaB/RealtimeTTS):** TTS library designed for real-time applications.
- **[Real-Time Voice Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning):** An open-source project that enables cloning a voice in 5 seconds to generate arbitrary speech in real-time. 
- **[StyleTTS](https://github.com/StyleTTS/StyleTTS):** TTS model that leverages style diffusion and adversarial training with large speech language models.
- **[OpenVoice](https://github.com/OpenVoiceAI/OpenVoice):** voice cloning approach that requires only a short audio clip from the reference speaker to replicate their voice and generate speech in multiple languages. 
- **[F5-TTS](https://github.com/SWivid/F5-TTS):** TTS model capable of zero-shot voice cloning with minimal input.


### Open Source Datasets for True Human Voices
To complement the synthetic audio data, we'll incorporate authentic human speech from reputable open-source datasets commonly used in training TTS and Automatic Speech Recognition (ASR) models:
- **[LibriSpeech](https://www.openslr.org/12):** corpus of approximately 1,000 hours of read English speech derived from audiobooks.
- **[VCTK Corpus](https://datashare.ed.ac.uk/handle/10283/3443):** contains speech data from multiple speakers with various accents, useful for multi-speaker TTS and ASR training.
- **[Common Voice](https://commonvoice.mozilla.org/en/datasets):** open-source project by Mozilla that offers a large dataset of voices in multiple languages, contributed by volunteers.
- **[Hi-Fi TTS](https://openslr.org/109):** multi-speaker English dataset for training text-to-speech models.
