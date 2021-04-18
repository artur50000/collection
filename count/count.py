from functools import lru_cache
import collections

@lru_cache(maxsize = 128)
def unique_letters(string_to_check):

    num_of_chars = 0
    collect = collections.Counter(string_to_check)

    for item in collect.values():
        if item == 1:
            num_of_chars += 1

    return num_of_chars
