from docx import Document
from docx.shared import RGBColor

def add_content_mode1(doc, content):
    '''
    增加内容
    '''
    para = doc.add_paragraph().add_run(content)
    # 设置字体格式
    para.font.name = '仿宋'
    # 设置下划线
    para.font.underline = True
    # 设置颜色
    para.font.color.rgb = RGBColor(255,128,128)  

doc = Document('./demo.docx')

add_content_mode1(doc, 'Hello Python!!!')

paragraphs = doc.paragraphs

for para in paragraphs:
    print(para.text)