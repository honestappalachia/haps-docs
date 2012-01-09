========
Overview
========

Quick Outline
-------------

Honest Appalachia allows users to upload files safely and anonymously through our secure upload site. The secure upload site is a Tor Hidden Service, a web server using a special protocol that protects the anonymity of both the client and the server.

When the hidden service receives a file, it encrypts it and uploads it to a separate file server before securely deleting the original copy. This encrypted copy is only accessible to members of Honest Appalachia, who will retrieve these files and strip them of metadata that could potentially identify the source.

Once a "cleaned" version of the uploaded file is produced, it will be distributed among our network of journalists and potentially published for the public to view on our website.

Design Choices
--------------

This is an overview of the Honest Appalachia secure submission system. The goal is to strike a balance between security, ease of use, and cost effectiveness.

Security fanatics may disagree with some of our choices in developing this system, but there is always a trade-off between convenience, cost, and security. These documents describe what we consider to be the most practical solutions, along with suggestions of additional measures that could be taken for added security if more resources were available.

Honest Appalachia is focused on serving the Appalachia region of the United States of America, so currently our threat model, subsequent design, and recommendations are all based on the surveillance capabilities of US government and law enforcement, and the legal rights of US citizens. Consider :ref:`contribute` if you want to support other parts of the world.

Much of this documentation refers to evading law enforcement or government surveillance. While whistleblowing is legally protected in the United States, its legal status is loosely and inconsistently defined, primarily at the state level. Therefore we assume the worst, and act to protect whistleblowers even if they could be threatened by unjust uses of the legal system. In a truly just and democratic society, whistleblowers would not need to fear their government and this site would not be necessary in the first place.

Threat Analysis
---------------

The primary goal of Honest Appalachia is *protecting the identity of sources*, with a secondary goal being resistance to takedown or interference.

Protecting the Identity of Sources
++++++++++++++++++++++++++++++++++

..  note::
    The greatest threat to the anonymity of any whistleblower is themselves. Unfortunately, there is nothing we can do to protect people from speaking too candidly or putting trust in the wrong people. 
    
    The most well-known alleged source to Wikileaks, Bradley Manning, was arrested only after he described sharing classified information with Wikileaks to Adrian Lamo over AIM, who subsequently turned him in to the FBI. Given the security precautions Manning said he took in the portions of these chat logs that have been published, it seems unlikely that he would have been caught due to any flaw in his process of copying information or the Wikileaks submission protocol. The old maxim that humans are the weakest link in any secure system goes both ways.

    Our only solution to this difficult problem is education. Hopefully by understanding what is involved in an act of whistleblowing, including the legal and psychological consequences, people will carefully consider their choices and make better decisions in the long run.

Honest Appalachia focuses on the *technical* threat model related to the identity of sources, which begins the moment a potential source accesses our website.

The three main avenues for revealing a source's identity are through:

1.  Surveillance/analysis of the transfer of the file, or records of it
2.  The file itself may contain identifying information about the source
3.  Communications between the source and Honest Appalachia could reveal their identity

An important point to note here is that complete anonymity for sources is beneficial for both sources and Honest Appalachia activists. **We don't want to know who you are**. This concept is sometimes referred to as **plausible deniability**, and it protects everybody involved.

Avoiding surveillance/analysis of the upload
********************************************

Passive and active surveillance are both concerns here. Your internet activity is always being logged by at least two sources:

1.  The Internet Service Provider (ISP) who connects you to the Internet
2.  The websites you are visiting

It can additionally be logged by other stops along the network; for example, a coffee shop's free wireless router may be logging your internet access.

There are two important techniques used to avoid surveillance of data "on the wire". The first is to use an encrypted connection. This is why we use HTTPS for all of the sites at the ``honestappalachia.org`` domain. Using HTTPS additionally makes these sites harder to hack, by reducing the chance that a hacker might sniff login credentials and subsequently gain access to the site.

To be continued...

What does a successful upload look like?
----------------------------------------

This is a good way to get a bird's eye view on the system.

1.  A user visits the Honest Appalachia upload page, using Tor to anonymize their traffic. All of the pages at the honestappalachia.org domain force access through HTTPS.
2.  The upload page confirms that they are using a Tor exit node to communicate, and redirects them to the real upload site, a Tor hidden service.
3.  The user is presented with a simple web form allowing them to upload a file and optionally include comments about it.
4.  The file and comments are uploaded using HTTP with the Tor hidden service protocol, which is end-to-end encrypted. The user receives a confirmation page and is done.
5.  The hidden service encrypts the uploaded file with a GPG public key, then uploads it to Amazon S3 for storage, where is further encrypted with AES-256. The original and encrypted files are securely deleted from the hidden service. 
6.  An activist for Honest Appalachia downloads the encrypted file from Amazon S3 and uses their private key to decrypt it. They review the upload files, carefully removing any information, like file metadata, that could identify the original source.
7.  The cleaned file is distributed to journalists for analysis and publication.
