# tts-corpus-creator
collection of different source of tts api for generating corpus.
feature:
- large scale tts
- support both free and charge source

## Source

### Charge

#### Google Cloud TTS
1. install `pip install google-cloud-texttospeech`
```python
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "xxx.json"

from ttscorpus.source import GoogleCloud

gc = GoogleCloud()
gc("hi,there", 'output')
```

### Free

#### Mac

1. install ffmpeg `brew install ffmpeg`

```python
from ttscorpus.source import MAC

mac = MAC()
mac('hello, there, I am mac', 'output')
```

#### Google TTS
1. install `pip install gtts`
```python
from ttscorpus.source import GoogleTTS

mac = GoogleTTS()
mac('sixty six year old badly. independence of mutual fund boards represents discrete defeat.', 'test')
```

#### Android TTS
1. build android tts server app from: [https://github.com/voidful/android-tts-server](https://github.com/voidful/android-tts-server)
 