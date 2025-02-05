import operator
from boardgame import BoardGame
class Executive:
    def __init__(self, ifile):
        self.bg_list = []
        f = open(ifile, 'r')
        f.readline()
        for line in f:
            self.bg_list.append(BoardGame(line.split('\t')))
        f.close()
        self.user_interface()
    def user_interface(self):
        print("Welcome to the Board Game Selector!")
        print("1. Display all board games")
        print("2. Display board games by Gibbons Rating")
        print("3. Display board games by BGG Average")
        print("4. Display board games by Average Weight")
        print("5. Display board games by Year Published")
        print("6. Display board games by BGG Best Players")
        print("7. Exit")
        choice = input("Please select an option: ")
        if choice == 1:
            self.display_all()
        elif choice == 2:
            self.display_gibbons()
        elif choice == 3:
            self.display_baverage()
        elif choice == 4:
            self.display_avgweight()
        elif choice == 5:
            self.display_yearpublished()
        elif choice == 6:
            self.display_bggbestplayers()
        elif choice == 7:
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            self.user_interface()

