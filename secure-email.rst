.. _secure-email: 

============
Secure Email
============

Our recommendations in this document are based on our own security policies, as well as information from the EFF's `SSD (Security Self Defense) project <https://ssd.eff.org/>`_.

Outline:

1.  Get a separate e-mail for activist work
2.  Use encryption
3.  Use POP - don't store your email in the cloud!

Get a separate e-mail account
-----------------------------

You may be using email provided by your ISP (AOL, Hotmail, MSN, etc.) an organization you work for (mark.felt@fbi.gov), or maybe you use a free webmail service like GMail or Yahoo Mail. Although it is fine to use such an e-mail account for day-to-day use, *they are not safe* for use by whistleblowers or activists concerned about government surveillance. 

Why?
++++

There are several reasons to get a new e-mail account.

1.  Your current e-mail is probably closely associated with your real name and other personally identifying information. Think about how often you use it to sign up for online services, on mailing lists whose archives may be published, or on social networking websites like Facebook.

    Try Google searching your own email address - you might be surprised how easy it is to correlate your online activity. It's certainly the first thing an attacker would do.

2.  Most e-mail providers

    a)  save your e-mail on their servers.
    b)  log your access to your account, including the recipients and dates of e-mails sent and received

    Providers keep copies of your e-mail for your convenience. This is what enables you to use GMail in your web browser to access your email on any computer, from anywhere in the world. They log access for numerous reasons, including their own troubleshooting needs. 

    All of this convenience can become a problem for activists. In the US, communications providers, including e-mail providers, can be legally ordered to turn over your personal information with a subpoena or a court order. It is actually simpler legally to obtain your information from a third party, and this can be done without probable cause or any notice to you. See the section on `Information Stored by Third Parties <https://ssd.eff.org/3rdparties>`_ from the SSD project for details.

3.  Some useful security guidelines are:

    a) principle of adequate protection. 
    b) separation of duties

    By separating your personal life from your work as an activist, you limit the potential damage to yourself and your work should either email account be compromised.


.. warning::
    There is a trade-off between security and convenience. Unless you take additional complicated and risky steps, secure email can only be accessed on your physical computer, and you will have the only copies of that email, making it your responsibility to back it up. You lose the convenience of services like GMail.

How?
++++

The best choice is getting a new email account from a service that is designed with activists in mind.

In the US, we've had great results using the email provided by `Riseup <https://riseup.net/>`_. They're a Seattle-based collective providing digital resources for activists. Their services are free to use, but consider donating if you find them useful.

Email providers like Riseup take a `number of steps <https://help.riseup.net/en/email#what-is-special-about-riseup-net-email>`_ to protect your privacy. If you're interested in exploring alternatives, here's a checklist of things to look for in an email provider:

-   Encrypts email traffic with StartTLS.
-   Encrypts your stored email on their servers.
-   If they offer a webmail client that you can access in your browser, secures the connection over HTTPS.
-   Doesn't use identifying e-mail headers that disclose your IP address to recipients. Examples of these headers are: **X-Originating-IP**, **Received**.
-   Performs minimal or no logging, or avoids logging personally identifying information like your IP address.

Another popular secure-email provider is `Hushmail <http://www.hushmail.com/>`_. We have not used them but they are often recommended. A very important detail about Hushmail is that you should use their `client-side Java Encryption Engine <https://help.hushmail.com/entries/245155-using-java-with-hushmail>`_. Otherwise, Hushmail will decrypt your private key *on the server*, leading to a brief window of time when they can read the contents of your email. In the past, `they have been legally obligated <http://www.wired.com/threatlevel/2007/11/encrypted-e-mai/>`_ to disclose client's personal information to federal prosecution, including the contents of their email. If you're using Hushmail, **use the Java configuration**.

In general, we recommend using a communications provider that serves the public, rather than running your own email server or using one someone you know may have set up. Ultimately, using a public communications provider gives you `stronger legal protections <https://ssd.eff.org/3rdparties/govt/stronger-protection>`_.

..  note::
    Most alternative e-mail providers don't have the same resources as big companies like Google, Yahoo, or Microsoft. As a result, their storage limits are much lower. Riseup's is around 20MB, for example, compared to Google's approximately 7GB. Although you can fit a lot of plain text email into 20MB, you should be careful with attachments, especially larges ones like images. Accessing your email through POP, as described in the next section, also means this will be less of an issue.

At the bare minimum, get a separate email from a free public webmail provider like GMail, and try not to share any personally identifying information during the registration process. If you encrypt your email and use POP to access it, you will minimize the amount of data available to government and law enforcement.

