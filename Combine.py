# Patrick Lenis
# subgr.2

def combineMessages(save_struct, save_path):
    final_message = ""
    # reads saved messages from data structure
    for message in save_struct: 
        final_message = final_message + message # add messages to final outpur
    
    # write final message to output file
    with open (save_path, "w") as file: 
        for line in final_message:
            file.write(line)