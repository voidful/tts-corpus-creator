import random
from collections import defaultdict


class GoogleCloud:

    def __init__(self):
        from google.cloud import texttospeech
        self.texttospeech = texttospeech
        self.client = texttospeech.TextToSpeechClient()
        self.speaker_profile = self.build_voices_profile()

    def build_voices_profile(self):
        """Lists the available voices."""
        voices = self.client.list_voices()
        profile_dict = defaultdict(list)
        for voice in voices.voices:
            ssml_gender = self.texttospeech.SsmlVoiceGender(voice.ssml_gender)
            for language_code in voice.language_codes:
                profile_dict[language_code].append({
                    'speaker': voice.name,
                    'gender': ssml_gender.name,
                    'sr': voice.natural_sample_rate_hertz
                })
        return profile_dict

    def __call__(self, text, outfile, lang='en-US'):
        input_text = self.texttospeech.SynthesisInput(text=text)
        voice = self.texttospeech.VoiceSelectionParams(
            language_code=lang,
            name=random.choice(self.speaker_profile[lang])['speaker']
        )

        audio_config = self.texttospeech.AudioConfig(
            speaking_rate=random.uniform(0.8, 1.2),
            pitch=random.uniform(-1.7, 1.7),
            audio_encoding=self.texttospeech.AudioEncoding.MP3
        )

        response = self.client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        with open(f'{outfile}.mp3', "wb") as out:
            out.write(response.audio_content)
