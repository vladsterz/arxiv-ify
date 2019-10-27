import time

#from src.utilities import get_entries_by_date
from src.arxiv.queries_manager import ArxivManager
from src.gui.gui import ArxivEntriesManager
def main():
    man = ArxivManager()
    man.do_query(field = "cs.CV")

    works = man.get_by_date(2019,10,24)

    manager = ArxivEntriesManager(10, works)
    manager.top.mainloop()

    breakpoint = True


if __name__ == "__main__":
    main()