import random
import re
import subprocess
import sys
from collections import defaultdict


class MAC:

    def __init__(self):
        import pandas as pd
        self.pd = pd
        self.speaker_profile = self.build_voices_profile()

    def build_voices_profile(self):
        profile_dict = defaultdict(list)
        output_bytes = subprocess.check_output(["say", "-v", "?"]).decode(sys.stdout.encoding)
        lang_list = [[p.strip() for p in re.split('  +', s)] for s in str(output_bytes).split("\n") if
                     len(s.strip()) > 0]
        for lang in lang_list:
            profile_dict[lang[1]].append(lang[0])
        return profile_dict

    def transform_into_mp3(self, fname):
        subprocess.check_output(
            ["ffmpeg", "-y", "-i", f"{fname}.aiff", "-f", "mp3", "-acodec", "libmp3lame", "-ab", "192000", "-ar",
             "44100", f"{fname}.mp3"])
        subprocess.call(['rm', f"{fname}.aiff"])

    # ref: https://gist.github.com/jeffeuxMartin/b96382cbee4a0e1eaa38b28925dc0b16
    def __call__(self, text, outfile, lang='en_US'):
        lang = lang.replace("-", "_")
        subprocess.check_output(
            ["say", '-v', random.choice(self.speaker_profile[lang]), f'{text}', '-o', f'{outfile}'])
        self.transform_into_mp3(outfile)
