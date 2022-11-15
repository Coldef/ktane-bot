# TODO: remove this file

import speech_recognition as sr
import gtts
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    said = r.recognize_google(audio, language="fi")
    print("Google Speech Recognition thinks you said " + said)

    mp3_fp = BytesIO()  # "".encode  #  BytesIO()
    tts = gtts.gTTS(said, lang="fi")
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    play(AudioSegment.from_file(BytesIO(mp3_fp.read()), format="mp3"))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
