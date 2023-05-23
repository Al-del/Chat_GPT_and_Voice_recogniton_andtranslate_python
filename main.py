import speech_recognition as sr
import re
class voice_recognition:
    r = sr.Recognizer()
    def _record(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.r.listen(source)
        return audio
    def understand_the_text(self):
        audio_ = self.record()
        your_words_is = self.r.recognize_google(audio_, language="ro")
        res = re.findall(r'\w+', your_words_is)
        if res[0]=="dreapta":
            print("Hello_there")
get_the_text_recog=voice_recognition()
get_the_text_recog.understand_the_text()