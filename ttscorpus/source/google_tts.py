class GoogleTTS:

    def __init__(self):
        from gtts import gTTS
        self.gTTS = gTTS

    def __call__(self, text, outfile, lang='en'):
        tts = self.gTTS(text, lang=lang)
        tts.save(f'{outfile}.mp3')
