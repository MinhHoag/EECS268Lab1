from executive import Executive

def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.run()

if __name__ == "__main__":
  main()
with open('gibbons-boardgames.tsv', 'r') as f:
    boardgamelist = f.readline()
my_list = boardgamelist.split()
print my_list