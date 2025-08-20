import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    if data is None:
        return "I did not catch that."
    user_data = data.lower()  # convert to lowercase for easy matching
    

    if "what is your name" in user_data:
        ans = "My name is Virtual Assistant"
        text_to_speech.text_to_speech(ans)
        return ans

    elif "hello" in user_data or "hi" in user_data or "hye" in user_data:
        ans = "Hi Sir, how can I help you?"
        text_to_speech.text_to_speech(ans)
        return ans

    elif "good morning" in user_data:
        ans = "Good morning sir"
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "what are you doing" in user_data:
        ans = "I am talk to you"
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "thank you" in user_data:
        ans = "Your's most Welcome"
        text_to_speech.text_to_speech(ans)
        return ans
    
    
    

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data:
        ans = "Ok Sir, shutting down"
        text_to_speech.text_to_speech(ans)
        return ans

    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")  # fixed URL
        ans = "Gaana.com is now ready for you"
        text_to_speech.text_to_speech(ans)
        return ans

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        ans = "YouTube is now ready for you"
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        ans = "Google is now ready for you"
        text_to_speech.text_to_speech(ans)
        return ans
    
    elif "instagram" in user_data:
        webbrowser.open("https://instagram.com/")
        ans = "Instagram Reels are now ready for you"
        text_to_speech.text_to_speech(ans)
        return ans

    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans

    else:
       
        text_to_speech.text_to_speech(data)
        return data
