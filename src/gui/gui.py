from tkinter import *
import os
import webbrowser
import arxiv
import scholarly

class ImageButton:
    def __init__(
        self,
        path_to_img         : str,
        width               : int,
        height              : int,
        command             , #pressed callback
        master
    ):
        if not os.path.exists(path_to_img):
            photo = None
            self.button = None
            raise Exception("{} not found".format(path_to_img))
        else:
            photo = PhotoImage(
                master = master,
                file = path_to_img)
            
            photo = photo.subsample(
                photo.width() // width,
                photo.height() // height)

            self.button = Button(
                master = master,
                command = command
            )

            self.button.img = photo
            self.button.config(image = photo)

        

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
            self.entries_gui.append(w)


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
        
        # self.header = Text(self.box)
        # self.header.pack()
        # self.header.insert(END, self.entry['title'])
        #TODO: Add this later plz
        #self.header.config(font = ('Courier' , 26), height = 2)

        # self.authors = Text(self.box)
        # self.authors.pack()

        #TODO: I think that authors are in some other order that paper's
        authors_links = list()
        for author in self.entry['authors']:
            data = scholarly.search_author(author)

            label = Label(self.box, text=author, fg="blue" if data else "black", cursor="hand2")
            #label.pack(LEFT)
            authors_links.append(label)
            if data:
                scholar_link = "https://scholar.google.com/citations?user={}".format(next(data).id)
                authors_links[-1].bind("<Button-1>", lambda e: webbrowser.open_new_tab(scholar_link))

        # text = self.entry['summary']
        # self.w = Text(self.box)
        # self.w.pack()
        # self.w.insert(END, text)

        photo_img_w = 40
        photo_img_h = 40

         #TODO: fix this getcwd
        file = os.path.join(os.getcwd(),"data/gui_data/arxiv.png")
        command = lambda : webbrowser.open_new_tab(self.entry['arxiv_url'])
        pdf_button = ImageButton(
            path_to_img     =   file,
            width           =   photo_img_w,
            height          =   photo_img_h,
            command         =   command,
            master          =   self.box
        )
        pdf_button.button.pack(side = LEFT)

         #TODO: fix this getcwd
        file = os.path.join(os.getcwd(),"data/gui_data/pdf.png")
        command = lambda : webbrowser.open_new_tab(self.entry['pdf_url'])
        pdf_button = ImageButton(
            path_to_img     =   file,
            width           =   photo_img_w,
            height          =   photo_img_h,
            command         =   command,
            master          =   self.box
        )
        pdf_button.button.pack(side = LEFT)

        #arxiv.download(self.entry)
        


    