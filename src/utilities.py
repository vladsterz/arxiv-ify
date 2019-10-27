def is_same_date(date1 , date2):
    '''Compares two dates acquired from time library'''
    is_same = True
    for i in range(3):
        is_same &= date1[i] == date2[i]
    return is_same

def get_entries_by_date(query_results, date):
    result_list = []
    for result in query_results:
        entry_date = result["published_parsed"]
        if is_same_date(date, entry_date):
            qq = True

#def get_latest_enties_