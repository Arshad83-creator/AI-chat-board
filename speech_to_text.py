import speech_recognition as sr

def speech_to_text():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something...")
        audio=r.listen(source)
        try:
            
            voice_data= r.recognize_google(audio)
            print("You said:",voice_data)
            return voice_data
    
        except sr.UnknownValueError:   
            print("Error : Could not understand audio")
            return

        except sr.RequestError:   
            print("RequestError")
            return


# speech_to_text()



