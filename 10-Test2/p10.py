def f(computer: set, smartphone: set):
    # Given a set of contacts, return the total number of friends

    all_friends = computer

    for friend in smartphone:
        all_friends.add(friend)

    return len(all_friends)


if __name__ == "__main__":
    computer = {'John', 'Peter'}
    smartphone = {'Peter','Frank','Ann'}

    print(f(computer,smartphone)) # returns 4
    
    computer = {'Breeze','Huter','Walker','Chaser','Camper','Owl'}
    smartphone = {'Breeze','Owl','Storm','Walker'}

    print(f(computer,smartphone)) # returns 7