..  warning::
    We're recommending GMail here only because they've taken some good steps to protect their users, including
    
    1.  `defaulting to use HTTPS <http://gmailblog.blogspot.com/2010/01/default-https-access-for-gmail.html>`_, and
    2.  `using STARTTLS for email transfer <http://securitynirvana.blogspot.com/2011/10/more-starttls-support.html>`_.
        
    As you can `see here <http://www.google.com/transparencyreport/governmentrequests/userdata/>`_, however, Google regularly complies with requests for user data from governments and law enforcement. They should be used **if and only if** all other options fail.

Encrypt your email
------------------

This tutorial is written for users of Thunderbird with the Enigmail plugin. It was developed on a Mac, but since Thunderbird and Enigmail are cross-platform, these steps should work with minimal modification on any operating system.

..  note::
    For your security, it's important to keep Thunderbird and plugins like Enigmail up-to-date. Thunderbird is configured to automatically download and install updates to itself and its add-ons. You can check these settings by opening the Preferences, going to the Advanced pane and then the Update section. If you open Thunderbird and it informs you that updates are available, **do not ignore it**. Promptly install the updates and restart Thunderbird so they take effect.

Step 1: Install Thunderbird and add your email account
++++++++++++++++++++++++++++++++++++++++++++++++++++++

First, `download Thunderbird <http://www.mozilla.org/en-US/thunderbird/>`_ and follow the subsequent installation instructions.

Once Thunderbird is installed, open it. It will prompt you to add a New Mail Account. You should only have to type your new email address and password - Thunderbird will figure out the rest. 
We'll assume that the default configuration is fine for now, coming back to the idea of using POP for additional security later.

..  warning::
    Don't put your real name in the **Your Name** field. It will be included with the mail headers and thus will not be encrypted.

If for some reason Thunderbird does not prompt you to add an account, or you already had Thunderbird installed, you can always add an email account through File > New > Mail Account...

Step 2: Install Enigmail
++++++++++++++++++++++++

Once you've added your email account to Thunderbird, you need to install Enigmail, a plugin that makes encrypting email easier and more accessible. The Enigmail website is a little confusing, but we'll guide you through the process.

First, you need to install GNU Privacy Guard (GPG). This is an open-source implementation of the OpenPGP encryption standard. Various groups exist to compile and maintain these tools on specific platforms. To get GPG, visit the site for your platform:

1.  Mac OS X: `GPGTools <http://www.gpgtools.org/>`_
2.  Windows: `GPG4WiN <http://gpg4win.org/>`_
3.  Linux: We recommend using your distro's package manager to install gpg.

    For example, on Debian/Ubuntu: ``$ sudo apt-get install gnupg``

Download and run the installer to get GPG on your system.

Once GPG is installed, you can install the Enigmail plugin for Thunderbird. To download, visit the `Enigmail Project page <http://enigmail.mozdev.org/>`_. A link to download for your operating system should be visible in the column on the left under "Download." Click the link to download the plugin file, which should end with ``.xpi``.

..  note::
    If you're using Firefox, the browser may get confused and think you're trying to install a Firefox plugin. If this happens, **right-click** the Download link to Save Link as...

Open Thunderbird. Go to Tools > Add-ons. Click the gear icon at the top of the Add-ons Manager and select "Install Add-on From File..." Navigate to the saved ``.xpi`` file and choose it. A window will pop open, verifying that you want to Install the plugin. Confirm your decision.

Once the plugin is installed, restart Thunderbird and you will be ready to move on to the next step.

Step 3: Create a keypair for this email account
+++++++++++++++++++++++++++++++++++++++++++++++

Go to OpenPGP > Key Management. This shows you a list of all the keys currently in your keyring (saved on your computer). Notice that the menubar has changed.

To add a new keypair, select Generate > New Key Pair. In the top menu, select the email account you wish to generate a keypair for. Choose a strong passphrase and type it in twice. Remember that GPG key passphrases can include spaces, and can be up to 60 characters (?) in length. Leave the defaults where they are, and click "Generate key". Now you will have to wait for the system to generate your keypair. As the note states, this may take several minutes. You can speed up the process by actively using your computer during the key generation process. This replenishes the entropy used by your computer to generate random numbers.

Once the key is generated, TODO: finish guide

Limitations of encrypted communications
~~~~~~~

Relational communication: can see how often/when Alice communicates with Bob, but not what they are saying. Also note that **the subject line of email is not encrypted**.

Should verify keys to avoid trust attacks.

Use POP
-------

enabling POP in gmail: https://mail.google.com/support/bin/answer.py?answer=13273

