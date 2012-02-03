.. _secure-email: 

============
Secure Email
============

Do you want to communicate with us securely? We encourage you to follow these best practices for communicating securely by email.

1.  Use a separate, dedicated e-mail account for activist work
2.  Encrypt your email
3.  Don't store email on your email provider's servers 

If you've never encrypted your email before, and have no idea what GPG is, you should read the following primer first:

Public Key Cryptography Basics
------------------------

In order to encrypt your email, you need to generate a GPG keypair. There are detailed instructions for how to do this below, but here we want to explain exactly what this means.

As the name "keypair" implies, there are actually two keys that are related to each other: your public key and your private key. Together, they perform encryption using clever mathematics so that a message encrypted with one key requires the other, complementary key for decryption.

The public key is meant to be, well, public: you can share it with your friends, email it to people, or upload it to a public keyserver. If someone wants to send you an encrypted message, they will use your public key to encrypt the message. Then only your private key will be able to decrypt it. Unlike the public key, your private key should be carefully protected and never shared with anyone.

Taken together, this encryption system is called *public-key cryptography*, or *asymmetric cryptography*.

Limitations of encrypted communications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Imagine that you have access to the email inbox of a tech-savvy individual who has used GPG to encrypt all of their email. You can't read any of their messages, but what else can you learn?

Encrypted communications do not protect against the analysis of relational communication. Looking at the hypothetical inbox, you can see how often/when Alice communicates with Bob, but not what they are saying. If Alice and Bob's true identities are known, this can still be very useful information.

Also, it is important to note that only the body of an email message is encrypted. The headers, *which include the subject line*, are not. You should avoid revealing information about the contents of an encrypted email in its subject line. Also, if your email provider uses headers that record your IP address, that will be accessible as well. Sensible email providers, like Riseup, avoid putting such identifying information in headers. 

A weak point in the design of public-key cryptography is key verification. Let's say you lookup your friend's public key on their website, or download it from a public keyserver. How do you know it's *really* their key? How can you trust it? To do so, you need to verify something about the key that only it's owner would know, with the owner themselves. You should do this in person, or over the phone if you recognize their voice, to make sure they are indeed the person you intend to communicate with. We will discuss how to do this in practice later.

Get a separate e-mail account
-----------------------------

The best choice is getting a new email account from a service that is designed with activists in mind.

In the US, we've had great results using the email provided by `Riseup <https://riseup.net/>`_. They're a Seattle-based collective providing digital resources for activists. Their services are free to use, but consider donating if you find them useful.

Email providers like Riseup take a `number of steps <https://help.riseup.net/en/email#what-is-special-about-riseup-net-email>`_ to protect your privacy. If you're interested in exploring alternatives, here's a checklist of things to look for in an email provider:

*   Encrypts email traffic with StartTLS.
*   Encrypts your stored email on their servers.
*   If they offer a webmail client that you can access in your browser, secures the connection over HTTPS.
*   Doesn't use identifying e-mail headers that disclose your IP address to recipients. Examples of these headers are: X-Originating-IP and Received.
*   Performs minimal or no logging; avoids logging personally identifying information like your IP address.

Once you've set up a new email account, you will need the email address and password for the next step.

Encrypt your email
------------------

This tutorial is written for users of Thunderbird with the Enigmail plugin. It was developed on a Mac, but since Thunderbird and Enigmail are cross-platform, these steps should work with minimal modification on any operating system.

..  note::
    For your security, it's important to keep Thunderbird and plugins like Enigmail up-to-date. Thunderbird is configured to automatically download and install updates to itself and its add-ons. You can check these settings by opening the Preferences, going to the Advanced pane and then the Update section. If you open Thunderbird and it informs you that updates are available, **do not ignore it**. Promptly install the updates and restart Thunderbird so they take effect.

Step 1: Install Thunderbird and add your email account
++++++++++++++++++++++++++++++++++++++++++++++++++++++

