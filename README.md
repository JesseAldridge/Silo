`python example_process.py 2>&1 | python silo.py &`

So you want to stick a script on a remote machine and leave it running forever?  
Cool.  But what happens if it crashes?  How will you know what went wrong?  
Maybe you should just redirect stderr and stdout to a file?  
Ok, cool.  But wait, this log file is just going to keep growing forever and will eventually fill
up the entire hard-drive.  
This is where silo comes in.  Just pipe your output to it as shown above and it will limit
the output to the last 1MB of data.
