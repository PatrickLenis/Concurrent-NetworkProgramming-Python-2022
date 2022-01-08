# Patrick Lenis
# subgr.2

import urllib.request

# download file from url
def downloadFile(url, save_path):
    url_data = urllib.request.urlopen(url) # get url data

    # write downloaded data to file
    with open (save_path, "w") as file:
        for line in url_data:
            file.write(line.decode('utf-8'))