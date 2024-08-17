import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY'] = "api key"

genai.configure(api_key = os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-pro')
print("HELLO THIS IS TERMINAL-AI")
question = ""
print("ASK ME ANYTHING! OR TYPE NEVERMIND TO EXIT")
while True:
    print()
    question = input("YOUR RESPONSE: ")
    if question == "Nevermind" or question == "nevermind" or question == "NEVERMIND":
        print()
        print("BYE!")
        exit()
    response = model.generate_content(question)
    print()
    print(response.text)
