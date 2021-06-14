
import speech_recognition as sr


def get_wakeUpWord():

    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=1)
        print("Listen to wake up world ....")
        text = ""
        try:
            audio = r.listen(source, phrase_time_limit=5)
            print("********** Stop Record **********")
            # text = r.recognize_google(audio, language='fa-IR')
            text = r.recognize_google(audio, language='en-US')

        except Exception as e:
            print("Exception: ")
    return text


def get_command():

    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening to command ....")
        text = ""
        try:
            audio = r.listen(source, phrase_time_limit=5)
            print("********** Stop Record **********")
            # text = r.recognize_google(audio, language='fa-IR')
            text = r.recognize_google(audio, language='en-US')

        except Exception as e:
            print("Exception: ")
    return text


while True:
    word = get_wakeUpWord()
    print(word)

    if word == "hey":
        command = get_command()
        print(command)

        if command == "hello world":
            print("You say Hello World !")
            # Do somthing  ....
