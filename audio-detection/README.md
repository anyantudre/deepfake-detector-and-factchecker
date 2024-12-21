# fake-audio-detection

## Data preparation and generation
### Available datasets
Available deep fake audios detection datasets:
- **ASVspoof2015-2017-2019-2021:** [website](https://www.asvspoof.org/database )
- **partial spoof**: [paper](https://arxiv.org/pdf/2204.05177.pdf) [dataset download](https://zenodo.org/record/5766198)
- **wavefake**:  [paper](https://arxiv.org/pdf/2111.02813.pdf)  [dataset download](https://zenodo.org/record/5642694#:~:text=WaveFake%3A%20A%20data%20set%20to%20facilitate%20audio%20DeepFake,finding%20new%20detection%20methods%20to%20prevent%20such%20attempts.) 
- **In-the-Wild:**  [website](https://deepfake-demo.aisec.fraunhofer.de/in_the_wild)  [paper](https://arxiv.org/pdf/2203.16263.pdf)  [dataset download](https://owncloud.fraunhofer.de/index.php/s/JZgXh0JEAF0elxa)
- **APTLY - Fake-or-Real (FoR) Dataset** [website](https://bil.eecs.yorku.ca/datasets/)

### Synthetic AI-generated voices generation
To build a robust dataset for deepfake audio detection, we'll utilize a variety of state-of-the-art, open-source text-to-speech (TTS) models:
- **[Coqui TTS](https://github.com/coqui-ai/TTS)**
- **[Parler-TTS](https://github.com/huggingface/parler-tts)**
- **[MeloTTS](https://github.com/myshell-ai/MeloTTS)**
- **[Piper](https://github.com/rhasspy/piper)**
- **[WhisperSpeech](https://github.com/WhisperSpeech/WhisperSpeech)**
- **[RealtimeTTS](https://github.com/KoljaB/RealtimeTTS)**
- **[Real-Time Voice Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)**
- **[StyleTTS](https://github.com/StyleTTS/StyleTTS)**
- **[OpenVoice](https://github.com/OpenVoiceAI/OpenVoice)**
- **[F5-TTS](https://github.com/SWivid/F5-TTS)**


### Open source datasets for real human voices
To complement the synthetic audio data, we'll incorporate authentic human speech from reputable open-source datasets commonly used in training TTS and ASR models:
- **[LibriSpeech](https://www.openslr.org/12):** corpus of approximately 1,000 hours of read English speech derived from audiobooks.
- **[VCTK Corpus](https://datashare.ed.ac.uk/handle/10283/3443):** contains speech data from multiple speakers with various accents, useful for multi-speaker TTS and ASR training.
- **[Common Voice](https://commonvoice.mozilla.org/en/datasets):** open-source project by Mozilla that offers a large dataset of voices in multiple languages, contributed by volunteers.
- **[Hi-Fi TTS](https://openslr.org/109):** multi-speaker English dataset for training text-to-speech models.


## Pretrained models
- [Transformers based audio models - Hugging Face](https://huggingface.co/docs/transformers/model_doc/xls_r): most of these models are self-supervised, transformer-based models for learning speech representations from raw audio (they perform pretty well on audio classification tasks)
    - **[AudioSpectrogramTransformer](https://github.com/ast-ml/ast)**
    - **[Wav2Vec 2.0](https://github.com/pytorch/fairseq/tree/main/examples/wav2vec):**
    - **WavLM**
    - **HuBERT**
    - **XLS-R (Cross-Lingual Speech Representation)**

- [TensorFlow audio models](https://github.com/tensorflow/models/tree/master/research/audioset)
    - **[VGGish](https://github.com/tensorflow/models/tree/master/research/audioset):**
    - **[YAMNet](https://github.com/tensorflow/models/tree/master/research/audioset/yamnet):**


## External ressources
- [Awesome-fake-audio-detection](https://github.com/john852517791/awesome-fake-audio-detection/blob/main/README.md)
