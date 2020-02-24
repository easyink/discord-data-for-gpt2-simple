# discord-data-for-gpt2-simple
This is a prep script that is used in conjunction with the gpt2-simple ai generator.  This needs your requested discord data as well.

After you get the requested data, place the script inside of the main folder, outside of the messages folder.
All of your messages are in that folder.

This script basically goes through every csv file and compiles it into one txt file to feed into the gpt2-simple thingy.

It uses regex to filter out emotes, and links. It also removes the remaining whitespace it leaves behind.

make sure to set the path for some of the variables.

It's a dirty script but I literally don't know how to code better, and it seemingly works.

It ultimately doesn't really generate anything interesting with the gpt2-simple since most messages are in response to other things, so it only generates responses to non existent people.
