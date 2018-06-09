import subprocess
print "The files in the specified directory are as follows. "
subprocess.call(['ls','--full-time','-tr','/home/divya/Documents/scripts/dummy-data/'])
confirm=raw_input("Specify the year from which the files should be deleted... ")
#print(confirm);
cmd = "find /home/divya/Documents/scripts/dummy-data/ -type f -ls | grep '"
cmd1= "' | awk '{ print $11 }'| xargs rm"
ps = subprocess.Popen(cmd+confirm+cmd1,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print output
#subprocess.call(['ls','-ltr','/home/divya'])
