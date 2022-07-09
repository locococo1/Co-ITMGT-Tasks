'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    out = ["follower", "followed by", "friends", "no relationship"]
    status = [to_member in social_graph[from_member]["following"], from_member in social_graph[to_member]["following"]]
    if status[0]+status[1]==2:
        return out[2]
    elif status[0]==0:
        if status[1]==1:
            return out[1]
        else:
            return out[3]
    else:
        return out[0]


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # get 2 unique symbols
    symbols = ['']
    for x in board:
        for y in x:
            if y not in symbols:
                symbols.append(y)
    del(symbols[0])
    
    # check board per symbol
    
    for x in symbols:
        #per row
        for row in board:
            if len(set(row))==1 and set(row)==set(x):
                return x
        
        #per column
        for col in zip(*board):
            if len(set(col))==1 and set(col)==set(x):
                return x

        #left diagonal
        if len(set([board[y][y] for y in range(len(board))])) == 1 and board[0][0] == x:
            return x

        #right diagonal
        if len(set([board[len(board) - y - 1][y] for y in range(len(board)-1,-1,-1)])) == 1 and board[len(board) - 1][0] == x:
            return x
    return "NO WINNER"
        
        
def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict 
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time=0;
    first=0;

    try:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]
    except:
        for i in range(2):
            for x in route_map:
                if x[0] == first_stop:
                    time = time + route_map[x]["travel_time_mins"];
                    first = 1;
                elif x[1] != second_stop and first==1:
                    time = time + route_map[x]["travel_time_mins"];
                elif x[1] == second_stop:
                    time = time + route_map[x]["travel_time_mins"];
                    first = 0;
            if i==0:
                time=0;
        return time