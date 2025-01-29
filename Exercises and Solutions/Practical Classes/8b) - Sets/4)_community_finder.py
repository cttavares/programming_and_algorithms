mixed_characters = [
    'Abraham Lincoln',         # Historical figure
    'Queen Elizabeth II',      # Historical figure
    'Winston Churchill',       # Historical figure
    'Superman',                # Fictional character
    'Cleopatra',               # Historical figure
    'Jon Snow',                # Fictional character
    'Tyrion Lannister',        # Fictional character
    'Ron Swanson',             # Fictional character
    'Julius Caesar',           # Historical figure
    'Vladimir Putin',          # Political figure
    'Angela Merkel',           # Political figure
    'The Joker',               # Fictional character
    'Lady Gaga',               # Celebrity
    'Homer Simpson',           # Fictional character
    'Napoleon Bonaparte',      # Historical figure
    'Barack Obama',            # Political figure
    'Gandhi',                  # Historical figure
    'Captain Jack Sparrow',    # Fictional character
    'Daenerys Targaryen',      # Fictional character
    'Elizabeth II',            # Historical figure (to create a fun twist with Queen Elizabeth II)
    'Sherlock Holmes',         # Fictional character
    'Margaret Thatcher',       # Historical figure
    'Harry Potter',            # Fictional character
]

# Hypothetical friendships that create more interconnections
ironic_friendships = [
    ('Abraham Lincoln', 'Sherlock Holmes'),
    ('Queen Elizabeth II', 'Elizabeth II'),  # An amusing "self" friendship
    ('Winston Churchill', 'Margaret Thatcher'),
    ('Superman', 'Harry Potter'),
    ('Cleopatra', 'Daenerys Targaryen'),
    ('Jon Snow', 'Tyrion Lannister'),  # From the same fictional universe
    ('Ron Swanson', 'Margaret Thatcher'),  # Amusing political twist
    ('Julius Caesar', 'Napoleon Bonaparte'),
    ('Vladimir Putin', 'Gandhi'),  # An ironic peaceful vs. strongman leadership
    ('Angela Merkel', 'Barack Obama'),
    ('The Joker', 'Tyrion Lannister'),  # The masterminds
    ('Lady Gaga', 'Daenerys Targaryen'),  # Queens of their own realms
    ('Homer Simpson', 'Jon Snow'),  # Oblivious to some realities
    ('Napoleon Bonaparte', 'Gandhi'),  # Historic figures from different times
    ('Barack Obama', 'Sherlock Holmes'),  # Analytical minds
    ('Gandhi', 'Superman'),  # Figures of peace and justice
    ('Captain Jack Sparrow', 'The Joker'),  # Chaotic characters
    ('Daenerys Targaryen', 'Cleopatra'),  # Rulers of ancient and fictional lands
    
    # ... additional friendships
]

list_of_sets = []
for i in ironic_friendships:
    added = False
    for j in list_of_sets:
        if i [0] in j or i [1] in j:
            j.add (i [0])
            j.add (i [1])
            added = True

    if added == False:
        a = set ()
        a.add (i [0])
        a.add (i [1])
        list_of_sets.append (a)

print (list_of_sets)
i = 0
while i < len (list_of_sets):
    if list_of_sets [i] != {}:
        j = 0
        while j < len (list_of_sets):
            if i != j:
                print ("Intersection of ", list_of_sets [i], " and ", list_of_sets [j], " is ", list_of_sets [i] & list_of_sets [j])
                if len (list_of_sets [i] & list_of_sets [j]) != 0:
                    list_of_sets [i] = list_of_sets [i] | list_of_sets [j]
                    list_of_sets [j] = set ()
            j += 1
    i = i + 1 



print (list_of_sets)


