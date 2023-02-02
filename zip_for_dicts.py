def dict_zip(*dicts):
    if not dicts:
        return

    n = len(dicts[0])
    if any(len(d) != n for d in dicts):
        raise ValueError("Arguments must all be of same length!")
    
    for key, first_val in dicts[0].items():
        yield key, first_val, *(other[key] for other in dicts[1:])
        
# https://www.youtube.com/watch?v=k2ZWyHdahEk&list=WL&index=37
