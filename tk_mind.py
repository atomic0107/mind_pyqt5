import tkinter
import json
import pprint

#dic = cl.OrderedDict()#順番付き辞書データ型
bd_width = 500     #frame h
bd_height = 500    #frame w
center_x = bd_width/2
center_y = bd_height/2
dic = {}

class Mindobj(tkinter.Label):
    def __init__(self,master=None,cnf={},**kw):
        tkinter.Label.__init__(self,master,cnf,**kw)
        self.bind('<Button-1>',self.mindobj_print)
        self.bind('<Double-Button-1>',self.edit_label)

    def mindobj_print(self,event):
        print("click mind obj")
    
    def edit_label(self,event):
        self.temp_label = event.widget
        print("#### edit label ####")
        edit_x = event.widget.winfo_x()
        edit_y = event.widget.winfo_y()
        editbox = tkinter.Entry()
        editbox.insert(tkinter.END,self.temp_label[u"text"])
        editbox.place( x = edit_x,y = edit_y )
        editbox.focus_set()#editbox active
        editbox.bind( '<Return>', self.update_label )#enter key
    
    def update_label(self,event):
        text = event.widget.get()
        event.widget.destroy()
        self.temp_label[u"text"] = text
        print(text)

class Mind():
    def __init__(self):
        global dic
        f = open("mind.json", 'r')
        dic = json.load(f) #JSON形式で読み込む
        f.close()
        print("print read json!")
        pprint.pprint(dic)
        self.mind_dic = dic

    def mind_print(self):#読み込んだjsonを表示
        print("hello my mind world!!")
        pprint.pprint(self.mind_dic)
        print(len(self.mind_dic["0"]["child"]))

def set_Mindobj():
    global dic
    mind_dic = dic
    print("----------set_Mindobj()---------")
    print("parent = " + str(len(mind_dic)))
    for i in range(len(mind_dic)):
        cy = center_y + i * 25
        cx = center_x
        lbl = Mindobj(text = mind_dic[str(i)]["parent"])
        lbl.place( x = cx ,y = cy )
        print("child = " + str(len(mind_dic[str(i)]["child"])))


def main():
    root = tkinter.Tk()
    root.title("tkinter test")
    root.geometry("500x500")
    set_Mindobj()
    root.mainloop()

if __name__ == "__main__":
    mind = Mind()
    mind.mind_print()#読み込んだJSONを表示する
    main()
