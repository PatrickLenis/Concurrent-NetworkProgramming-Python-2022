# Patrick Lenis
# subgr.2

def decryptFile(file_path, key, save_struct):
    alphabet = "abcdefghijklmnopqrstuvwxyz" # defined alphabet
    
    encrypted_message = ""
    decrypted_message = ""

    # read downloaded file
    with open (file_path, "r") as file:
        encrypted_message = file.readlines()

    # decrypt message
    for line in encrypted_message:
        for character in line:
            # move character by key (8 possitions)
            if character in alphabet:
                position = alphabet.find(character)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                decrypted_message = decrypted_message + new_character
            # ignore if character is not in alphabet (ex : ')
            else:
                decrypted_message = decrypted_message + character
        
    decrypted_message = decrypted_message + "\n\n" # add new line for easy reading

    save_struct.append(decrypted_message) # save to structure