import ytube_module as m
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import  threading
def click_func():
    url=yt_url.get()
    try:
        YouTube(url)
    except:
        messagebox.showerror('錯誤,pytube不支此影片或者網址錯')
        return
    urls = m.get_urls(url)
    if urls and messagebox.askyesno('確認方塊,是否下载清单内所有影片?(逛择否N)則下載单一影片)'):
        print('開始下載')
        for u in urls:
            threading.Thread(target = m.start_dload,args=(u,listbox)).start()
    else:
        yt = YouTube(url)
        if messagebox.askyesno('確認方塊',f'是否下载(yt.title)影片?'):
            threading.Thread(target = m.start_dload,args=(url,listbox)).start()
        else:
            print('取消下載')
window=tk.Tk()
window.geometry('640x480')
window.title('YouTube下載器')

input_fm=tk.Frame(window,bg='lightblue',width=640,height=240)
input_fm.pack()

lb=tk.Label(input_fm,text='請輸入Youtube影片網址',bg='white',fg='black',font=('微軟正黑體',12))
lb.place(rely=0.25,relx=0.5,anchor='center')

yt_url=tk.StringVar()
entry=tk.Entry(input_fm,textvariable=yt_url,width=50)
entry.place(rely=0.5,relx=0.5,anchor='center')

btn=tk.Button(input_fm,text='下載影片',command=click_func,bg='lightblue',fg='Black',font=('微軟正黑體',12))
btn.place(rely=0.5,relx=0.85,anchor='center')

dload_fm = tk.Frame(window,width=640,height=480-120)
dload_fm.pack()

lb=tk.Label(dload_fm,text='下载状態',fg='Black',font=('微軟正黑體',15))
lb.place(rely=0.1,relx=0.,anchor='center')
         
listbox = tk.Listbox(dload_fm, width=65, height=15)
listbox.place(rely=0.5, relx=0.5,anchor='center')


sbar = tk.Scrollbar(dload_fm)
sbar.place(rely=0.5, relx=0.87, anchor='center', relheight=0.7)

listbox.config(yscrollcommand= sbar.set)
sbar.config(command = listbox.yview)

window.mainloop()