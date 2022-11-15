from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import gtts
import speech_recognition as sr
from constants import CANCEL_PHRASE

LANGUAGE = "fi"

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Calibrating")
    r.adjust_for_ambient_noise(source)
    print("Calibrating done")


def ask_player(content):
    """
    Asks something from the player, returns with the player's answer
    :param content: Question string
    :return: Player's given answer. If the player decides to cancel the question with CANCEL_PHRASE, returns false.
    """
    print("Asked player: " + content)
    mp3_fp = BytesIO()
    tts = gtts.gTTS(content, lang=LANGUAGE)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    play(AudioSegment.from_file(BytesIO(mp3_fp.read()), format="mp3"))

    with sr.Microphone() as source:
        print("Listening for answer")
        audio = r.listen(source)

    try:
        said = r.recognize_google(audio, language="fi").lower()
    except sr.UnknownValueError:
        return ""
    print("Got answer: " + said)
    if said == CANCEL_PHRASE:
        return CANCEL_PHRASE
    return said.lower()


def tell_player(content):
    """
    Tells something to the player
    :param content: String to be said
    :return:
    """
    if content == "":
        return
    print("Told player: " + content)
    mp3_fp = BytesIO()  # "".encode  #  BytesIO()
    tts = gtts.gTTS(content, lang=LANGUAGE)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    play(AudioSegment.from_file(BytesIO(mp3_fp.read()), format="mp3"))
    return


def listen(timeout=None):
    """
    Just listening to the player
    :param timeout: Amount of seconds listened
    :return: What was said into the microphone
    """

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=timeout)
    except sr.WaitTimeoutError as e:
        print("Listening timed out")

    try:
        said = r.recognize_google(audio, language="fi").lower()
    except sr.UnknownValueError:
        return ""
    print("Got answer: " + said)
    return said.lower()

