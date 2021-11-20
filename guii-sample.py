import tkinter
from tkinter.constants import INSERT

def btn_click():
    print('テスト')

# 画面作成
tki = tkinter.Tk()
tki.title("TK-test")
tki.geometry("700x500")

# ラベル
lbl_1 = tkinter.Label(text='name')
lbl_1.place(x=30, y=70)
lbl_2 = tkinter.Label(text='')
lbl_2.place(x=30, y=100)

# insert txt
lbl_1.INSERT(tkinter.end,"hoge")

# テキストボックス
txt_1 = tkinter.Entry(width=20)
txt_1.place(x=130, y=70)
txt_2 = tkinter.Entry(width=20)
txt_2.place(x=130, y=100)

# ボタン
btn = tkinter.Button(tki, text='result', command=btn_click)
btn.place(x=140, y=170)

# 画面をそのまま表示
tki.mainloop()
