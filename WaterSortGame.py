from Structures import *


class WaterSortGame:
    def __init__(self, colors_list, max_bottle_size):
        self.tubes = LinkedList()
        self.max_bottle_size = max_bottle_size
        self.colors = colors_list
        self.num_bottles = len(self.colors) + 1
        self.initialize_tubes()
        self.selected_bottle = 0

    def initialize_tubes(self):
        for _ in range(self.num_bottles - 1):  # Create n color-filled tubes
            self.tubes.append(Stack(self.max_bottle_size))

        self.tubes.append(Stack(self.max_bottle_size))  # Plus one extra tube for being empty

        # Randomly distribute the colors into the bottles
        all_colors = self.colors * self.max_bottle_size  # Repeat each color max_bottle_size times

        random.shuffle(all_colors)  # Shuffle the colors

        current_colors_index = 0
        for tube in self.tubes:
            while not tube.is_full() and current_colors_index < len(all_colors):
                tube.push(all_colors[current_colors_index])
                current_colors_index += 1

        # Shuffle the bottles to randomly distribute the empty bottle
        nodes = [node for node in self.tubes]
        random.shuffle(nodes)

        # Rebuild the LinkedList with shuffled nodes
        self.tubes = LinkedList()
        for node in nodes:
            self.tubes.append(node)

    def display_game_state(self):
        if self.selected_bottle != 0:
            self.selected_bottle -= 1
        tube_states = self.tubes.to_list_of_lists()
        max_level = max(len(tube) for tube in tube_states)

        # Determine the width of the column based on the longest color name
        column_width = max(len(color) for color in self.colors) + 2  # Add some padding

        # Print the state of all tubes, row by row
        for level in range(max_level):
            for tube_index, tube in enumerate(tube_states):
                # Use string formatting to maintain column width
                color = tube[level] if level < len(tube) else "Empty"
                print(f"{color:<{column_width}}", end="")
                # Print separator line if on the bottom row of the highlighted tube
            print()
        seperator = " " * (column_width * self.selected_bottle) + '---#---'
        print(seperator)



def main():
    print("Enter a space-separated list of colors followed by the maximum bottle size:")
    user_input = input()
    parts = user_input.split()


    if parts[0] == 'start' and len(parts) > 2:
        colors_list = parts[1:-1]
        max_bottle_size = int(parts[-1])

        game = WaterSortGame(colors_list, max_bottle_size)
        game.display_game_state()
        game.select(3)
    else:
        print("Invalid input format. Please use the format: 'start color1 color2 ... colorN maxBottleSize'")


if __name__ == "__main__":
    main()