[SOLVED] Using a keyboard shortcut to run a shell script !! gnome-terminal -e "bash /home/01553360702/ler.sh"

#  Using a keyboard shortcut to run a shell script

> Ubuntu 9.04

> I have a bash shell script located at "/home/devin/.Scripts/script"

> I want to attach it to a hot key, I go to "System > Preferences > Keyboard Shortcuts", click "Add", Type in a name, and under "Command" I put in "/home/devin/.Scripts/script", and then assign a key to it.

> When I press that key, nothing happens...

> Any ideas?

> Thanks in advance
> Devin

* * *

## Re: Using a keyboard shortcut to run a shell script

> Does your script have executable premissions? Other than that, might be a key bindign conflict, or something...

> BM

* * *

## Re: Using a keyboard shortcut to run a shell script

![Quote](../00 EVERNOTE_EM_USO/2cac455cbcc23e49c51beaede3ebca9d.png)>  Originally Posted by **> blur xc**

> Does your script have executable premissions? Other than that, might be a key bindign conflict, or something...

> BM
> Thanks for the reply.

> I believe it has executable permissions: I can run it from within the terminal with the command "/home/devin/.Scripts/script" and it works as expected.

> It doesn't matter what key I bind it to, it still doesn't work. I tested the each of the keys that I tried by assigning it to "Open Terminal", to make sure that they were being received/processed correctly, and they work there, but when I assign them to run the script, they don't do anything.

* * *

## Re: Using a keyboard shortcut to run a shell script

> What is it supposed to do? If you want a terminal window to appear, your command should be:

> Code:
> gnome-terminal -e "bash /home/devin/.Scripts/script"
>  Otherwise it'll be executed silently.

* * *

## Re: Using a keyboard shortcut to run a shell script

![Quote](../00 EVERNOTE_EM_USO/2cac455cbcc23e49c51beaede3ebca9d.png)>  Originally Posted by **> prodigy_**

> What is it supposed to do? If you want a terminal window to appear, your command should be:

> Code:
> gnome-terminal -e "bash /home/devin/.Scripts/script"
>  Otherwise it'll be executed silently.

> I don't need the terminal to (stay) open (the script is to toggle from internal to external display on my laptop). But apparently using

> Code:
> bash /home/devin/.Scripts/script
> instead of
> Code:
> /home/devin/.Scripts/script
> in the "Command:" field works correctly.

> Thanks for the help!

> Devin

* * *

## Re: Using a keyboard shortcut to run a shell script

> I know you've figured this out but the script may not have the following located at the top:

> Code:
> #!/bin/bash

> Which is probably why you have to type 'bash script_name' instead of just 'script_name'. It works when you're already in a terminal because you're in a bash environment which interprets the commands as such.

* * *

## Re: Using a keyboard shortcut to run a shell script

![Quote](../00 EVERNOTE_EM_USO/2cac455cbcc23e49c51beaede3ebca9d.png)>  Originally Posted by **> vttay03**

> I know you've figured this out but the script may not have the following located at the top:

> Code:
> #!/bin/bash

> Which is probably why you have to type 'bash script_name' instead of just 'script_name'. It works when you're already in a terminal because you're in a bash environment which interprets the commands as such.

> My script already contains that. The 'bash' command still seems to be required even with that.

* * *

## Re: Using a keyboard shortcut to run a shell script

![Quote](../00 EVERNOTE_EM_USO/2cac455cbcc23e49c51beaede3ebca9d.png)>  Originally Posted by **> NeoDevin**

> My script already contains that. The 'bash' command still seems to be required even with that.

> did you make your script executable?
> Code:
> chmod u+x script
> then it could be run by
> Code:
> ./script
> if the script is in your working directory, or
> Code:
> /path/to/script
> if it isn't.

> BM

* * *