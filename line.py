import tkinter
bd_width = 500     #frame h
bd_height = 500    #frame w
center_x = bd_width/2
center_y = bd_height/2

root = tkinter.Tk()
root.title("tkinter test")
canvas = tkinter.Canvas( width = bd_width, height = bd_height)
root.geometry( str(bd_width) + "x" + str(bd_height))
line_array = [0,0,50,100,100,50]
canvas.create_line(line_array,fill="blue", width=1, smooth=False)

canvas.pack()#canvas set object

root.mainloop()


