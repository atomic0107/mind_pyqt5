import sys
import tkinter

#
# GUI設定
#
root = tkinter.Tk()
root.title(u"TkinterのCanvasを使ってみる")
root.geometry("800x450")


#「描く」ボタンが押されたら
def draw(event):
    canvas.create_oval(10, 10, 140, 140, tag="oval")


#「消す」ボタンが押されたら
def erase(event):
    canvas.delete("oval")



#キャンバスエリア
canvas = tkinter.Canvas(root, width = 800, height = 300)

#円を描く
canvas.create_oval(10, 10, 140, 140, tag="oval")

#キャンバスバインド
canvas.place(x=0, y=0)



# 「描く」ボタン
button_draw = tkinter.Button( text=u'描く',width=15)
button_draw.bind("<Button-1>",draw)
button_draw.place(x=100,y=350)


# 「消す」ボタン
button_draw = tkinter.Button( text=u'消す',width=15)
button_draw.bind("<Button-1>",erase)
button_draw.place(x=350,y=350)


#
# GUIの末端
#
root.mainloop()