
# Auto Response Chatbot

This Python script automates the process of generating and sending responses based on chat history. It interacts with a chat application, selects a specific chat, retrieves its content, and uses OpenAI's GPT-4 model to generate a suitable response. The generated response is then sent back to the chat automatically.

## Prerequisites

Make sure you have the following Python libraries installed:

- `pyautogui`: For automating GUI actions (clicking, moving the cursor, dragging, etc.).
- `pyperclip`: For copying and pasting text from the clipboard.
- `openai`: For interacting with the OpenAI API.

You can install the required libraries by running the following command:

```bash
pip install -r requitements.txt
```

## Dependencies

| Dependency         | Version    |
|--------------------|------------|
| annotated-types     | 0.7.0      |
| anyio              | 4.7.0      |
| certifi            | 2024.12.14 |
| colorama           | 0.4.6      |
| distro             | 1.9.0      |
| h11                | 0.14.0     |
| httpcore           | 1.0.7      |
| httpx              | 0.28.1     |
| idna               | 3.10       |
| jiter              | 0.8.2      |
| MouseInfo          | 0.1.3      |
| openai             | 1.58.1     |
| PyAutoGUI          | 0.9.54     |
| pydantic           | 2.10.4     |
| pydantic_core      | 2.27.2     |
| PyGetWindow        | 0.0.9      |
| PyMsgBox           | 1.0.9      |
| pyperclip          | 1.9.0      |
| PyRect             | 0.2.0      |
| PyScreeze          | 1.0.1      |
| pytweening         | 1.2.0      |
| sniffio            | 1.3.1      |
| tqdm               | 4.67.1     |
| typing_extensions  | 4.12.2     |

## Setup

1. **API Key**: You need to replace the placeholder `<your openAI api key>` in the script with your actual OpenAI API key.
   
   You can get your OpenAI API key from [OpenAI's API documentation](https://beta.openai.com/docs/).

2. **Coordinates Adjustment**: The script relies on specific screen coordinates for interacting with the application. These coordinates (e.g., `pyautogui.click(409, 766)`) may need to be adjusted based on the screen resolution and the position of the chat window.

## Script Overview

The script performs the following tasks:

1. **Clicking and Selecting**: The script clicks on a predefined position to focus on the chat window and selects the text from the conversation.
2. **Text Extraction**: It copies the selected text from the chat using the clipboard (`ctrl + c`).
3. **Response Generation**: The copied text is sent to OpenAI's GPT-4 model, which processes it and generates a response. The model is instructed to consider Marathi words and generate appropriate responses for a user named Yashodhar Chavan.
4. **Sending Response**: The generated response is typed and sent back into the chat window using `pyautogui`.

## Example Usage

Simply run the script:

```bash
python main.py
```

This will initiate the process of selecting the chat, retrieving the message, generating a response, and sending it.

## Important Notes

- **Screen Coordinates**: The `pyautogui` actions (such as clicking, moving, and dragging) rely on screen coordinates. These may differ based on your screen resolution, the chat application window's position, or UI changes. You may need to adjust the coordinates accordingly.
- **API Key**: Make sure to securely handle your OpenAI API key and avoid hardcoding it in production applications. You may want to use environment variables or a configuration file for better security.
- **Dependencies**: Ensure you have installed the necessary dependencies (`pyautogui`, `pyperclip`, `openai`).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By Yashodhar Chavan
