# NEON-Pulse
Extract ALL mp3 links from your workspace to mass download with your own download manager, then rename to their original names you had them on your account.

Note: You need python installed to use this, this guide assumes you have it installed and working. Google a bit on how to install. (This has been tested on Chrome so follow the guide with it)

Note 2: You also need a download manager to bulk download these. I used Internet Download Manager (IDM for short), but it should work with any that supports bulk pasting of links or supports reading links from a text file.

Instructions:

1. Download the zip file containing all files from this repo by clicking on the green [<> CODE] button, selecting Download zip file, then extract them into any folder on your pc and name it anything you want.
  
2. Go into your suno workspace and select the workspace you want the songs from, then press F12 to open the Chrome console.
   
3. Click on the network tab on the console, then type V3 into the filter bar on the top part of the console.
   
4. Press F5 to refresh the page, you should see the network tab filling in with the network captures, including the v3 data we need. Make sure that it shows an {i} icon, this way you know it's fetching the song info data.

5. Begin scrolling down until you get to the last song you want to get the links from, or go all the way down so it gets all the links. You'll see more and more V3 fetch requests appear as you go on.

6. When you're done scrolling go to the console and look on the top part for an arrow pointing down (beside a wifi-looking icon), and click on it to export the data.

7. On the save as dialog that appears, save the file to the new folder you extracted the files on and rename it suno.har on the filename part.

8. Now go to the folder where all the files are extracted and double-click the extract har.py, it will extract the links and output a suno_links.txt file.

9. Copy/paste them into your download manager of choice and begin downloading them, make sure they are downloaded to the same folder. After you're done, move all songs into the "suno songs" folder for renaming.

10. Double click on the rename.py script and it will fetch the names from the .har file and rename them accordingly. If 2 or more songs are named the same it will add a number to differentiate them.

11. Enjoy your newly mass-downloaded songs!
