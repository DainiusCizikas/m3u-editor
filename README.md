# m3u-editor



### Introduction:



##### Purpose of the project:

The purpose of this project is to create an application that will provide a solution to a software problem and a lack of a specific feature that the Shanling M0s audio player has.

Additionally, by doing this project I will attempt to learn Python and code the "pythonic" way.



##### The problem:

The Shanling M0s is a small digital audio player (henceforth DAP) that provides convenience for people who want to disconnect from music streaming services or listen to music without the distractions of a phone.



I encountered two problems that I want to fix:

1. Lack of a specific feature - You can create playlists in the DAP that will have the music files that you choose, however, there is no option for alphabetically sorting the playlist for easier browsing. 
2. A bug - The DAP has a feature that will not let you add the same song twice, however, this feature does not work half of the time.



##### The plan:

* Export the playlists as .m3u files.
* Using the m3u-editor sort the playlists and remove duplicates.
* Import the playlists back to the DAP.
* Make gradual improvements to the program.



### Versions:



##### Current version:

Proof-of-Concept (PoC)

The PoC version takes an m3u file that is not sorted and has duplicates in the root directory of the project and creates a new m3u file that is sorted and has no duplicates.



##### Previous versions:

N/A



##### Future versions:

* Will handle potential errors
* Will check the file type before reading the file
* Will use system arguments to get the original file
* Will create a new file and delete the old one
* Will be more uesr-friendly
