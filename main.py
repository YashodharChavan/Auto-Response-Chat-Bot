import pyautogui
import time
import pyperclip
import openai

client = openai.OpenAI(
    api_key = "<your openAI api key>"
)

def get_response(prompt):
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are supposed to analyze the chats, the user is Yashodhar Chavan and you need to print what should be the next response of Yashodhar Chavan, the prompt may contain marathi words. You just need to give the response not enclosed in quotes"},
        {
            "role": "user",
            "content": prompt
        }
    ]
    )
    return completion.choices[0].message.content


def main():
    pyautogui.click(409, 766)
    time.sleep(2)    

    pyautogui.moveTo(554, 191)
    time.sleep(1)

    pyautogui.dragTo(1327, 651, duration=0.5, button='left')
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    text = pyperclip.paste()
    print(text)
    response = get_response(text)
    print(response)

    pyautogui.click(638, 695)
    pyautogui.typewrite(response)
    
    pyautogui.press('enter')

if __name__ == "__main__":
    main()