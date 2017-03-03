def chance_of_occurrence(events):
    """
    This is a model to assess the discrete probability of a set of events.
    We are assuming every event occurs at least once.
    Input:
    @events - a enumeration of the total occurences for a set of events.
    * type: list
        
    Output:
    @probabilities - a list of the resulting probabilities of each event.
    * type: list  
    """
    universe_of_events = len(events)
    frequencies_of_occurrence = {}
    for event in events:
        if event in frequencies_of_occurrence.keys():
            frequencies_of_occurrence[event] += 1
        else:
            frequencies_of_occurrence[event] = 1
    probabilities = {}
    for event in frequencies_of_occurrence.keys():
        probabilities[event] = frequencies_of_occurrence[event]*(1/universe_of_events)
    return probabilities

#import random
#events = []
#for _ in range(10000000000000):
#    events.append(random.choice(["h","t"]))
    
def are_events_fair(probabilities):
    """
    This function asks if all the events of a set of probabilities are equally likely
    Input:
    @events - a dictionary of events where each event is the key 
    and each value is it's associated probability
    * type: dictionary
    
    Output:
    @result - A boolean saying whether or not the events are fair, True means fair, 
    False means not fair
    * type: boolean
    """
    total_number_of_events = len(probabilities.keys())
    fair_probability = 1/float(total_number_of_events)
    for event in probabilities.keys():
        if probabilities[event] != fair_probability:
            return False
    return True

chance_of_occurrence([1,1,1,4,3,5,6,2,1,2,3,4,5,1,2,3,5,6,2,3,4,5,2])
print(chance_of_occurrence(["sad","kinda sad","sad","happy","kinda happy","happy","happy"]))
