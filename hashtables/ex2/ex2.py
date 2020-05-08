#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    table = {}
    for tick in tickets:
        table[tick.source] = tick.destination
    route = []
    place = table['NONE']
    for i in range(length):
        route.append(place)
        place = table[place]

    return route
