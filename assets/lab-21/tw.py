import mysql.connector as db

#
# Set up the database and cursor
#



#
# Begin the interaction
#
opts = [
    'Tweet!',
    'Show tweets',
    'List users',
    'Show tweets from user',
    'Like',
    'Quit',
]
user = input('Please enter your username: ')
while True:
    print()
    for i in range(len(opts)):
        print(' ' * 2, i + 1, opts[i])
    choice = int(input('Please enter your choice: '))

    #
    # Use the choice to decide which SQL statements to build and
    # execute
    #
