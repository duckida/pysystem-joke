from time import sleep

while True:
    cmd = input("$")
    if cmd == "help":
        print("Commands are ls, info, and help")
    elif cmd == "ls":
        print("Joke.txt beep.png Documents")
    elif cmd == "info":
        print("PyTERM 1.0 on macOS 11.1")

    else:
        print("Erasing disk C:")
        sleep(1)
        print("Complete")
        break
