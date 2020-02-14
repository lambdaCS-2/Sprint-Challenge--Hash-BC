#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
        # subtract the current value from the limit and store the difference 
        # which will be the number we are looking for in the hashtable 

        diff = limit - weights[i]
        # search the hashtable for a match to the difference
        match = hash_table_retrieve(ht, diff)
        if match is not None:
            #  if match is found return with the current index first
            return [i, match]
        # if there is no match, store the current value in the hashtable and keep looking
        hash_table_insert(ht, weights[i], i)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
