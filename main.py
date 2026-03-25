import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

import time

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.03)

'Done!!!!!'
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答を書く')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答を書く')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：', text
# 'コンディション：', condition
# if st.checkbox('Show Image'):
#     img = Image.open('アイコン用.png')
#     st.image(img, caption='urara&paisen&nyanta', width=350)
