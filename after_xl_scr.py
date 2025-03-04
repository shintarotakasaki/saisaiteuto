# -*- coding: utf-8 -*-
"""after_xl_scr
Automatically generated by Colab.
Original file is located at
    https://colab.research.google.com/drive/1b3VXkHSUL8qaZE8LvrnmW17Nh3gh3TGN
"""

from openpyxl import load_workbook
import streamlit as st
from io import BytesIO
import requests
import shutil

# コメントアウトされたコード

def xl_data_upload():
    values = []
    
    after_xl = st.file_uploader("アフター申請書エクセルをアップロードしてください")

    if after_xl is not None:
        file_mime = after_xl.type
        if file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            try:
                file = BytesIO(after_xl.getvalue())
                wb = load_workbook(filename=file)
                sheet = wb.active
                #st.write(f"Sheet title: {sheet.title}")
                rects = ["G19","G20","L15","N20","G21","N21","G23","Q23","H28"]

                for rect in rects:
                #残しておきたいので取りあえずコメントアウト、あとで消す。

                    values.append(sheet[rect].value)
                
                for rect, value in zip(rects, values):
                    st.write(f"{rect}: {value}")
                
                return values

            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
                return None, None

        else:
            st.write("エクセルファイル(.xlsx)をアップロードしてください")
            st.stop()

        #残しておきたいので取りあえずコメントアウト、あとで消す。
        
        for label, value in zip(labels, values):
            st.write(f"**{label}**: {value}")

if __name__ == "__main__":
    xl_data_upload()
# ... (他のコードは省略)
