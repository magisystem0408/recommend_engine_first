import streamlit as st
# import pandas as pd
from git.objects.base import Object

# ここでモデルをインポートする
# df =pd.read_csv("ratings.csv")

class RecomenndApp(Object):
    def __init__(self):
        self.serchWord = ""
        self.sideBarGui()
        self.mainGui()
    def sideBarGui(self):
        self.serchWord = st.sidebar.text_input("検索ワードを入力してください")
        st.sidebar.button("送信する")

    def mainGui(self):
        st.write(self.serchWord)
        # st.write(df.head())

        if not self.serchWord == "":
            # 入力された値はself.serchWordに格納されるので、学習させる。
            # 直し、モデル学習等が重すぎるので、マルチスレッド開いた方がいいかも
            print("ここでモデル処理判定をする")


if __name__ == '__main__':
    app = RecomenndApp()

