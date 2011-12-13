============
Secure Email
============

Our recommendations in this document are based on our own security policies, as well as information from the EFF's `SSD (Security Self Defense) project <https://ssd.eff.org/>`_.

Outline:

1.  Get a separate e-mail for activist work
2.  Use POP - don't store your email in the cloud!
3.  Use encryption

Get a separate e-mail account
------------------------

You may be using email provided by your ISP (AOL, Hotmail, MSN, etc.) an organization you work for (mark.felt@fbi.gov), or maybe you use a free webmail service like GMail or Yahoo Mail. Although it is fine to use such an e-mail account for day-to-day use, *they are not safe* for use by whistleblowers or activists concerned about government surveillance. 

Why?
~~~~

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

4.  There is a trade-off between security and convenience. Unless you take additional complicated and risky steps, secure email can only be accessed on your physical computer, and you have the only copies of that email, making it your responsibility to back it up. You lose the convenience of services like GMail.

How?
~~~~

At the bare minimum, get a separate email from a free webmail provider like GMail, and try not to share any personally identifying information during the registration process. If you encrypt your email and use POP to access it, you will minimize the data available to government and law enforcement.

We recommend using a communications provider that serves the public because it gives you `stronger legal protections <https://ssd.eff.org/3rdparties/govt/stronger-protection>`_, and the best choice is a service that is designed with activists in mind and performs minimal logging. 

In the US, we've had great results using the email provided by `Riseup https://riseup.net/>`_. They're a Seattle-based collective providing digital resources for activists. Their services are free to use, but consider donating if you find them useful.

Note that most alternative e-mail providers don't have the same resources as big companies like Google, Yahoo, or Microsoft. As a result, their storage limits are much lower. Riseup's is around 20MB, for example, compared to Google's approximately 7GB. Although you can fit a lot of plain text email into 20MB, you should be careful with attachments, especially larges ones like images. Accessing your email through POP, as described in the next section, also means this will be less of an issue.

Use POP
-------

enabling POP in gmail: https://mail.google.com/support/bin/answer.py?answer=13273

------------------
Encrypt your email
------------------

This tutorial is written for users of Thunderbird with the Enigmail plugin. It was developed on a Mac but should work with minimal modification for any OS.

For your security, it's important to keep Thunderbird and plugins like Enigmail up-to-date. Thunderbird is configured to automatically download and install updates to itself and its add-ons. You can check these settings by opening the Preferences, going to the Advanced pane and then the Update section. If you open Thunderbird and it informs you that updates are available, *do not ignore it*. Promptly install the updates and restart Thunderbird so they go into effect.

+++++++++++++++++++++++++++++++++++++++++++++
Step 1: Add your email account to Thunderbird
+++++++++++++++++++++++++++++++++++++++++++++

If you haven't done so already, add your email account to Thunderbird with File > New Mail Account. We'll assume that the default configuration is fine for now, coming back to the idea of using POP for additional security later.

+++++++++++++++++++++++++++++++++++++++++++++++
Step 2: Create a keypair for this email account
+++++++++++++++++++++++++++++++++++++++++++++++

Go to OpenPGP > Key Management. This shows you a list of all the keys currently in your keyring (saved on your computer). Notice that the menubar has changed.

To add a new keypair, select Generate > New Key Pair. In the top menu, select the email account you wish to generate a keypair for. Choose a strong passphrase and type it in twice. Remember that GPG key passphrases can include spaces, and can be up to 60 characters (?) in length. Leave the defaults where they are, and click "Generate key". Now you will have to wait for the system to generate your keypair. As the note states, this may take several minutes. You can speed up the process by actively using your computer during the key generation process. This replenishes the entropy used by your computer to generate random numbers.

Once the key is generated,

