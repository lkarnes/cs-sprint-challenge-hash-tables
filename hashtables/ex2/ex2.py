#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    storage = {}
    for i in tickets:
        storage[i.source] = i.destination
    pos = storage['NONE']
    route.append(pos)
    while pos != "NONE":
        route.append(storage[pos])
        pos = storage[pos]  
    print(route)
    return route
