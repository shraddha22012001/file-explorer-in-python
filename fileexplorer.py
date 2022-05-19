
import os

while True:
    def menu():
        x = ('1. Create File \n2. Write \n3. Read \n4. ReadLine\n5. Append\n6. Copy File1 to file2 \n7. Remove \n8. Exit\n') 
        print(x)
    menu()
    choice = int(input('Please select one of the following : ')) 
    if choice == 1:
        path = 'F:\documents\quantiphi training\python training'
        file = 'myfile.txt'
        dir_list = os.listdir(path)
        print("List of directories and files before creation:")
        print(dir_list)
        print()

        with open(os.path.join(path, file), 'w') as fp:
            pass
            
        dir_list = os.listdir(path)
        print("List of directories and files after creation:")
        print(dir_list)
    elif choice == 2:
        file1 = open("myfile.txt","w")
        L = ["This is First line \n","This is Second Line \n","This is Third Line \n"] 
        file1.write("Hello \n")
        file1.writelines(L)
        file1.close() #to change file access modes
        print("\nfile write  operation performed successfully!!")
    elif choice == 3:
        if os.path.exists("myfile.txt"):
            file1 = open("myfile.txt","r+") 
            print("Output of Read function is ")
            print(file1.read())
            print()
            file1.close()  
        else:
            print("\nThe file does not exist")
    elif choice == 4:
        if os.path.exists("myfile.txt"):
            file1 = open("myfile.txt","r+")
            file1.seek(0)
            # readlines function
            print("\nOutput of Readlines function is ") 
            print(file1.readlines()) 
            print()
            file1.close()
        else:
            print("\nThe file does not exist")
    elif choice == 5:
        if os.path.exists("myfile.txt"):
            file1 = open("myfile.txt","a")
            L = ["This is forth line \n","This is fifth Line \n","This is sixth Line \n"] 
            file1.writelines(L)
            file1.close() #to change file access modes
            print("\nfile append operation performed successfully!!")
        else:
            print("\nThe file does not exist")
    elif choice == 6:
        if os.path.exists("myfile.txt"):
            with open('first.txt','r') as firstfile, open('myfile.txt','a') as secondfile:
                
                # read content from first file
                for line in firstfile:
                        
                        # append content to second file
                        secondfile.write(line)
            print("\nThe file content copied into your file ")
        else:
             print("\nThe file does not exist")
    elif choice == 7:
        if os.path.exists("myfile.txt"):
          os.remove("myfile.txt")
          print("\n File removed successfully")
        else:
          print("\nThe file does not exist")
    elif choice == 0:
        print('\nAgain try one of the following')
        break
    else:
        break       
print()





 



