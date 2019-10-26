import arxiv
import time

from source.utilities import get_entries_by_date
def main():
    query_result = arxiv.query(search_query="cs.GR", sort_by="submittedDate", max_results=10)
    today = time.gmtime()
    today[2] -= 3
    get_entries_by_date(query_result, today)
    print("\n\n\n")
    query_result = arxiv.query(search_query="cs.GR", sort_by="submittedDate", max_results=10, start = 1)

    get_entries_by_date(query_result, today)

    breakpoint = True


if __name__ == "__main__":
    main()