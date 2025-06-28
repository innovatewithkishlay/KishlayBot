import gradio as gr
from chatbot import get_answer

def respond(message, history):
    response = get_answer(message)
    return response

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 KishlayBot - Personal AI Assistant")
    chatbot = gr.ChatInterface(
        respond,
        examples=["Who is Kishlay?", "What projects has he built?", "Where is his resume?"],
        theme="soft"
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
