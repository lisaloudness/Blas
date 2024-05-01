# Blas Test Document

[Main README.md file](/README.md)

[View live project](https://blas-8701405f8705.herokuapp.com/)

[View Github repository](https://github.com/lisaloudness/Blas)

</br>

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Manual Testing](#manual-testing)
3. [Automated Testing](#automated-testing)
   - [Code Validation](#code-validation)
   - [Browser Validation](#browser-validation)
4. [User Testing](#user-testing)
5. [Bugs and Issues](#bugs-and-issues)

</br>

## **Testing User Stories**

1. As an administrator of the site, I have the ability to create, modify and delete recipes to effectively manage the content.
2. As an administrator of the site, I can log out from the admin panel to disconnect from the website.
3. As an administrator of the site, I can manage categories.
4. As an administrator of the site, I can manage users.

   - When logged in as "Admin", the user has elevated rights to add, edit and delete all recipe content on the site.
   - When logged in as "Admin", the user is directed to an admin dashboard rather than user profile. The Admin Dashboard displays all recipes which are stored in the database.
   - The recipe cards displayed in the Admin Dashboard have prominent edit and delete function buttons.
   - When logged in as "Admin", the user can log out at any time by selecting the Log Out option which is displayed on the fixed navbar and only visible when an user is in session.
   - From the admin dashboard, "Admin" can navigate to Manage Categories Page. Here "Admin" can add new categories and delete existing categories.
   - From the admin dashboard, "Admin" can navigate to Manage Users Page. Here "Admin" can delete existing users.




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
   - When an user uploads a recipe to the website, the user may wish to include a picture of the finished dish as a visual to show an appealing and appenticing example of the recipe to another user. Photos must be uploaded as an url pasted into the appropriate input field on the add recipe form. If the registered user chooses not to upload an image when publishing a recipe, a stock image will be used in its place.

#### Epic: Navigation
1. Users can easily navigate the main pages of the website from the homepage and fixed navbar.	
2. Users can search for recipes using keywords to quickly find specific recipes.
3. Users can easily search the recipes without needing to register.
4. Users can easily search again or clear previous search.

   - The landing page has a large prominent button center screen that reads "Get Cooking!" which navigates the user to the main recipe database screen which shows all recipes available to view on the website. One click and the user, registered or not, can view all recipes available on Blas.
   - The fixed navbar is accesible throughout the browsing experience.  The options available to the user  on the navbar are dependant if the user is logged in or not.
   - All users to the site can browse the website for recipes of interest to them.
   - All users can search the website for a recipe containing a specific ingredient.
   - Only registered users have access to a personal profile page and the ability to add, edit and delete their own recipes.
   - Once an ingredient search has been performed, the search term will remain in the search box to remind the user what ingredient they have searched.  Previous search can be overwritten should the user want to perform another search.
   - After the first search has been performed, a "Show all recipes" button appears under the search box which will act as a reset button and return all recipes in the database. 


[Back to top](#blas-test-document)

</br>   

## **Manual Testing**

1. Developer Tools were used throughout the development process to test website responsiveness on all devices.

2. All links within the site were tested to ensure that:

   - All navigation links are working.
   - Social media links and third party partner links are working and open in a new page.
   - Hover states work correctly.

3. CRUD actions performed to ensure:
   - I am able to CREATE an user profile and submit a new recipe to the database.
   - I am able to READ all recipes available on the website.
   - I am able to edit and UPDATE recipes I have submitted to the website.
   - I am able to DELETE recipes I have uploaded to the website.

4. Website compatibility was tested on Firefox, Chrome, Edge and Safari browsers. No issues to note.   

[Back to top](#blas-test-document)
</br>

## **Automated Testing**

## **Code Validation**

The W3C Markup Validator and W3C CSS Validator Services were used to validate the website to ensure there were no syntax errors in the html and css code.  
[Home Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2F) - No error detected.

[Search Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Fget_recipes) - No error detected.

[Sign Up Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Fregister) - No error detected.

[Log In Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Flogin) - No error detected.

[Profile Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Fprofile%2Flisaj) - No error detected.

[Add Recipe Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Fadd_recipes) - No error detected.

[Edit Recipe Page - W3C Markup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Fedit_recipes%2F661fc83da2f6bb40d70f7418) - No error detected.

[Manage Categories - W3 Marup Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fblas-8701405f8705.herokuapp.com%2Fget_categories) - No error detected.

[JSHint](https://jshint.com/) - JSHint was used to validate the javascript code. No errors detected.

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - There were no error detected.
<details>
<summary>CSS Validator</summary>
![CSS Validator](/static/images/readme/CSS_validation.png)
</details>
<br>

[CI Python Linter](https://pep8ci.herokuapp.com/#) - The CI Python Linter was used to format and validate the python code to PEP8 standards. No Errors detected.
<details>
<summary>CI Python Linter</summary>
![CI Python Linter](/static/images/readme/CI_python_linter.png/)
</details>
<br>



## **Browser Validation**

The Chrome Light House test was used to audit the performance, accessibility, best practices, and SEO.  Here are the results:

1. Index / Home page
   - Desktop [Full report can be found here](/static/documentation/home_lighthouse.html)
   - ![Desktop Home Page Results](/static/images/readme/home_lighthouse.png "Light House Desktop Results")

   - Mobile [Full report can be found here](/static/documentation/home_mob_lighthouse.html)
   - ![Mobile Home Page Results](/static/images/readme/home_mob_lh.png "Light House mobile results")


2. Search page
   - Desktop [Full report can be found here](/static/documentation/search_lighthouse.html)
   - ![Desktop Facilities Page Results](/static/images/readme/search_lighthouse.png "Light House Desktop Results")

   - Mobile [Full report can be found here](/static/documentation/search_mobile_lighthouse.html)
   - ![Mobile Facilities Page Results](/static/images/readme/search_mob_lh.png "Light House mobile results")


3. Add Recipe page
   - Desktop [Full report can be found here](/static/documentation/addrecipe_form_lighthouse.html)
   - ![Desktop Newsletter Page Results](/static/images/readme/addrecipe_lighthouse.png "Light House Desktop Results")

   - Mobile [Full report can be found here](/static/documentation/form_mob_lighthouse.html)
   - ![Mobile Newsletter Page Results](/static/images/readme/form_mob_lh.png "Light House mobile results")


4. Sign Up page
   - Desktop [Full report can be found here](/static/documentation/signup_lighthouse.io-20240426T1)
   - ![Desktop Gallery Page Results](/static/images/readme/signup_lighthouse.png "Light House Desktop Results")

   - Mobile [Full report can be found here](/static/documentation/signup_mobile_lh.io-20240426T1)
   - ![Mobile Gallery Page Results](/static/images/readme/signup_mobile.png "Light House mobile results")


5. Admin Dashboard page
   - Desktop [Full report can be found here](/static/documentation/admin_lighthouse.html)
   - ![Desktop Gallery Page Results](/static/images/readme/admin_lighthouse.png "Light House Desktop Results")

   - Mobile [Full report can be found here](/static/documentation/admin_mobile_lighthouse.html)
   - ![Mobile Gallery Page Results](/static/images/readme/admin_mobile_lh.png "Light House mobile results")


6. Manage Categories page
   - Desktop [Full report can be found here](/static/documentation/manage_categories_lighthouse.html)
   - ![Desktop Gallery Page Results](/static/images/readme/manage_cat_lighthouse.png "Light House Desktop Results")

   - Mobile [Full report can be found here](/static/documentation/manage_cat_moile.html)
   - ![Mobile Gallery Page Results](/static/images/readme/manage_cat_mobile.png "Light House mobile results")


[Back to top](#blas-test-document)
</br>


## **User Testing**

The website was shared with family and colleagues for their valued feedback.
- More use could have been made of tooltipped instructions.
- Overall functionality of the site works well.
- The background photos appear zoomed on IOS devices.  This is a known bug of background-attachment-fixed style on IOS.
- Styling could be improved in terms of positioning on the page.


## **Bugs and Issues**
- There were no known bugs or issues found at time of testing.