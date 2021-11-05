# Lab: Password Cracking

Recall that in computer science,
"hacking" is a good thing.
it is the process of building cool stuff.
"Cracking" is the bad thing that muggles usually mean when they talk about hacking.
Cracking is the process of breaking stuff.

In this lab, you'll get your first taste of cracking.
You'll learn how to crack the passwords of encrypted zip files using python,
and see that the basic tools for cracking are the same as the basic tools for hacking.

## Part I: Background

**Working with zip files in python**

This lab contains an encrypted zip file called `guido_secrets.zip`.
In this first part of the lab,
you'll learn how to open up and decrypt this file in python.

Python can open password protected zip files using the built-in `zipfile` module.
Download `guido_secrets.zip`, and try running the following code:
```
from zipfile import ZipFile
with ZipFile('guido_secrets.zip') as zf:
    password = b'BFDL'
    zf.extractall(pwd=password)
```
Notice:
1. After running this program,
    your working directory should contain a folder named `guido_secrets` with a file `secrets.txt` which contains a poem about the "zen of python."
    This is a particularly famous poem that every pythonista should read through at least once.

1. The `password` variable is a `bytes` object and not a `str`.
   Zip file passwords are not traditional string passwords that you might be familiar with,
   instead they are a sequence of bytes.
   It's traditional that the sequence of bytes happens to correspond to an English language ASCII sequence,
   but it's not required.
   In particular, it is impossible to have zip file password with non-latin characters.

   Try changing the `password` variable to `'BFDL'` instead of `b'BFDL'` and you should get a `TypeError`.
   (And hopefully it makes sense why.)
   
   Recall that if we have a variable with type `str`, we can convert it into a `bytes` object using the `.encode` function:
   ```
   password_str = 'BFDL'
   password = password_str.encode('ascii')
   ```
   is equivalent to
   ```
   password = b'BFDL'
   ```

1. Now try changing the byte sequence to anything other than `BFDL`.
   You should get a `RuntimeError` indicating that the you supplied the incorrect password.
   No files will be generated in your working directory.
   (Depending on your computer's settings, you may get a different exception thrown.)

**Zip bombs**

Zip files are particularly dangerous objects from a cracking perspective due to something called a "zip bomb".
Antivirus software often opens up zip files and looks inside for virus software.
But just the act of opening up a zip bomb can break a computer:
opening the zip file requires decompressing the file,
which can use up all the space on your hard drive.

For example:

1. The file [42.zip](https://unforgettable.dk/) is only 42KB large,
   so it's a quick download.
   But if you unzip it, it takes up 4.5PB of disk space on your computer.
   PB stands for petabytes, and 1 petabyte is 1000 terabytes (or 1,000,000 gigabytes).
   You probably don't have that much disk space,
   so don't try to unzip it :)

   <img src=zipbomb.jpg width=400px>

1. Even worse is the file [quine.zip](https://wgreenberg.github.io/quine.zip/).
   This file actually contains itself inside of it!
   Antivirus software will open up zip files inside of zip files,
   so antivirus software opening `quine.zip` will get stuck in an infinite loop of opening this file forever.

   This one is safe for you to open, however, and I recommend you do so.
   You can see that the file contains another file exactly like itself,
   and try opening it a couple of times.

   <img src=zipbomb-dawg.jpg width=400px>

Python has no built-in protection against zip bombs,
so you should never open an untrusted zip file from python
(since it might be a bomb).

I promise that the files I'm giving you aren't zip bombs :)
   
## Part II: Cracking

**The Scenario:**

For this lab, you're going to pretend that it's the year 2015 and you are an analyst at [GRU](https://en.wikipedia.org/wiki/GRU),
the infamous Russian spy agency.
One of your agents has risked their life to bring you the file `whitehouse_secrets.zip`.
This file was stolen from an IT worker at the white house,
and contains secret details of the upcoming US presidential election.
Your job is to access these details.
(Your bosses want to use them as part of an operation to manipulate the 2016 election.)

Unfortunately, the file is encrypted and you don't know the password.
Fortunately, you have some leads that will help you guess the password:

1. In July 2015, the website [Ashley-Madison (ashleymadison.com) had a major data leak](https://en.wikipedia.org/wiki/Ashley_Madison_data_breach).
   Ashley-Madison is a dating website for married people to find extra-marital lovers without their spouse's knowledge,
   and a group of hackers called "The Impact Team" acquired and leak this data in order to damage what they considered to be an immoral business.

1. You know that the IT worker who created the `whitehouse_secrets.zip` is an active user of Ashley-Madison.
   This IT worker, like [most people](https://www.infosecurity-magazine.com/blogs/your-employees-reusing-passwords/),
   reuses the same password for everything they do.
   So one of the leaked passwords from Ashley-Madison will decrypt the `whitehouse_secrets.zip` file.
   We just have to figure out which one.

**Historical Aside:**

This scenario is not made up.
The military news website defenseone.com [reports that](https://www.defenseone.com/threats/2015/08/ashley-madison-hack-opm-government-military/119279/) 45 White House staffers had accounts at Ashley-Madison and more than 10000 military personnel had accounts.
The [Associated Press](https://apnews.com/article/1c34b10bff3744f386706480333ef9f5) confirms that a White House IT staffer was among the users.

Because of the national security implication of adultery,
adultery will [typically disqualify someone](https://news.clearancejobs.com/2013/01/15/adultery-and-security-clearances/) from getting a security clearance in the United States.
And even though adultery is not against the law for civilians,
adultery is a [felony offense](https://militarybenefits.info/ucmj-adultery/) for anyone in the military.

**Your Tasks:**

1. Download `whitehouse_secrets.zip`.

1. [The SecLists github repo](https://github.com/danielmiessler/SecLists/) contains lots of security related datasets,
   including the passwords of the Ashley-Madison leak.
    These passwords are located at `Passwords/Leaked-Databases/Ashley-Madison.txt`.
    Download this file.

1. Create a program `password_cracker.py` that finds the password of the zip file.
   Your program should:

    1. Open then file `Ashley-Madison.txt`,
       and create a list called `passwords` that contains all of the passwords.

    1. For each password in `passwords`,
       try opening `whitehouse_secrets.zip` with that password.
       If it successfully opens, then print out the password.

       **HINT:**
       You should use a `try`/`except` clause to determine whether the zip file opened,
       and perform different operations based on whether the file opened or not.

       Once the file is successfully decrypted,
       you should have a new file `whitehouse_secrets/secrets.txt` that contains President Obama's secrets.

1. (Optional, but recommended)
   Change your passwords so that you're not using the same password for everything.
   I personally like to memorize all my passwords,
   but other people prefer using password managers to store the passwords.
   Firefox has an [excellent one built-in](https://www.mozilla.org/en-US/firefox/lockwise/).

   According to Snowden, the NSA is capable of guessing up to [1 trillion passwords per second](https://news.ycombinator.com/item?id=8448894),
   and [jack the ripper](https://www.openwall.com/john/) is a famous open source tool that's capable of guessing millions of passwords per second on an ordinary computer.
   (Your python program is probably capable of guessing between 10,000-100,000 passwords per second, which is a lot slower than jack the ripper.)
   So using strong passwords that are hard to guess is important.
   The [XKCD comic has a great technique](https://www.explainxkcd.com/wiki/index.php/936:_Password_Strength) for generating easy-to-remember passwords that not even the NSA can crack.

**Submission:**

Upload to sakai:
1. the password to `whitehouse_secrets.zip`
1. your `password_cracker.py` file
1. the contents of `whitehouse_secrets/secrets.txt`

