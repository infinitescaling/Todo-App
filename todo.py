import os 
class Todolist:

    def __init__(self):
        self.list = []
        list_file = open('listfile.txt', 'r+')
        for line in list_file:
            if line != "" or line != '\n':
                self.add_list(line)

    def get_list(self):
        for item in self.list:
            print item

    def add_list(self, item):
        item = item.strip()
        self.list.append(item)
        print "Item added is " + item

    def remove_list(self, item):
        item = item.strip()
        if item in self.list:
            self.list.remove(item)
    
    def save_list(self):
        path = '/Users/scalingasan/projects/python/todo/'
        os.remove(path+'listfile.txt')
        
        list_file = open('listfile.txt', 'w+')
        for item in self.list:
            if item != "" or item != '\n':
                list_file.write("%s\n" % item)
    


def main():
   new_list = Todolist()
   print "1. Get List"
   print "2. Add to List"
   print "3. Remove from List"
   print "4. Exit"
   while(1):
       input = raw_input("Choose option: ")
       if int(input) < 5 and int(input) > 0:
           if int(input) == 1:
               new_list.get_list()
           elif int(input) == 2:
               input = raw_input("Add an item\n")
               new_list.add_list(input)
           elif int(input) == 3:
               input = raw_input("Remove an item\n")
               new_list.remove_list(input)
           else:
               break
       else:
           print "Bad input"
   new_list.save_list()

main()
