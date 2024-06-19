import os
test=open("C:\\Users\\Hznrb\\OneDrive\\Documents\\New folder\\Jonathon.txt")
test.close()

if os.path.exists("C:\\Users\\Hznrb\\OneDrive\\Documents\\New folder\\Jonathon.txt"):
    print("ur file got deleted")
    os.remove("C:\\Users\\Hznrb\\OneDrive\\Documents\\New folder\\Jonathon.txt")
else:
    print("file no existe")