import tkinter
import json
import pprint

#dic = cl.OrderedDict()#順番付き辞書データ型
bd_width = 500     #frame h
bd_height = 500    #frame w
center_x = bd_width/2
center_y = bd_height/2
dic = {}

class Mindobj():
    md_dict={}
    posx=0
    posy=0
    def __init__(self,name):
        # super(Mindobj,self).__init__(md_dict)
        self.name = tkinter.StringVar()
        self.name.set(name) 
        self.lbl=tkinter.Label(textvariable = self.name)
        self.lbl.bind('<Button-1>',self.mindobj_print)
        self.lbl.bind('<Double-Button-1>',self.edit_label)

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
        print(self.md_dict)
        
        #vtext = self.md_dict["parent"] + "　→　" + text
        self.md_dict["parent"] = text
        self.name.set(text)
        pprint.pprint(self.md_dict)
        pprint.pprint(dic)

    def child_print(self):
        pprint.pprint(self.md_dict)
    
    def birth_child(self):
        if( len(self.md_dict["child"]) > 0 ):
            for i in range(len(self.md_dict["child"])):
                cy = self.posy + i*25
                cx = self.posy + 100
                mdo = Mindobj(self.md_dict["child"][str(i)]["parent"])
                mdo.md_dict = self.md_dict["child"][str(i)]
                mdo.lbl.place( x = cx ,y = cy )


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
    mdo = Mindobj(mind_dic[str(i)]["parent"])
    mdo.posy = center_y + i * 25
    mdo.posx = center_x + j
    mdo.md_dict = mind_dic[str(i)]
    mdo.child_print()
    mdo.lbl.place( x = mdo.posx ,y = mdo.posy )
    mdo.birth_child()


def main():
    global dic
    root = tkinter.Tk()
    root.title("tkinter test")
    root.geometry( str(bd_width) + "x" + str(bd_height))
    canvas = tkinter.Canvas(root, width = bd_width, height = bd_height)
    set_Mindobj(dic)
    root.mainloop()

if __name__ == "__main__":
    mind = Mind()
    mind.mind_print()#読み込んだJSONを表示する
    main()
