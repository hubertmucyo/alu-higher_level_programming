#!/usr/bin/python3


def best_score(a_):
    if a_ is None:
        return "None"
    elif len(a_) > 0:
        dict_me = dict(sorted(a_.items(), key=lambda x: x[1], reverse=True))
        list_me = list(dict_me)
        return list_me[0]
    else:
        return "None"
