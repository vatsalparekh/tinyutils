def next_to(input_list, search_term, place=1,
            search_base=None, search_end=None):

    try:
        if search_base is not None:
            search_base = input_list.index(search_base)

        if search_end is not None:
            search_end = input_list[
                (search_base):].index(search_end) + search_base
    except ValueError:
        search_base, search_end = None, None
        print ("ValueError!!! Values taken as default.")

    effective_list = input_list[search_base:search_end]

    try:
        if search_term in effective_list:
            return effective_list[effective_list.index(search_term) + place]
        else:
            return "Not Found"
    except IndexError:
        return None
