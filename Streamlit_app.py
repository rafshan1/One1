import streamlit as st
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

r=sr.Recognizer()
def main():
    st.image('assistant.gif')
    st.title("One")
    
    
    

    # Function to listen for voice commands
    def listen():
        with sr.Microphone() as source:
            st.write("Listening....")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            st.write("Recognizing...")
            command = r.recognize_google(audio).lower()
            st.write("You said:", command)
            return command
        except sr.UnknownValueError:
            st.write("Sorry, I can't understand this command")
            return ""
        except sr.RequestError:
            st.write("Unable to access your command")
            return ""

    # Function to speak text
    def speak(text):
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[0].id)

        engine.say(text)
        engine.runAndWait()

    # Initial greeting
    st.write("Hi, I am your virtual assistant, how can I help you")
    speak("Hi, I am your virtual assistant, how can I help you")
    # Sidebar with command options
    st.sidebar.title("Commands")
    command = st.sidebar.selectbox("Select Command", ["Time", "Open YouTube", "Open Facebook", "Play", "Search", "Exit"])
    
    # Processing commands:streamlit run One.py
    if command == "Time":
        time = datetime.datetime.now().strftime("%I:%M %p")
        st.image("clock1.gif")
        st.write(f"Now time is {time}")
        speak(f"Now time is {time}")
        
    elif command == "Open YouTube":
        webbrowser.open("https://www.youtube.com/")
    elif command == "Open Facebook":
        webbrowser.open("https://www.facebook.com/")
    elif command == "Play":
        st.video('f2.mp4')
        #webbrowser.open("https://www.youtube.com/shorts/CxjdJ3Lf_o4")
    elif command == "Search":
        topic = st.image("wiki.gif"),st.text_input("Enter topic to search on Wikipedia:")
        if st.button("Search"):
            st.image('search.gif')
            try:
                result = wikipedia.summary(topic, sentences=10)
                st.write(result)
                #speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                st.write(f"Multiple matches found for '{topic}'. Please be more specific.")
                speak(f"Multiple matches found for '{topic}'. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                st.write(f"No Wikipedia page found for '{topic}'.")
                speak(f"No Wikipedia page found for '{topic}'.")
    elif command == "Exit":
        speak("May Allah bless you")
    
        # Embed the button with custom GIF animation using HTML and Markdown
   


if __name__ == "__main__":
    main()
