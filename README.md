`sudo apt-get install git`
`git clone https://github.com/JesseAldridge/logrot`

`python logrot/example_process.py 2>&1 | python logrot/logrot.py &`

So you want to stick a script on a remote machine and leave it running forever?  
Cool.  But what happens if it crashes?  How will you know what went wrong?  
Maybe you should just redirect stderr and stdout to a file?  
Ok, cool.  But wait, this log file is just going to keep growing forever and will eventually fill
up the entire hard-drive.  
This is where logrot comes in.  Just pipe your output to it as shown above and your output will
be written to `~/logrot_out.txt`.  Only the most recent 1 MB of output data will be retained.
