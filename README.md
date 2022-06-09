
# DocumentCloud Move Account Add-On

This DocumentCloud Add-On helps transfer documents from one user to another. As long as the current user has the proper permissions, it will act on __all documents displayed in the current search.__ This can be helpful for merging accounts, transfering bulk documents between users, and other tasks. If you're moving a small number of documents (less than 25), you can instead simply select the documents you want to move and click "Edit" and "Change Owner," which is faster and provides a nicer interface. This Add-On is useful for bulk moves.

## Important: This Add-On will permanently change permissions to documents.

*Please read all instructions before running this Add-On. If you'd like assistance transferring documents or merging accounts, our team is happy to assist as well — just reach out to us via email at info at DocCloud's domain name.*

Note that currently there is little logging and diagnostic information for the Add-On, so it's good to check the number of documents before and after — transferring documents may take some time to work through the search indexes so it may take a time for the numbers to reflect, even after documents are properly transferred.

## Tips for using the Move Account Add-On

First, there's a few things you will want to have handy:

* The *username* of the account that currently has the documents, which you wish to transfer the documents away from. When logged in to accounts.muckrock.com, this will be the the string of characters in grey under your name towards the top left of the profile page:
![Screen Shot 2022-06-09 at 9 49 58 AM](https://user-images.githubusercontent.com/136939/172863294-124b9dc1-a6f6-4a79-8c22-46a0e6580174.png)
* The *user id* of the account which will receive the documents. This is a __number__, not a username. While logged in as the user that will be receiving the documents, if you click "Your Documents" it's the string of numbers after your name.
![Screen Shot 2022-06-09 at 9 53 52 AM](https://user-images.githubusercontent.com/136939/172864148-bdc1428d-a833-4eba-afd5-1d67589e1347.png)
* If you'd like to move the organization that the documents are associated with, also get the organization ID. While logged in as either user, make that organization your active organization and then click "`Organization Name`'s Documents." It will be the number at the end of that name.
![Screen Shot 2022-06-09 at 9 56 07 AM](https://user-images.githubusercontent.com/136939/172864645-2f0c2a69-e0fa-459f-bfce-5d6af50f5729.png)
To transfer the documents to a different organization, both the old and the new owner must be a member of that organization.

A few things to do or check in advance:

* First, both users *must* be in at least one shared organization. This helps reduce spam and other types of potential abuse. If you need to, [create a new organization](https://accounts.muckrock.com/organizations/) and add both users to it.
* Second, this will only transfer document permissions. If you'd like to transfer projects, please go to the old user and invite the new user to all the projects you'd like them to have permissions to.

Another important note is how permissions can vary depending on organizational ownership and the published status of the document.

* If a document is private and you own it and it's in an organization you're no longer part of, you still have edit access.
* If a document is public and you own it and it's in an organization you're no longer part of, __you will lose all editing access to the document.__ This is to prevent accidental or purposeful deletion of documents that are linked to or embedded within published stories. You may still add such such to projects or add private annotations. If you need to make other alterations or change a public aspect of the document, you can download and re-upload the document, or you may request to be added to the organization at which point you'll regain permissions.