First, `download Thunderbird <http://www.mozilla.org/en-US/thunderbird/>`_ and follow the installation instructions.

Once Thunderbird is installed, open it. It will prompt you to add a New Mail Account. Start by typing your new email address and password.

If you wish to remain anonymous, use a pseudonym in the "Your Name" file - this name will be included in email headers, which means it will be visible to the people you email and also will never be encrypted.

Click "Continue" and Thunderbird will attempt to fetch configuration information from the server. Assuming this works, you will be given a choice to use IMAP or POP3. These are two different protocols for accessing your email on the server. IMAP leaves your email on the server, which means that you can access your email from multiple computers or through a webmail interface (like Gmail). POP copies mail to your computer and deletes the copies stored on the server. We highly encourage you to use POP for activist emails.- just click the associated radio button.

..  image:: images/thunderbird_new_mail_account.png
    :align: center

If for some reason Thunderbird does not prompt you to add an account, or you already had Thunderbird installed, you can always add an email account through File > New > Mail Account...

Step 2: Install Enigmail
++++++++++++++++++++++++

Once you've added your email account to Thunderbird, you need to install Enigmail, a plugin that makes encrypting email easier. The Enigmail website is a little confusing, but we'll guide you through the process.

First, you need to install GNU Privacy Guard (GPG). This is an open-source implementation of the OpenPGP encryption standard. Various groups exist to compile and maintain these tools on specific platforms. To get GPG, visit the site for your platform:

1.  Mac OS X: `GPGTools <http://www.gpgtools.org/>`_
2.  Windows: `GPG4WiN <http://gpg4win.org/>`_
3.  Linux: We recommend using your distro's package manager to install gpg.

    For example, on Debian/Ubuntu: ``$ sudo apt-get install gnupg``

Download and run the installer to get GPG on your system.

Once GPG is installed, you can install the Enigmail plugin for Thunderbird. To download, visit the `Enigmail Project page <http://enigmail.mozdev.org/>`_. A link to download for your operating system should be visible in the column on the left under "Download." Click the link to download the plugin file, which should end with ``.xpi``.

..  note::
    If you're using Firefox, the browser may get confused and think you're trying to install a Firefox plugin. If this happens, right-click the Download link and Save Link as...

Open Thunderbird. Go to Tools > Add-ons. Click the gear icon at the top of the Add-ons Manager and select "Install Add-on From File..." Navigate to the saved ``.xpi`` file and select it. A window will pop open, verifying that you want to Install the plugin. Confirm your decision.

Once the plugin is installed, restart Thunderbird. You are now ready to encrypt your email and read encrypted mail sent to you from others.

Step 3: Create a GPG Key Pair for this email account
+++++++++++++++++++++++++++++++++++++++++++++++

In the menubar, go to OpenPGP > Key Management. This shows you a list of all the keys currently in your keyring (saved on your computer). Notice that the menubar has changed.

To add a new keypair, select Generate > New Key Pair. In the top menu, select the email account you wish to generate a keypair for.

Choose a strong passphrase and type it in twice. Remember that GPG key passphrases can include spaces, and can be up to 60 characters in length. Note that if you forget/lose this password, it will be impossible for you to access your encrypted emails.

Leave the defaults where they are, and click "Generate key". Now you will have to wait for the system to generate your keypair. As the note states, this may take several minutes. You can speed up the process by actively using your computer during the key generation process. This replenishes the entropy used by your computer to generate random numbers.

Once the key is generated, you're ready to send an encrypted email. First, here's a quick primer on public key cryptography so you understand the basics of what you're doing.


Use POP
-------

If you've followed the guide so far, then you are already using the POP3 protocol to communicate with your email server. We set this option in the "New Mail Account" dialog box after entering the email address and password.

You may wish to configure your POP settings more closely. You can do so by editing the account settings. To access an account's settings, right-click on the account name in the left sidebar and choose "Settings...". Or in the menubar click Tools > Account Settings, and find the account you whose settings you wish to edit.  


