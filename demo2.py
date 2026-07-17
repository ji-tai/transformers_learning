from transformers import pipeline
import gradio as gr

# 加载模型
classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")

# 定义一个预测函数
def predict(text):
    result = classifier(text)[0]
    return f"{result['label']} (置信度: {result['score']:.2f})"

# 手动创建 Interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="输入评论"),
    outputs=gr.Textbox(label="预测星级"),
    title="多语言情感分析"
)

interface.launch()