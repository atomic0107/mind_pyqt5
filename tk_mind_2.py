"""

"""
import tkinter
import json
import pprint
import numpy as np
import math

bd_width = 500     #frame h
bd_height = 500    #frame w
center_x = bd_width/2
center_y = bd_height/2
PC_width = 100
Child_width = 25
TXT_W = 6
TXT_H = 10
dic = {}

class Mindobj():
    md_dict = {}
    posx = 0
    posy = 0
    width = 0
    global canvas

    def __init__(self,name,x,y):
        self.canvas = canvas
        self.posx = x
        self.posy = y
        self.name = tkinter.StringVar()
        self.width = len(name)*TXT_W
        self.name.set(name) 
        self.tag = self.canvas.create_text(self.posx,self.posy,text = self.name.get())
        self.canvas.tag_bind(self.tag,'<Button-1>',self.mindobj_print)
        self.canvas.tag_bind(self.tag,'<Double-Button-1>',self.edit_label)
        self.set_position()

    def set_position(self):
        pass

    def mindobj_print(self,event):
        print("click mind obj")
    
    def edit_label(self,event):
        self.temp_label = event.widget
        print("#### edit label ####")
        editbox = tkinter.Entry()
        editbox.insert(tkinter.END , self.name.get())
        editbox.place( x = self.posx , y = self.posy )
        editbox.focus_set()#editbox active
        editbox.bind( '<Return>', self.update_label )#enter key
    
    def update_label(self,event):
        text = event.widget.get()
        event.widget.destroy()
        self.md_dict["parent"] = text
        self.name.set(text)
        self.canvas.delete(self.tag)
        self.canvas.create_text(self.posx,self.posy,text = self.name.get())

    def child_print(self):
        pprint.pprint(self.md_dict)
    
    def birth_child(self):
        if( self.md_dict.get("child") ):
            for i in range(len(self.md_dict["child"])):
                cy = self.posy - ( Child_width * (len(self.md_dict["child"])- 1) / 2.0 ) + i * Child_width
                cx = self.posx + PC_width
                mdo = Mindobj(self.md_dict["child"][str(i)]["parent"],cx,cy)
                mdo.md_dict = self.md_dict["child"][str(i)]
                mdo.md_dict.setdefault("id_parent",self)
                mdo.md_dict.setdefault("id_object",mdo)
                mdo.birth_child()

                linex = np.arange(self.posx ,mdo.posx,1)#xの標本数
                amin = self.posy + TXT_H#描画開始位置
                amax = mdo.posy + TXT_H#描画終了位置
                x0 = self.posx + ( abs( ( self.posx  ) - mdo.posx ) / 2 )#傾き最大位置
                h = 15#傾き最大
                s = 5#s > 0
                f = []
                for x in linex:
                    y = curve_mind(amin,amax,x,x0,h,s)
                    f.append(x)
                    f.append(y)
                canvas.create_line(f,fill="blue", width=1, smooth=True)

class Mind():
    def __init__(self):
        global dic
        f = open("mind.json", 'r')
        dic = json.load(f) #JSON形式で読み込む
        f.close()
        print("print read json!")
        self.mind_dic = dic

    def mind_print(self):#読み込んだjsonを表示
        print("hello my mind world!!")

def set_Mindobj(dict):
    mind_dic = dict
    print("----------set_Mindobj()---------")
    print("parent = " + str(len(mind_dic)))
    j = 0
    i = 0
    """
    for i in range(len(mind_dic)):
        cy = center_y + i * 25
        cx = center_x + j
        lbl = Mindobj(text = mind_dic[str(i)]["parent"])
        lbl.place( x = cx ,y = cy )
        print("child = " + str(len(mind_dic[str(i)]["child"])))
        if( len(mind_dic[str(i)]["child"]) > 0 ):
            child_mind_dic = mind_dic[str(i)]["child"]
            j = 100
            k = i+1
            print(child_mind_dic[str(k)])
            set_Mindobj(child_mind_dic[str(k)]["child"])
    """
    cy = center_y + i * 25
    cx = center_x + j
    mdo = Mindobj(mind_dic[str(i)]["parent"],cx,cy)
    mdo.md_dict = mind_dic[str(i)]
    mdo.md_dict.setdefault("id_object",mdo)
    mdo.birth_child()

def main():
    global dic
    global canvas
    root = tkinter.Tk()
    root.title("tkinter test")
    canvas = tkinter.Canvas( width = bd_width, height = bd_height)
    root.geometry( str(bd_width) + "x" + str(bd_height))
    set_Mindobj(dic)
    canvas.pack()#canvas set object
    root.mainloop()

"""
amin    : 描画開始位置
amax    : 描画終了位置
x       : xの標本数
x0      : 傾きが最大になるx座標
h       : 傾き
s       : s > 0
"""
def curve_mind(amin,amax,x,x0,h,s):
    y1 = amin
    y2 = amax - amin
    y3 = (x/x0)**(-1*h)
    y4 = 1 + (y3**s)
    f = y1 + ( y2 / y4 )
    #f = (a*b)/(a+(b-a)*np.exp(-1*c*t))
    return f

if __name__ == "__main__":
    mind = Mind()
    #mind.mind_print()#読み込んだJSONを表示する
    main()
