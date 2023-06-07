# ScrapeMailMe

Simple script to scrape the specified websites and email data to the specified email address.

## DISCLAIMER:
Always make sure that the admins of the website you are scraping authorize such use of their website.

## Assumptions:
- Your server will use Python 3.10 and will allow you to configure a venv and install packages on it. PythonAnywhere is a good example of one that allows this, offering you even a free account to get started. But there might be others, no doubt.
- For the moment, you will only be able to receive the text in a tag (and/or its children), not images, video, etc.
- For now, the info about the website should be entered manually in the `websites_info` dict list. (I know, the idea is to change this in the future). 

## How to use:

As of the moment, you will need to:
1. Get the files on this repo (you could clone them or simply download them as ZIP. Take a look at the `Code` button on the top right of this page, above the code, for simple instructions and help on this).
1. Upload these files to your server (for example, PythonAnywhere in their `Files` tab -see instructions below-, etc.). 
2. Create a virtual environment (aka `venv`) and install the dependencies. See below instructions for this on PythonAnywhere, as an example.
2. Create your own `.env` file and fill it in as specified below.
3. If on PythonAnywhere, and interested on scheduling the task to be repeated with a certain frequency, go to the `Tasks` tab and schedule it. PythonAnywhere allows one scheduled task for free (for one month, then you need to renew it), if you want more than one, then you'll need to upgrade your account. Otherwise, on other platforms, you will need to check if it's possible to schedule tasks.
4. (Optional, but recommended) - For enhanced security, you will probably want to set up an 'App Password' on the Gmail account you plan on using to send the emails. See below instructions on how to do this.

### Uploading files to PythonAnywhere

Once you created your free account, within the home page (i.e. your dashboard), click on the `Files` tab.

To your left, you should have the `Directories` section, and to your right, the `Files` section.

In the `Directories` section, you should see a `New directory` button that you can click to create a new folder (after entering the folder's name to the left; in my case, I just named it `scrapemailme/`). 

Upon clicking on `New directory`, not only the folder will be created, but also you will be moved into it (you can always see your current directory -where you are- in the top left corner of the screen, under the logo).

Once inside the folder for this project, you can now upload one by one the files, using the `Upload a file` button on the `Files` section. *Upload all the files, except for the `.gitignore` one and this `README.md`*.

### Creating a venv and installing dependencies on PythonAnywhere

Once you've uploaded the files, click on the `Consoles` tab on the top right of the screen.

Now, under the `Start a new console` heading, click on the `Bash` option.

You will probably want to create a [virtual environment](https://docs.python.org/3/library/venv.html) where to install the dependencies. But first, check where you are positioned right now:
```
$ pwd
/home/<your_username_here>
``` 
Now, you can decide to either create the venv inside your project folder or outside it, in the current folder. I am going to choose the latter here, but you could use either. Do take into account *the path*, though, since later you will need to activate the venv using it (see below).
```
python3 -m venv <your_venv_name>
```
With the [`-m` flag](https://docs.python.org/3/using/cmdline.html#cmdoption-m), you specify that what follows is to be interpreted as a module and not as a command for `python3`. `venv` is the module (or lib) we will use, and then we just specify the name for our venv. That's personal choice.

Once created, we just need to activate it:
```
source venv/bin/activate
```
(Here is where the *path* is critical. Mine is like above, but yours could be different, depending on where you decided to create the venv)

Now your bash prompt should look smth like:
```
(venv) 12:34 ~ $ 
```
... effectively indicating that you have the venv active.

Now, provided you already uploaded your files in step 1, you can proceed to install the dependencies:
```
pip install -r scrapemailme/requirements.txt
```
Do notice once again, the *path* to the `requirements.txt` has to be accurate.

To make sure they were all properly installed, you can check it out with:
```
pip freeze
```
(provided the `venv` is still active)

The way this works is certain (confidential) values should be provided by you by means of an `.env` file. These files are very simple, just holding key-value pairs, usually called `environment variables`, as they vary (differ) on each environment.

So let's first create the `.env` file. Head towards the `Files` tab. Make sure to click on the project's directory (`scrapemailme/`, in my case). 

Once inside it, you'll notice that, at the top of the `Files` section, you have an empty field and a `New File` button to the right. This is where you can type the name of your new file (including the initial period, so that would be `.env`) and create it. As you create it, it will open up in the screen for you.

Once there, you can copy-paste the following and then fill it in with your values:
```
email_username=
email_password=
email_host=
email_port=
receiver_email=
```

Your file should now look, for example, like this:

```
email_username=username@gmail.com
email_password=superpassword
email_host=smtp.gmail.com
email_port=465
receiver_email=receiver@mymail.com
```

*Take into account the values for `host` and `port` have been customized for a Gmail account sending the emails. Should you use another email provider, you will need to find out their host and port values.*

### Scheduling a task in PythonAnywhere

Disclaimer: Scheduling one task daily that needs to be manually rescheduled every month is something that PythonAnywhere offers with a free account. However, should you need a higher frequency, more simultaneous scheduled tasks or should you just not want to have to schedule every month, then you will need to upgrade to a paid account.

This is actually incredibly simple. You just head towards the `Tasks` tab, and then, under `Scheduled Tasks`, specify the time of the day for the task (*in UTC time, not necessarily your local timezone!*).

Then, to the right, in the `Command` field, you will need to specify two commands: one to activate your `venv` and another one to execute the `main.py` file in your project directory.

*Again, paths are critical here. I will do this according to my paths, but do check how are your paths to both the project directory and the `venv`*

```
source venv/bin/activate; python scrapemailme/main.py
```

Optionally add a description and then click `Create` and it's ready. Your task is scheduled!

### Set up an App Password on your (sender) Gmail account

**1)** Firstly, log in to your Gmail account.

**2)** Then, click on your profile's button, at the top right of the screen and then on `Manage your Google Account`.

![Click on your profile's button, and then on `Manage your Google Account`.](readme_images/mail_config_1.jpg)

**3)** Now, on the left of your screen, click on the `Security` tab.

![Click on the `Security` tab.](readme_images/mail_config_2.jpg)

**4)** If you didn't already, enable 2-step verification for this account. Once enabled, click on the arrow to the right of the `2-Step Verification` field.

![Enable 2-step verification and click on the arrow to the right of the `2-Step Verification` field.](readme_images/mail_config_3.jpg)

**5)** Once inside the 2-Step Verification, at the bottom of the page, click on `App passwords`.

![Once inside the 2-Step Verification, at the bottom of the page, click on `App passwords`.](readme_images/mail_config_4.jpg)

**5)** Now, select the `Other (Custom name)` option and enter a name for it.

![Now, select the `Other (Custom name)` option and enter a name for it.](readme_images/mail_config_5.jpg)

**6)** After that, once you click on `Generate`, you will receive a unique code. This is the code you will need to use as a replacement to your `email_password` in the `.env` file. That is, this app will authenticate on your Gmail Account using a different password from the actual password you use.
