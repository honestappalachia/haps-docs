========
Overview
========

This is an overview of the Honest Appalachia secure submission system. We believe it strikes a good balance between security, ease of use, and cost effectiveness.

What does a successful upload look like?
----------------------------------------

This is a good way to get a bird's eye view on the system.

1.  A user visits the Honest Appalachia upload page, using Tor to anonymize their traffic. All of the pages at the honestappalachia.org domain force access through HTTPS.
2.  The upload page confirms that they are using a Tor exit node to communicate, and redirects them to the real upload site, a Tor hidden service.
3.  The user is presented with a simple web form allowing them to upload a file and optionally include comments about it.
4.  The file and comments are uploaded using HTTP over a Tor circuit to the hidden service. The user receives a confirmation page and is done.
5.  The hidden service encrypts the uploaded file with GPG and the Honest Appalachia public key, then uploads it to Amazon S3 for storage, where is further encrypted with AES-256. The original and encrypted files are securely deleted from the hidden service. 
6.  An activist for Honest Appalachia downloads the encrypted file from Amazon S3 and uses their private key to decrypt it. They review the upload files, carefully removing any information, like file metadata, that could identify the original source.
7.  The cleaned file may be distributed to journalists for analysis and publication.
