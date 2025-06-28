import gradio as gr
from chatbot import get_answer

def respond(message, history):
    response = get_answer(message)
    return response

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        neutral_hue="slate",
        font=["Inter", "Segoe UI", "sans-serif"]
    ),
    css="""
    body { background: linear-gradient(120deg, #f8fafc 0%, #e0e7ef 100%); }
    #main-container {
        max-width: 460px;
        margin: 48px auto 0 auto;
        padding: 32px 24px 24px 24px;
        background: rgba(255,255,255,0.98);
        border-radius: 18px;
        box-shadow: 0 8px 32px 0 rgba(60,60,120,0.08);
        border: 1px solid #e2e8f0;
    }
    .gr-chatbot {
        background: #f3f6fa;
        border-radius: 14px;
        box-shadow: 0 2px 8px 0 rgba(60,60,120,0.03);
        border: none;
        font-size: 1.13rem;
    }
    .gr-input input {
        background: #f8fafc;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        font-size: 1.1rem;
        padding: 14px;
    }
    .gr-button {
        border-radius: 12px !important;
        font-weight: 600;
        letter-spacing: 0.02em;
        background: linear-gradient(90deg, #2563eb 0%, #38bdf8 100%);
        color: #fff;
        border: none;
        box-shadow: 0 2px 8px 0 rgba(60,60,120,0.05);
    }
    """
) as demo:
    with gr.Column(elem_id="main-container"):
        gr.Markdown(
            "<div style='text-align:center;margin-bottom:18px;'>"
            "<span style='font-size:2.2rem;font-weight:800;color:#2563eb;'>KishlayBot</span><br>"
            "<span style='font-size:1.1rem;color:#64748b;'>Your Personal AI Assistant</span>"
            "</div>"
        )
        gr.ChatInterface(
            respond,
            examples=["Who is Kishlay?", "What projects has he built?", "Where is his resume?"],
            height=400,
            show_copy_button=True,
            show_share_button=False,
        )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
