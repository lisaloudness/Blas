# Blas - Testing

[Main README.md file](/README.md)

[View live project](https://blas-8701405f8705.herokuapp.com/)

[View Github repository](https://github.com/lisaloudness/Blas)

</br>

## Table of Contents

1. [Testing User Stories](#Testing-User_Stories)
2. [Manual Testing](#Manual-Testing)
3. [Automated Testing](#Automated-Testing)
   - [Code Validation](#Code-Validation)
   - [Browser Validation](#Browser-Validation)
4. [User Testing](User-Testing)

</br>

## **Testing User Stories**

1. As an administrator of the site, I have the ability to create, modify and delete recipes to effectively manage the content.
2. As an administrator of the site, I can log out from the admin panel to disconnect from the website.
   - When logged in as "Admin", the user has elevated rights to add, edit and delete all recipe content on the site.
   - When logged in as "Admin", the user is directed to an admin dashboard rather than user profile. The Admin Dashboard displays all recipes which are stored in the database.
   - The recipe cards displayed in the Admin Dashboard have prominent edit and delete function buttons.
   - When logged in as "Admin", the user can log out at any time by selecting the Log Out option which is displayed on the fixed navbar and only visible when an user is in session.



#### Epic: Login / Register
1. Users can register for an account to engage with the sites content.
2. Users can log in or out of their accounts to connect or disconnect from the website.
3. Users can easily check if they are logged in or out to know their current status.
   - First time users to the website are invited to "sign up" as a registered user on the home page.
   - On the "sign up" page, first time users are informed of the benefits of being a registered user, i.e. ability to add, edit delete content.
   - When a first time user signs up to the website, they are redirected to their personal profile page.
   - When a registered user signs up to the website, they are redirected to their personal profile page.
   - A registered user can easily check their log in status by hovering over the profile icon which is visible on the fixed navbar only when an user is logged in.  When the user hovers over the profile icon, a tooltip will flash stating "You are logged in <username>".
   - In order to sign up to the website, the user must register an username and password on the sign up page. This action also logs in the user in the first instance.
   - A user must be a registered user in order to log in and view their personal profile page.
   - Only when an user is logged in does a logout link appear on the fixed navbar. By selecting this, the user cookie session ends.  

#### Epic: Registered Users
1. As a logged-in user, I can publish recipes for others to see.
2. As a logged-in user, I have the ability to delete my own recipes.
3. As a logged-in user, I can edit recipes to make updates or correct errors.
4. As a logged-in user, I can upload images alongside my recipe for others to view the dish.
   - When an user is logged-in, the user is re-directed to their profile page which has bold clear links to add recipes at the top of the page. By selecting the "add" recipe icon, the user is re-directed to the add recipe page which is a form The form is made up of various input fields and drop down fields which the user completes and submits to the database.
   - The add recipe button is only visible to logged-in users on the fixed navbar.
   - The edit button is visible on recipe cards on the search recipes page only when the session username matches the "created by" username.
   - When an user uploads a recipe to the website, the user may wish to include a picture of the finished dish as a visual to show an appealing and appenticing example of the recipe to another user. Photos must be uploaded as an url pasted into the appropriate input field on the add recipe form. If the registered user chooses not to upload an image when publishing a recipe, a stock image will be uploaded in its place.

#### Epic: Navigation
1. Users can easily navigate the main pages of the website from the homepage and fixed nav bar.	
2. Users can search for recipes using keywords to quickly find specific recipes.
3. Users can easily search the recipes without needing to register.
4. Users can easily search again or clear previous search



[Back to top](#Blas---testing)

</br>   

## **Manual Testing**

1. Developer Tools were used throughout the development process to test website responsiveness on all devices.

2. All links within the site were tested to ensure that:

   - All navigation links are working.
   - Social media links and third party partner links are working and open in a new page.
   - Hover states work correctly.

3. The form element on the Newsletter tab was tested to ensure that:
   - The ''Required'' fields are working.
   - The submit button opens the code institute form dump page in a new tab.
   - The radio button is set to default.

4. Website compatibility was tested on Firefox, Chrome, Edge and Safari browsers. No issues to note.   

[Back to top](#Victoria-park---testing)
</br>

## **Automated Testing**

## **Code Validation**

The W3C Markup Validator and W3C CSS Validator Services were used to validate the website to ensure there were no syntax errors in the html and css code.  
[W3C Markup Validator](https://validator.w3.org) - There were no error detected.
![HTML Validation, no error detected](assets/testing/w3_index.png "HTML Validation, no error detected")

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - There were no error detected.
![CSS Validator, no error detected](assets/testing/w3_css.png "CSS Validation, no error detected")

## **Browser Validation**

The Chrome Light House testing was used to audit the performance, accessibility, best practices, and SEO. After applying some changes to make the performance faster, including converting all images to webp format, setting a width and height to some images. Here are the results:

1. Index page
   - Desktop [Full report can be found here](assets/testing/home_desktop.com-2023)
   - ![Desktop Home Page Results](assets/testing/home_desktop_lh.png "Light House Desktop Results")

   - Mobile [Full report can be found here](assets/testing/home_mobile.com-2023)
   - ![Mobile Home Page Results](assets/testing/home_mobile_lh.png "Light House mobile results")


2. Facilities page
   - Desktop [Full report can be found here](assets/testing/facilities_desktop.com-2023)
   - ![Desktop Facilities Page Results](assets/testing/facilities_desktop_lh.png "Light House Desktop Results")

   - Mobile [Full report can be found here](assets/testing/facilities_mobile.com-2023)
   - ![Mobile Facilities Page Results](assets/testing/facilities_mobile_lh.png "Light House mobile results")


3. Newsletter page
   - Desktop [Full report can be found here](assets/testing/contact_desktop.com-2023)
   - ![Desktop Newsletter Page Results](assets/testing/contact_desktop_lh.png "Light House Desktop Results")

   - Mobile [Full report can be found here](assets/testing/contact_mobile.com-2023)
   - ![Mobile Newsletter Page Results](assets/testing/contact_mobile_lh.png "Light House mobile results")


4. Gallery page
   - Desktop [Full report can be found here](assets/testing/gallery_desktop.com-2023)
   - ![Desktop Gallery Page Results](assets/testing/gallery_desktop_lh.png "Light House Desktop Results")

   - Mobile [Full report can be found here](assets/testing/gallery_mobile.com-2023)
   - ![Mobile Gallery Page Results](assets/testing/gallery_mobile_lh.png "Light House mobile results")


[Back to top](#Victoria-park---testing)
</br>


## **User Testing**

The website was shared with family and colleagues for their valued feedback. Common issues noted in the feedback were fixed
- The social media icons for Instagram and Twitter were in the wrong place.
- Twitter is now re=branded as X.
- The background photos appear zoomed on IOS devices.  This is a known bug of background-attachment-fixed style on IOS.
- The original background color chosen from the color palette was changed from #9CD9A8 to a stronger #62760c to compliment the font color and stronger contrast.


