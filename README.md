# InfiniteShoot

This webapp represents the concept of a business focused on photo shooting and creating albums for different
events such as graduation, marriage or birthday parties. The webapp is well automated with lots of subsystems
such as authentication, album builder or personal gallery view.

![Website main page](infiniteshoot_documentation/picture1.jpg)

## Backend

In the backend I have 9 databases each of them very important for the functionality and infrastructure of 
the app.

* APPOINTMENT which includes only one table, Appointments
* AUTHENTICATION AND AUTHORIZATION which includes the login system and users table
* BLOG which contains one table, Posts
* CONTACT which includes two tables: Contacts and Newsletters
* GALLERY which contains the customized tables: Client Catalogues, Images Clients, and Platform Presentation 
  Images
  
The databases can be seen below in the administration panel of the webapp:

![Website main page](infiniteshoot_documentation/picture2.jpg)

##### APPOINTMENT

The appointments table includes all the appointments who are requested by the user using a form inside 
the webapp. It includes fields such as phone number, full name and desired date for the photo shoot to happen.
The system is pretty simple, the user is making an appointment for a photo shoot, and because it is assumed 
that the freelancer or business owner already has an appointment system, the app just saves the data into a database so that
the freelancer just has to connect to the person to talk about details such as where should be the photo shoot
or if the date is right. This scenario seems very real because the process of creating interoperability
between the app and the appointment system would be very time-consuming and money-consuming. That being said,
this solution (interoperability) will pretty much be avoided by both the programmer and freelancer or business owner.

##### How does the form looks in the user view

![Website main page](infiniteshoot_documentation/picture3.jpg)

From the administration panel, the superuser is able to check messages and set them as seen or not and also
set them to accepted or refused. This can be seen in the screenshot below:

![Website main page](infiniteshoot_documentation/picture4.jpg)