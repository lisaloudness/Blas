# **Blas Recipe Website**

![Resonive All Screens](/static/images/readme/readme_screens.png)

## **Table Of Content**
1. [Introduction](#introduction)
2. [Development](#development)
3. [UX](#ux)
   - [User Demographic](#user-demographic)
   - [User Stories](#user-stories)
4. [UI](#UI)
   - [Layout](#layout)
   - [Typography](#typography)
   - [Color Scheme](#color-scheme)
5. [Testing](#testing)  
6. [Technologies Used](#technologies-used)
7. [Deployment](#deployment)
8. [Future Development](future-development)
9. [Credits & Acknowledgements](#credits-&-acknowledgements)

## **Introduction**

This website was designed to be a basic online recipe book that display recipes for all who like to cook. The focus of the site is to allow users to upload recipes and images for other users to search and use.

This is the third of four Portfolio Projects that the developer must complete during their Full Stack Software Development Program at The Code Institute.

The main requirements were to build a Non-Relational Database backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. The focus of this project is on data rather than any business logic. This also requires the developer to create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
The full application can be viewed <a href="https://blas-8701405f8705.herokuapp.com/" target="_blank" >here</a>.

[Back to top](#blas-recipe-website)
 
## **Development**

This platform is targeted towards a wide range of end users, from those who are looking for quick and easy recipes due to a busy lifestyle, those who have a bit more time to browse and contribute, to those who simply love cooking and want to share their ideas and favourite recipes with the rest of the world!  The application is built fully responsive to provide an accessible user experience on all devices.

### Research

When the project’s initial planning began, informal discussions were held with members of my family and work colleagues to determine what features and expectations are important to users when browsing recipes. Existing recipe websites were also researched as inspiration.

### User Demographic

![recipe_user_1](https://user-images.githubusercontent.com/28737216/48661085-90193380-ea64-11e8-9caa-e2a98376aab3.PNG) ![recipe_user_4](https://user-images.githubusercontent.com/28737216/48661158-880dc380-ea65-11e8-9d88-5ccceab2c4dd.PNG)  
![recipe_user_3](https://user-images.githubusercontent.com/28737216/48661190-27cb5180-ea66-11e8-8213-1e6a4fe3c82e.PNG) ![recipe_user_2](https://user-images.githubusercontent.com/28737216/48661185-1c782600-ea66-11e8-89fe-3492de14ab1d.PNG)


### User-Stories

#### Epic: Admin

-	As an administrator of the site, I have the ability to create, modify and delete recipes to effectively manage the content.
-	As an administrator of the site, I can log out from the admin panel to disconnect from the website.

#### Epic: Registered Users
-	As a logged-in user, I can publish recipes for others to see.
-	As a logged-in user, I have the ability to delete my own recipes.
-	As a logged-in user, I can edit recipes to make updates or correct errors.
-	As a logged-in user, I can upload images alongside my recipe for others to view the dish.
#### Epic: Login / Register
-	Users can register for an account to engage with the sites content.
-	Users can log in or out of their accounts to connect or disconnect from the website.
-	Users can easily check if they are logged in or out to know their current status.
#### Epic: Navigation
-	Users can easily navigate the main pages of the website from the homepage and fixed nav bar.	
-	Users can search for recipes using keywords to quickly find specific recipes.
-	Users can easily search the recipes without needing to register.
-   Users can easily search again or clear previous search

[Back to top](#blas-recipe-website)


## **UX**

### Data Schema:

The following shows the basic set-up data schema of the MongoDB database:
![mongodb categories](/static/images/readme/mongo_schema.png)


### Wireframes / Mockups:

- User Flowchart - [View](/static/images/readme/data_flow.png)
- Home Page Wireframe - [View](/static/images/readme/home_wire.png)
- Register Page Wireframe - [View](/)
- Sign In Page Wireframe - [View](/)
- Search Page Wireframe - [View](/static/images/readme/search_wire.png)
- Search Results Page Wireframe - [View](/)
- Profile Page Wireframe - [View]()
- Add/Edit Page Wireframe - [View]()

[Back to top](#blas-recipe-website)

## Features

### Design Features
Each page of the website features a consistent responsive navigational system:

- The **Header** contains a conventionally placed logo in the top left of the page (whereby clicking this will redirect users back to the home page) and a navigation bar in the right of the header. On smaller screens, the navigation bar condenses into a dropdown with navigation options and the logo moves to center screen.


- The **Footer** is kept simple containing only social links and disclaimer information. On smaller screens, this condenses into a single column, with each section moving underneath its neighbour on the left.

<dl>
  <dt><a href="https://blas-8701405f8705.herokuapp.com/home/" target="_blank" alt="Home Page">Home Page</a></dt>
  <dd>The Home Page is laid out with a nav section on top, an image below the width of the screen. The features are as follows:
     <ul>
          <li><strong>Get Cooking! Button</strong> - On the home screen you will see, a bold, colourful button with the words “Get Cooking” to invite and entice the user into clicking further into the website.
          </li>
          <li><strong>Sign Up</strong> - Under the above mentioned button, there will be a link inviting first time users to sign up. This will navigate to the sign up page.
          </li>
     </ul>
  </dd>

  <dt><a href="https://blas-8701405f8705.herokuapp.com/get_recipes/" target="_blank" alt="Search Recipes">Search Recipes Page</a></dt>
  <dd>This is the main page of the website where all users (registered or unregistered) will be able to view and search all recipes.
     <ul>
          <li><strong>Search Box</strong> - This will be the main focus of the page, allowing users to enter a search term.
          </li>
	<li><strong>Recipe Cards</strong> - Below the search box will be individual recipe cards displayed in rows to fill the screen.  Allowing all recipes to display in this way will prompt the user to use the search box and not overwhelm with the entire library.
          </li>
<li><strong>Search Results</strong> - These will appear on the same page and the remaining library will be hidden.
          </li>
<li><strong>Search Box</strong> - Once a search has been performed, a reset button will appear below the search box enabling the user to revert to the all in library.
     </ul>
  </dd>

  <dt><a href="https://8080-lisaloudness-blas-udlva2oew1g.ws-eu110.gitpod.io/view_recipes/6617e2e2c4ee9a40c5af29ac" target="_blank" alt="View Recipe">View Recipe Page</a></dt>
  <dd>
     <ul>
          <li><strong>Featured Image</strong> - The featured image shows the image the user uploaded, or the stock placeholder image if no image was uploaded by the user.
          </li>
          <li><strong>Edit Buttons</strong> - If the user is logged in and is the author of the said recipe, clicking the edit button will bring the user to the edit page. The recipe details are populated into the form and the user can edit the information, upload a new image and save the information. 
          </li>
     </ul>
  </dd>

  <dt><a href="https://blas-8701405f8705.herokuapp.com/edit_recipes/6617e2e2c4ee9a40c5af29ac" target="_blank" alt="Edit Recipe Page">Edit Recipe Page</a></dt>
  <dd>This page shows the form populated with the specific recipe's information which can be saved and edited:
     <ul>
          <li><strong>Edit Recipe Form</strong> - The form is prepopulated with all the recipe information. The user can edit this information, only if they are the author of the recipe. Saving this recipe redirects the user to their profile page where they can then view their uploaded recipe list.
          </li>
     </ul>
  </dd>

  <dt><a href="https://blas-8701405f8705.herokuapp.com/add_recipes/" target="_blank" alt="Add Recipe Page">Add Recipe Page</a></dt>
  <dd>This page has a form that allows the user to add a recipe, as well as upload an image:
     <ul>
          <li><strong>Add Recipe Form</strong> - An empty form is displayed, allowing the user to enter the recipe details, as well as upload an image of the recipe. If no image is uploaded, the stock placeholder image is saved instead. Adding this recipe redirects the user to their profile page where they can then view their uploaded recipe list.
          </li>
     </ul>
  </dd>

  <dt><a href="https://blas-8701405f8705.herokuapp.com/login" target="_blank" alt="Sign In Page">Sign In Page</a></dt>
  <dd>This page has a form allowing the user to enter their username, email and password to register an account:
     <ul>
          <li><strong>Sign In Form</strong> - This form has two input fields, the username and the password. A submit button at the end of the form login the user in if the information was correct and has not been used by other users previously, and redirects the user to their profile page.
          </li>
     </ul>
  </dd>
  
  <dt><a href=" https://blas-8701405f8705.herokuapp.com/register" target="_blank" alt="Sign Up Page">Sign Up Page</a></dt>
  <dd>This page has a form allowing the user to enter their username and password to register an account:
     <ul>
          <li><strong>Sign In Form</strong> - This form has two input fields, username and password. A submit button at the end of the form login the user in if the information was correct and has not been used by other users previously, and redirects the user to their profile page.
          </li>
     </ul>
  </dd>
</dl>
 
### Existing Features
- **Header Logo** - Appearing on every page for brand recognition. Clicking the logo will return the users to the home page, as expected.
- **Header Navigation Bar** - Appearing on every page for a consistently easy and intuitive navigable system.
- **Social Icons** - Appearing on every page, the icons are appropriate representations of the Social Media platforms, found in the footer.
- **Recipe Cards** - Appearing on the search page and profile page, the recipe cards give a brief overview of the recipe, showing the image, description, servings, prep and cook time.
- **Recipe Form** - Access by clicking the “+” icon on the profile page, the form allows the user to add or edit a recipe, including adding an image to display on the recipe page and recipe card.
- **Search Page** - A page that shows the user the site's available recipes, shown as recipe cards. If the user is logged in and their username matches user that created that card, an edit icon will be visible on the recipe card.
- **Recipe Page** - A recipe page whose content changes with the recipe details of the chosen recipe. 
- **Add/Edit Recipe Page** - A page designed to allow the user to add a recipe if logged in, and edit a recipe if they are logged in as the recipe's author. 
- **Sign In Page** - A page designed to allow the user to log in using previously created user details; a username and a password.
- **Sign Up Page** - A page designed to allow the user to create a user profile using a username and a password.

### Features to Implement in the future
- **Comments Section**
     - This feature would have been used to allow users to comment on each others recipes and provide feedback to the author and future users.

- **Further use of info modals**
     - This feature would have been used to confirm that the user wished to go ahead with an action e.g. “Are you sure you want to log out?”

- **Carousel Card Display**
	- This feature would have been used on the home page so users could get an instant idea of the recipes on offer.
- **Ability to create further categories by Admin**
	- When mentally planning out this project, this feature was always going to be included but I simply ran out of time before submission date.

























The main features of the application are the following:

- View full library of all recipes contained in the database.
- Search Function to allow users to search recipes containing specific ingredients.
- Function to allow users to Reset the search function and return them to the full list of recipes
- Registered users are allowed to edit only their own recipes.
- Registered users are allowed to upload recipes to the website.
- When adding new recipes / editing recipes users can also add New Categories.

 
### Home Page

### Recipes / Result Page

### Login / Sign Up Page

### Profile Page


### Admin Page


### Add Recipe Page

### Edit Recipe Page

The main features of the application are the following:

- View full list of all recipes contained in the database
- Search Function to allow users to search recipes containing specific ingredients.
- Function to allow users to Reset the search function and return them to the full list of recipes
- Registered users are allowed to edit only their own recipes.
- Registered users are allowed to upload recipes to the website.
- When adding new recipes / editing recipes users can also add New Categories.

[Back to top](#blas-recipe-website)

### Future Developments

Ideally, User Registration would be used on such an application for the CRUD operations within the database.  This would require Account Authentication / Login functionaility also

Full form validation would also be required to prevent users from ommiting required data.

Admin functionality would be a key value pair using, for example, a toggle switch for is_admin? or is_superuser therefore potentionally allowing more than one admin or superuser and not being reliant on an unique username.

When the responsiveness was tested on certain phones, the "Get Started" button on the Index page would not be displayed.

Lastly, there were issues with using nested data within some records, which required a change of approach to the data schema.

[Back to top](#blas-recipe-website)

# Technologies Used

## Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)


## Frameworks, Libraries & Programs Used
[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Materializecss](https://materializecss.com/)- used for basic HTML templates and styling.

[Mongodb]( https://cloud.mongodb.com/v2/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=492438439811&utm_term=cloudinary&gclid=Cj0KCQiAt8WOBhDbARIsANQLp96hTerzfFJ_P9lX0tEYEdtM3tSsYB6fhw-x3wQxOO0oc4hXm-A2ZBUaAptIEALw_wcB) - Used to store images online for the recipe posts. 

[Summernote](https://summernote.org/) Used to add a text area field to the admin setup to enable a list of ingredients and method steps.

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Balsamiq](https://balsamiq.com/) - was used to create site wireframes.

[Am I Responsive](http://ami.responsivedesign.is/) - to check if the site is responsive on different screen sizes.

[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/) - were used for all the images

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - was used to validate HTML

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - was used to validate CSS

[Beautify](https://www.jpkc.com/tools/beautify/) - was used to correct indentation issues and get rid of too much whitespace - HTML, CSS

[Coolors](https://coolors.co/9df57a-3c444c-fee73b-ff4f98-2daaf3-a9bedb) - to make color palette



## Technologies used

Technologies used in this project include:

* Materialize: Materializecss 
* HTML5/CSS: Used for the layout and styling of the application.
* Python 3.4.3: The back end functionality of the application was written entirely in python 3.0.
* Flask Microframework: Flask was used to extend pythons functionality to the front end.
* Balsamiq: Used to create the below wireframes.
* Gitpod used as development environment workspace
* The project uses **JQuery** to simplify DOM manipulation.

[Back to top](#blas-recipe-website)

## Testing

Mainly manual testing used throughout - for routing and checking if data is properly rendered in the correct template and format, "test_app.py" was used, whereby on satisfactory completion, the clean functional code would then be transferred to the "app.py" file

Basic testing included:

- DB Connection
- Editing Recipes
- Adding Recipes
- Adding new Categories / Main Ingredients / Cuisine Type
- Rendering data / images

Many GitHub commits will contain the prefix `TESTING`

Pep 8 was used to assist with cleaning the data - indentation, whitespaces, non-spaces, 2 lines expected

http://pep8online.com/

[Back to top](#blas-recipe-website)

## Deployment
This website is deployed to Heroku from a GitHub repository, the following steps were taken:

#### Creating a Repository on GitHub
- First make sure you are signed into [Github](https://github.com/) and go to the code institutes template, which can be found [here](https://github.com/Code-Institute-Org/ci-mongo-template).
- Then click on **use this template** and select **Create a new repository** from the drop-down. Enter the name for the repository and click **Create repository**.
- Once the repository was created, I clicked the green **code** button and copied the HTTPS address. I then navigated to [Codeanywhere](https://app.codeanywhere.com/) and clicked on **New Workspace** to create a workspace in codeanywhere so that I could write the code for the site.
  
#### Making a Local Clone
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LHarveyDev/the-kitchen-cupboard)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/LHarveyDev/the-kitchen-cupboard
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/LHarveyDev/the-kitchen-cupboard
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

#### Forking the Github Repository 
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LHarveyDev/the-kitchen-cupboard.git)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

#### Creating an app on Heroku
- After creating the repository on GitHub, head over to [heroku](https://www.heroku.com/) and sign in.
- On the home page, click **New** and **Create new app** from the drop down.
- Give the app a name(this must be unique) and select a **region** I chose **Europe** as I am in Europe, Then click **Create app**.

#### Deploying to Heroku.
- In Codeanywhere CLI, the root directory of the project, run: pip3 freeze --local > requirements.txt to create a requirements.txt file containing project dependencies.
- In the Codeanywhere project workspace root directory, create a new file called Procfile, with capital 'P'. Open the Procfile. - Inside the file, check that web: python3 app.py has been added when creating the file Save the file.
- Push the 2 new files to the GitHub repository
- Login to Heroku, select Create new app, add the name for your app and choose your closest region.
- Navigate to the Deploy tab on Heroku dashboard and select Github, search for your repository and click 'connect'.
- Navigate to the settings tab, click reveal config vars and input the following:


| Key | Value
|:-------:|:--------|
| DATABASE_URL  |    |
| IP  |    |
|  PORT |    |
|  SECRET_KEY   |     |

Actual Enviroment variables not disclosed for security. They can be found in my env.py file which has been added to my .gitignore file within my project and therefore is not commited to github.

[Back to top](#blas-recipe-website)

## Credits

### Code

- Code Institute's Task Manager project walkthrough. Used to create the user authentication function [Code Institute](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/02-UserAuthenticationAndAuthorization/04-login_functionality)
- Code Institute's Task Manager project walkthrough. Used to create the search function [Code Institute](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/app.py#L28)
- The Flask documentation was referred to throughout the project [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/)
- The Materialize documentation was used to create the various components.
- I also used Slack to view other students work in the project-milestone-3 and peer-code-review channels

## Credits

### Content
- Recipe details were copied from https://www.bbcgoodfood.com to create the recipe library.

### Media
- The photos used for the recipes were sourced from https://www.bbcgoodfood.com

### Acknowledgements

- I received inspiration for this project from https://www.bbcgoodfood.com
- I would like to thank

[Back to top](#blas-recipe-website)
