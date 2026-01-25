with open("Playlist.m3u", "r") as playlist:
    original_list = playlist.read().splitlines() #reads the document
unique_list = list(set(original_list)) #removes duplicates
sorted_list = sorted(unique_list) #sorts the list
with open("NewPlaylist.m3u", "w") as playlist:
    playlist.write("\n".join(sorted_list) + "\n")