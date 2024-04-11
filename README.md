# Milestone Project 3

## Basic Recipe Book

This is a basic online recipe book for various users.  Features include viewing, editing and adding recipes - additional features may be added in the future.  

This website was designed to be a basic online recipe book that display recipes for all who like to cook. The focus of the site is to allow users to upload recipes and images for other users to search and use.

This is the third of four Portfolio Projects that the developer must complete during their Full Stack Software Development Program at The Code Institute.

The main requirements were to build a Non-Relational Database backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. The focus of this project is on data rather than any business logic. This also requires the developer to create functionality for users to create, locate, display, edit and delete records (CRUD functionality).
The full application can be viewed <a href="https://basic-recipe-book.herokuapp.com/" target="_blank" >here</a>.
 
## UX

This platform is targeted towards a wide range of end users, from those who are looking for quick and easy recipes due to a busy lifestyle, those who have a bit more time to browse and contribute, to those who simply love cooking and want to share their ideas and favourite recipes with the rest of the world!  The application is built fully responsive to provide an accessible user experience on all devices.

### Research

When the project’s initial planning began, informal discussions were held with members of my family and work colleagues to determine what features and expectations are important to users when browsing recipes. Existing recipe websites were also researched as inspiration.

### User Demographic

![recipe_user_1](https://user-images.githubusercontent.com/28737216/48661085-90193380-ea64-11e8-9caa-e2a98376aab3.PNG)

![recipe_user_2](https://user-images.githubusercontent.com/28737216/48661185-1c782600-ea66-11e8-89fe-3492de14ab1d.PNG)

![recipe_user_3](https://user-images.githubusercontent.com/28737216/48661190-27cb5180-ea66-11e8-8213-1e6a4fe3c82e.PNG)

![recipe_user_4](https://user-images.githubusercontent.com/28737216/48661158-880dc380-ea65-11e8-9d88-5ccceab2c4dd.PNG)


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
-	
-	Users can search for recipes using keywords to quickly find specific recipes.
-	Users can easily search the recipes without needing to register.


### Data Schema:

The following shows the basic set-up of the MongoDB database, which is hosted on the cloud-based Mlab DaaS:

### Wireframes / Mockups:

- User Flowchart - [View](/static/images/readme/data_flow.png)
- Home Page Wireframe - [View](/static/images/readme/home_wire.png)
- Register Page Wireframe - [View](/)
- Sign In Page Wireframe - [View](/)
- Search Page Wireframe - [View](/static/images/readme/search_wire.png)
- Search Results Page Wireframe - [View](/)
- Profile Page Wireframe - [View]()
- Add/Edit Page Wireframe - [View]()



## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features

The main features of the application are the following:

- View full list of all recipes contained in the database
- Search Function to allow users to search recipes containing specific ingredients.
- Function to allow users to Reset the search function and return them to the full list of recipes
- Registered users are allowed to edit only their own recipes.
- Registered users are allowed to upload recipes to the website.
- When adding new recipes / editing recipes users can also add New Categories.

### Features Left to Implement / Issues

Ideally, User Registration would be used on such an application for the CRUD operations within the database.  This would require Account Authentication / Login functionaility also

Full form validation would also be required to prevent users from ommiting required data.

Another issue noted is the fact that if a user wishes to add a New Category / Cuisine Type / Main Ingredient, then they must do so before they begin adding/editing current attributes of a recipe (as the page will refresh and any new/amended data will not be committed to the database)

When the responsiveness was tested on certain phones, the "Get Started" button on the Index page would not be displayed.

Lastly, there were issues with using nested data within some records, which required a change of approach to the data schema.


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
