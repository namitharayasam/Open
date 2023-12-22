import os
import openai
import gradio

my_api_key = "paste your api key here"
openai.api_key = my_api_key

def customGPT(role, user_input):
    messages = [{"role": "system", "content": role}]

    messages.append({"role": "user", "content": user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": chatgpt_reply})

        return chatgpt_reply

    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred, please try again later."

demo = gradio.Interface(
    fn=customGPT,
    inputs=["text", "text"], 
    outputs="text",
    title="Custom GPT"
)

demo.launch(share=True)
