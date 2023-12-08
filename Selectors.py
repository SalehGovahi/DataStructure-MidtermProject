from WaterSortGame import WaterSortGame

def select(WaterSortGame, bottle_number):
    WaterSortGame.selected_bottle = bottle_number
    WaterSortGame.display_game_state()
    
def deselect(WaterSortGame):
    WaterSortGame.selected_bottle = 1
    
def select_next(WaterSortGame):
    if WaterSortGame.selected_bottle == WaterSortGame.num_bottles:
        print("It is the last bottle")
    else:
        WaterSortGame.selected_bottle += 1
    
def select_previous(WaterSortGame):
    if WaterSortGame.selected_bottle == 1:
        print("It is the first bottle")
    else:
        WaterSortGame.selected_bottle -= 1