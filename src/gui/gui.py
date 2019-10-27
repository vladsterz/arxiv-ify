from tkinter import *
import os
import webbrowser
import arxiv

class ArxivEntriesManager:
    def __init__(
        self,
        number_to_show      : int,
        entries             : list
    ):
        self.n = number_to_show
        self.entries = entries
        self.top = Tk()
        self.entries_gui = []

        for i in range(self.n):
            w = ArxivEntryGui(
                self.entries[i],
                500,
                self.top
            )
            self.entries.append(w)


class ArxivEntryGui:
    def __init__(
        self,
        entry       : dict,
        width       : int,
        master
    ):
        self.width = width
        self.entry = entry
        self.master = master

        button = Button(
            master = self.master,
            text = entry['title'],
            width = self.width,
            command = self.is_pressed)
        
        button.pack()

    def is_pressed(self):
        self.box = Tk(className=self.entry['title'])
        text = self.entry['summary']
        self.w = Text(self.box)
        self.w.pack()
        self.w.insert(END, text)

        photo_img_w = 40
        photo_img_h = 40

        #TODO: fix this getcwd
        file = os.path.join(os.getcwd(),"data/gui_data/arxiv.png")
        if os.path.exists(file):
            arxiv_photo = PhotoImage(
                master = self.box,
                file = file)
            
            arxiv_photo = arxiv_photo.subsample(
                arxiv_photo.width() // photo_img_w,
                arxiv_photo.height() // photo_img_h)
        else:
            arxiv_photo = None
        
        arxiv_button = Button(
            master = self.box,
            command = lambda : webbrowser.open_new_tab(self.entry['arxiv_url'])
        )
        arxiv_button.img = arxiv_photo
        arxiv_button.config(image = arxiv_photo)
        arxiv_button.pack(side = LEFT)

         #TODO: fix this getcwd
        file = os.path.join(os.getcwd(),"data/gui_data/pdf.png")
        if os.path.exists(file):
            pdf_photo = PhotoImage(
                master = self.box,
                file = file)
            
            pdf_photo = pdf_photo.subsample(
                pdf_photo.width() // photo_img_w,
                pdf_photo.height() // photo_img_h)
        else:
            pdf_photo = None
        
        pdf_button = Button(
            master = self.box,
            command = lambda : webbrowser.open_new_tab(self.entry['pdf_url'])
        )
        pdf_button.img = pdf_photo
        pdf_button.config(image = pdf_photo)
        pdf_button.pack(side = LEFT)

        arxiv.download(self.entry)
        


    