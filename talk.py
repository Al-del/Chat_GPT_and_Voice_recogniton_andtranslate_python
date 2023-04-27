import pyttsx3
def talk_what_we_need(what_u_want_to_say):
	engine=pyttsx3.init()
	engine.setProperty('rate','6')
	voices=engine.getProperty('voices')
	engine.say(what_u_want_to_say)
	engine.runAndWait()
