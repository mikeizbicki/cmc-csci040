import requests

########################################
# FIXME 0:
# Implement the following functions so that the test cases pass.
#
# NOTE:
# In your next FIXMEs, you will use these functions to do the wardial.
# All good programmers, whenever they are solving any "concrete" task like wardialing,
# will break that task into smaller functions.
# These functions can then be worked on individually,
# and we can check if they are working using the test cases.
# Then, once we are confident the small functions work,
# we put them together to accomplish our original task.
########################################

def is_server_at_hostname(hostname):
    '''
    A hostname is a generic word for either an IP address or a domain name.
    Your function should return True if `requests.get` is successfully able to connect to the input hostname.

    HINT:
    The input hostname will not contain a scheme,
    and you will have to add it.

    # Test cases for code that works with the internet are hard to write.
    # The are "nondeterministic" because the output of the test case depends not only on your code being correct,
    # but also on the webpages working correctly.
    # These test cases use google and facebook, which are almost certainly going to be online.
    # But if these webpages go down (or you're not connected to the internet),
    # then the test cases will fail even if your code is correct.
    >>> is_server_at_hostname('google.com')
    True
    >>> is_server_at_hostname('www.google.com')
    True
    >>> is_server_at_hostname('GoOgLe.CoM')
    True
    >>> is_server_at_hostname('142.250.68.110')  # IP address for google.com
    True

    >>> is_server_at_hostname('facebook.com')
    True
    >>> is_server_at_hostname('www.facebook.com')
    True
    >>> is_server_at_hostname('FACEBOOK.com')
    True

    # These test cases below use made up hostnames and so should always pass
    # (i.e. your function will always return `False`)
    # even when the internet isn't working.
    >>> is_server_at_hostname('google.commmm')
    False
    >>> is_server_at_hostname('aslkdjlaksjdlaksjdlakj')
    False
    >>> is_server_at_hostname('142.250.68.110.1.3.4.5')
    False
    >>> is_server_at_hostname('8.8.8.8')
    False

    HINT:
    Your test cases may take a LONG time to run when they can't connect to a webserver.
    This is because by default, the requests library will wait for a long time (minutes) for a server response.
    You should shorten that time to something more reasonable.
    Review the requests documentation to see how to speed up these calls and make your function faster:
    <https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts>
    
    Requests does not set a short timeout because the optimal value to use is application dependent.
    When connecting to a highly reliable service like google,
    1 second would be a sufficient timeout.
    (Anything longer than 1 second probably means there is an error in your internet connection and not an error at google.)
    But for our application, we will be connecting to servers far away in a country known for unreliable internet.
    I recommend setting a timeout of 5 seconds.
    A longer timeout would ensure that we don't miss any "slow" servers,
    but it would also make scanning take much longer.
    5 seconds is a reasonable tradeoff between these extremes.
    '''
    try:
        # if the hostname is not an IP address,
        # then we set the Host header variable to 'Host'
        if hostname.replace('.', '').isdigit():
            headers={'Host': 'Host'}
        else:
            headers={}

        requests.get(
            url='http://' + hostname,
            timeout=5,
            headers=headers,
            )
        return True
    except requests.exceptions.ConnectionError:
        return False


"""
def increment_ip(ip):
    '''
    Return the "next" IPv4 address.

    >>> increment_ip('1.2.3.4')
    '1.2.3.5'
    >>> increment_ip('1.2.3.255')
    '1.2.4.0'
    >>> increment_ip('0.0.0.0')
    '0.0.0.1'
    >>> increment_ip('0.0.0.255')
    '0.0.1.0'
    >>> increment_ip('0.0.255.255')
    '0.1.0.0'
    >>> increment_ip('0.255.255.255')
    '1.0.0.0'
    >>> increment_ip('0.255.5.255')
    '0.255.6.0'
    >>> increment_ip('255.255.255.255')
    '0.0.0.0'
    '''


def enumerate_ips(start_ip, n):
    '''
    Return a list containing the next `n` IPs beginning with `start_ip`.

    >>> list(enumerate_ips('192.168.1.0', 2))
    ['192.168.1.0', '192.168.1.1']

    >>> list(enumerate_ips('8.8.8.8', 10))
    ['8.8.8.8', '8.8.8.9', '8.8.8.10', '8.8.8.11', '8.8.8.12', '8.8.8.13', '8.8.8.14', '8.8.8.15', '8.8.8.16', '8.8.8.17']

    # This test ensures that you are properly handling "wrap around"
    #
    >>> list(enumerate_ips('192.168.0.255', 2))
    ['192.168.0.255', '192.168.1.0']

    The following tests ensure that the correct number of ips get returned.

    >>> len(list(enumerate_ips('8.8.8.8', 10)))
    10
    >>> len(list(enumerate_ips('8.8.8.8', 1000)))
    1000
    >>> len(list(enumerate_ips('8.8.8.8', 100000)))
    100000
    '''


########################################
# FIXME 1:
# Create a list of all the IP addresses assigned to the DPRK.
# Recall that the DPRK is assigned all IP addresses in the range from `175.45.176.0` to `175.45.179.255` (1024 IPs in total).
# You should use your `enumerate_ips` function that you created above.
########################################
dprk_ips = []


########################################
# FIXME 2:
# Filter the `dprk_ips` list you created above so that it contains only the IPs that have a web server.
# Use the accumulator pattern and your `is_server_at_hostname` function.
#
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
########################################
dprk_ips_with_servers = []


########################################
# Once you've completed the tasks above,
# the following code should output the list of IP addresses.
# You don't have to modify anything here.
########################################
if __name__ == '__main__':
    print('dprk_ips_with_servers=', dprk_ips_with_servers)
"""
