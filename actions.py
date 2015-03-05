import subprocess
p = subprocess.Popen("/usr/local/bin/12vmon", stdout=subprocess.PIPE, shell=True)

(output, err) = p.communicate()

p_status = p.wait()

print "Command output : ", output
print "Command exit status/return code : ", p_status
