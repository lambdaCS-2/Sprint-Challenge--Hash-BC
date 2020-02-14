#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
  
    # create hashtable to store all the tickets
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    #  start point will have no source
    # route[0] = hash_table_retrieve(hashtable, 'NONE')

    current = 'NONE'

    # skip the first one because it is set manually
    for i in range(length):
        
            
        # use previous destination to find the next destination
        # Then, when constructing the entire route, the `i`th location 
        # in the route can be found by checking the hash table for the `i-1`th location.
        route[i] = hash_table_retrieve(hashtable, current)
        current = route[i]


    return route[:-1]



