'''
Class that holds metadata of queries made.
Will definetly update later.
'''
import arxiv
class ArxivManager:
    def __init__(self):
        self.queries = []
        self.last_start = 0
        self.max_results = 100 
    

    def do_query(
        self            ,
        field           : str
    ):
        query_result = arxiv.query(
            search_query=field,
            sort_by="submittedDate",
            start=self.last_start,
            max_results=self.max_results)
        
        self.last_start += self.max_results
        self.queries += query_result

    def get_by_date(
        self            ,
        year            : int,
        month           : int,
        day             : int
    ):
        #pass
        return [x for x in self.queries if x['updated_parsed'][:3] == (year,month,day)]