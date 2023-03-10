print("******** into file_append.py ********")

# a = append - add the content to the end of content..
# open the file for append contact, if not exist create new one
def demo1():
    print("demo1")
    my_file1 = open('demo_files/demo_append_to_file1.txt', 'a')
    my_file1.write('\n hola class we create NEW File and write in file.. \nPython.. :) ')
    my_file1.close()


# Example - append to file with Hebrew
def demo2():
    my_file2 = open("demo_files/demo_append_to_file2.txt", 'a', encoding='utf-8')
    my_file2.write("שורה חדשה התווספה.. \n")    # encoding='utf-8'
    my_file2.close()


# Example - append to python file
def demo3():
    my_file3 = open('demo_files/demo_append_to_python_file.py', 'a')
    my_file3.write("""print('Hola')\n""")
    my_file3.close()


def play():
    demo = input("Enter number demo / 0 = End ")
    if demo == "0":
        return
    elif demo == "1":
        demo1()
    elif demo == "2":
        demo2()
    elif demo == "3":
        demo3()
    play()

play()