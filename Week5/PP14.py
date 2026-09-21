myQueue = []
def enqueue():
    element = int(input("Enter a number:"))
    myQueue.append(element)
    print(myQueue)


def dequeue():
    myQueue.pop()
    print(myQueue)

def display_queue():
    myQueue.sort()
    print(myQueue)

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        display_queue()
        break





