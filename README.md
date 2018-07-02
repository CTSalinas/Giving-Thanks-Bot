Giving-Thanks-Bot
=================
Grateful bot that uses PRAW (Python Reddit Api Wrapper) to give thanks to other users

When run, will read the first 100 historical comments and any new incoming comments.

Bot will read commands by other users and do the following posted command.
Current commands included are:
  !ty which give thanks to a user.
  !deletethanks which deletes a post that the bot has used.
 
 Bot also creates a text file to keep track of posts it has replied to before. Should the bot have to be rerun, it will not reply to comments it has replied to before. Furthermore, it will not reply again when the bot's previous comment has been deleted.
 
