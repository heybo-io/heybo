__author__ = "Tai Kersten"
import wikipedia as wiki


def skills_player():
    pass


def chunk_out(term_string, chunk_len = 40):
    counter = int(len(term_string)/chunk_len) 
    
    start_idx = 0
    end_idx = chunk_len
    
    return_list = []

    while counter >= 0:

        chunk = term_string[start_idx:end_idx]
        start_idx = end_idx
        end_idx += chunk_len
        return_list.append(chunk)        
        counter -=1

    return return_list
    


def wikipedia(term, chunk_len = 40):
    try:  
        my_search = wiki.summary('term')
        chuck_out(my_search)

    except:
        return ['Im Sorry I could not find a good search',]
