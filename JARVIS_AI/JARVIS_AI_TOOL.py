# install the packages
# speechrecognation
# wikipedia
# openai
import datetime
import os
from secretkey import apikey
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
# import random


chatstr=""
def chat(query):
    #write a program to chat with the bot
    global chatstr
    # print(chatstr)
    openai.api_key =apikey
    chatstr += f"Suraj:\n {text}\njarvis:"
    print(chatstr)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo: wrap this inside ao a try catch
    print(response["choices"][0]["text"])
    speaker.Speak(response["choices"][0]["text"])
    chatstr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")



def ai(prompt):
    openai.api_key = apikey
    text1 = f"Open ai response for prompt \n {prompt} \n *******************************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo: wrap this inside ao a try catch
    print(response["choices"][0]["text"])
    text1 += response["choices"][0]["text"]
    if not os.path.exists("openai"):
        os.mkdir("openai")

    # with open(f"formate- {text}")
    # with open(f"openai/formate- {random.randint(1, 10)}", "w") as f:  #this code id to save the file in just number formate

    with open(f"openai/{' '.join(text.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text1)got


# speaker = win32com.client.Dispatch("SAPI.SpVoice")


# while True:
#     print("hello i am jarvis how can i help you.")
#     s = input("Enter what you want to speak: ")
#     speaker.speak(s)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(query)
            return query
        except Exception as e:
            return "SOME ERROR IS COMEING WILL SOLVE SHORTLY"


if __name__ == '__main__':
    # print('Pycharm')
    speaker.speak("Hello i am jarvis A I")
    while True:
        print("listening....")
        text = takeCommand()
        sites = text

        # sites = [["YouTube","https://www.youtube.com/"],["Google","https://www.google.com/"],["Wikipedia","https://www.wikipedia.com/"]]
        for site in sites:
            if f'search {site}'.lower() in text.lower():
                speaker.speak("Searching the result sir..")
                webbrowser.open(sites)

            # play music command
            # if f'Play {site}'.lower() in text.lower():
            #     speaker.speak(sites + "sir..")
            #     web_browser.open(sites)

        if 'play music'.lower() in text.lower():
            mpath = "https://www.youtube.com/watch?v=nACojFS-RI8"
            speaker.speak("Playing Music, sir")
            webbrowser.open(mpath)

        # open any file
        if "open file manager".lower() in text.lower():
            file_path = (r'C:\Users\Sushi\Downloads\hey')
            speaker.speak("Opening file, sir")
            os.startfile(file_path)

        # Time
        if "what is the time".lower() in text.lower():
            ctime = datetime.datetime.now().strftime("%H:%M:%S")
            print(ctime)
            speaker.speak(f"Time is {ctime}")
            # print(ctime)

        if "what is the date".lower() in text.lower():
            from datetime import date

            date = date.today().strftime("%B %d, %Y")
            print(date)
            speaker.speak(f"Date is {date}")

        if "open browser".lower() in text.lower():
            browser = ("C:\Program Files\Google\Chrome\Application\chrome.exe")
            os.startfile(browser)
            speaker.speak(f"opening browser")

        if "using artificial intelligence".lower() in text.lower():
            ai(prompt=text)

        else:
            chat(text)
