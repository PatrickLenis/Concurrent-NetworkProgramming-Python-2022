# Patrick Lenis
# subgr.2

import threading

from Download import downloadFile
from Decrypt import decryptFile
from Combine import combineMessages

# console coloers
BLUE = "\033[0;36m"
DEFAULT = "\033[0m"

message_struct = [] # data structure to store decrypted messages

# prints result (saved in s_final)
def printResult(file_path): 
    print(BLUE + "\n--------------------- Final Message ---------------------\n" + DEFAULT)
    
    result = []

    with open (file_path, "r") as file: # read resulted file
        result = file.readlines()
    
    for line in result: # print lines in file
        print(line)

    print(BLUE + "\n---------------------------------------------------------\n" + DEFAULT)

# ----------- thread functions -----------

def downloadThread(): 
    # defined in Download.py
    downloadFile("https://advancedpython.000webhostapp.com/s1.txt", "./Files/s1_enc.txt")
    downloadFile("https://advancedpython.000webhostapp.com/s2.txt", "./Files/s2_enc.txt")
    downloadFile("https://advancedpython.000webhostapp.com/s3.txt", "./Files/s3_enc.txt")

def decryptThread(): 
    # defined in Decrypt.py
    decryptFile("./Files/s1_enc.txt", 8, message_struct)
    decryptFile("./Files/s2_enc.txt", 8, message_struct)
    decryptFile("./Files/s3_enc.txt", 8, message_struct)

def combinerThread(): 
    # defined in Combine.py
    combineMessages(message_struct, "./Files/s_final.txt")

# --------- end thread functions ---------

if __name__ == "__main__":
    
    # download thread
    downloader_thread = threading.Thread(target=downloadThread)
    downloader_thread.start()
    downloader_thread.join()

    # decrypt thread
    decryption_thread = threading.Thread(target=decryptThread)
    decryption_thread.start()
    decryption_thread.join()

    # combine thread
    combiner_thread = threading.Thread(target=combinerThread)
    combiner_thread.start()
    combiner_thread.join()

    printResult("./Files/s_final.txt") # print resulted text