# 样例1：文本分类
# 导入gradio
import gradio as gr
# 导入transformers相关包
import transformers
# 通过Interface加载pipeline并启动文本分类服务
print("当前 Gradio 版本:", gr.__version__)
print("当前 Transformers 版本:", transformers.__version__)