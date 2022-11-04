import requests

# FIXME 0:
# Copy/paste the implementation of the `is_server_at_ip` function
# from the lab instructions below.
def is_server_at_ip(ip):
    '''
    returns `True` if a server exists at the input IP address;
    otherwise returns `False`
    '''
    return True


# FIXME 1:
# Create a list of all the IP addresses assigned to the DPRK.
# Recall that the DPRK is assigned all IP addresses in the range from `175.45.176.0` to `175.45.179.255` (1024 IPs in total).
# These IP addresses should be represented as python strings.
# It is possible to do this using either a 1-line list comprehension or a multi-line for loop.
dprk_ips = ['175.45.176.0', '175.45.176.1', '175.45.176.2', 'etc...']


# FIXME 2:
# Create a list of all IP addresses in dprk_ips that have a server at them.
# Print this list of IPs to the screen.

# HINT:
# Use the accumulator pattern.

# HINT:
# Your for loop will take a LONG time to run.
# There are 1024 IPs that you must scan,
# and you're waiting up to 5 seconds for each.
# That means you're code will take up to 1024*5/60 = 85 minutes to run.
# You should output some debugging messages to let you know which ip address you are currently scanning.
# Also, if you haven't watched the WarGames movie yet,
# I recommend watching it while you're code is running :)
#
# In "real" war dialing code,
# all of these connections are done in parallel,
# and so the scan of all 1024 IPs can be completed in just seconds.
# An ordinary laptop and internet connection can scan the entire internet (4.2 billion IPs) in under an hour.
# Parallel programming is quite hard, however,
# so we're just doing the slow and sequential version in this lab.
# If you go on to take the CS46 class (data structures) next semester,
# you'll learn how to write this parallel code.

# HINT:
# Depending on your computer's configurations,
# there are many other exceptions that might possibly be thrown besides `ConnectTimeout`,
# and you'll have to get creative about debugging these problems.
