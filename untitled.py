import random, time

# Set up the constants:
MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40  # (!) Try modifying this number.

def get_racers():
    # Ask how many snails to race:
    while True:  # Keep asking until the player enters a number.
        print(f'How many snails will race? Max: {MAX_NUM_SNAILS}')
        response = input('> ')
        if response.isdecimal():
            num_snails = int(response)
            if 1 < num_snails <= MAX_NUM_SNAILS:
                break
        print(f'Enter a number between 2 and {MAX_NUM_SNAILS}')

def draw_track():
  

    # Enter the names of each snail:
    snail_names = []  # List of the string snail names.
    for i in range(1, num_snails + 1):
        while True:  # Keep asking until the player enters a valid name.
            print('Enter snail #' + str(i) + "'s name:")
            name = input('> ')
            if len(name) == 0:
                print('Please enter a name.')
            elif name in snail_names:
                print('Choose a name that has not already been used.')
            else:
                break  # The entered name is acceptable.
        snail_names.append(name)
    
    return num_snails, snail_names

def draw_track():
    # Display each snail at the start line.
  print('\n' * 40)
  print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
  print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
  snail_progress = {}
  for name in snail_names:
      print(name[:MAX_NAME_LENGTH])
      print('@v')
      snail_progress[name] = 0

def main():
   # Display the snails (with name tags):
    for name in snail_names:
        spaces = snail_progress[name]
        print((' ' * spaces) + name[:MAX_NAME_LENGTH])
        print(('.' * snail_progress[name]) + '@v')
	
 
