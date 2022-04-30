# Treasure Island
## Introduction

The live link can be found here - (https://treasure-island.herokuapp.com/)

Welcome to Treasure Island. Treasure Island is simple Blog but very informative blog site which gives users information about E-Commerce stores. Treasure Island blog site is about E-Commerce Store's. 

 This blog website will allow user complete CRUD system. User can register to website, user can comment on the blogs. User can add new category about E-Commerce and can add valueable information.

## Table of Contents

# Table of Contents
 [1. User Expereince (UX) design](#ux)
  - [1.1. Strategy:](#strategy)
    - [Project Goals](#project-goals)
        - [User Goals](#user-goals)
        - [User Expectation](#user-expectation)
        - [User Stories](#user-stories)
  - [1.2. Skeleton](#skeleton)

 [2. Features](#features)

 [3.Technologies used](#technologies-used)

 [4.Testing](#testing)

 [5.Bugs](#bugs)

 [6. Deployment](#deployment)

 [7. Acknowledgement](#acknowledgement)

 <a name="ux"></a>
# 1. User Expereince (UX) design
 [Go to top](#table-of-contents)

 This blog website will provide information to user: how many online stores are there. Which includes information regarding these stores. This website will provide information about delivery providers. How many of global delivery providers are there. How they make sure that your parcel will be dillevered safely. 
  
 It will explain about payment methods. How many ways are there to buy product online. Multiple payment are added in the blog site. if user know any he can add it.

 <a name="strategy"></a>
 # 1.1. Strategy
  [Go to top](#table-of-contents)

 <a name="project-goals"></a>
  ### Project Goals

 The main goal of the project is to allow CRUD system to user. User can resgister to website. User can view other people blog. 
 User can login logout at any time. The Blog site is responsive and eye catching.

 <a name="user-goals"></a>
 ### User Goals:

 * User can add Blog Post
 * User can Edit Blog Post
 * User can delete Post
 * User can Comment on blog post
 * User can like Post
 * User can Add Category

 <a name="user-expectation"></a>
  ### User Expectations:

  * User should be able to register to website
  * User should be able to Login/Logout to the website
  * Website should be responsive
  * User should be able to contact with the autorities

 <a name="user-stories"></a>
 ### User Stories

 Throughout the project I used the GitHub projects board to log all user stories as my project management tool. This helped me keep focus on the necesarry tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed.

 ![User Stories Issuess](media/issuuess.JPG)

 <a name="skeleton"></a>
 # 1.2. Skeleton
  [Go to top](#table-of-contents)
 
 ### Wireframes

 ### Home 
 ![Desktop Version](media/Home.PNG)

 ### Add Blog 
 ![Desktop Version](media/AddBlog.PNG)

 ### Add Category 
 ![Desktop Version](media/AddCategory.PNG)
 
 ![Desktop Version](media/Recent-Post.PNG)
 ### AddBlog
 ![Desktop Version](media/Mobile-AddBlog.PNG)
 ### AddCategory
 ![Desktop Version](media/Mobile-AddCategory.PNG)
 ### HomeMobile
 ![Desktop Version](media/Mobile-Home.PNG)
 ### signIn Page 
 ![Desktop Version](media/Mobile-SignIn.PNG)
 ### SignOut Page
 ![Desktop Version](media/Mobile-Signout.PNG)
 ### SignUp page
 ![Desktop Version](media/Mobile-Signup.PNG)
 
 <a name="features"></a>
# 2. Features
 [Go to top](#table-of-contents)
 
 * Authentication is a key feature of the project
 * Authorization is also implemented
 * Only authorized user can add, update delete the blog or category
 * Dropdown on the category is palced so that each category can be views separatley

 ### HomePage
 Home page is designed using material design boots bootstrap. A jumbotron is placed right after the header. After the Jumbotorn a craousel is displayed which is also being designed by the material design bootstrap.

 After the craousel list of the blog is displayed. Total 6 post is being shown on the home page then a paginator is used to move items to the next page. This is a requirement by the codeinstitute. 


 ![feature-Home](media/feature-Home.JPG)
 ![feature-Home2](media/feature-Home2.JPG)

 ### Post detail

 Post detail page open when user clicked on the post. Where description of the post is being shown. On this Page user can add comments and like the post. Also delete and update button is shown so that user can update or delete the post.  

 ![post_detail](media/post_detail.JPG)


 ### Category View
  Catgegory are displayed as dropdown. multiple category are sown in the dropdown. you can click any of them to see what this category about. And You can your own category if you want and enlighten us with your knowledge.

  ![cat-1](media/cat-1.JPG)
  ![cat-2](media/cat-2.JPG)
  ![cat-3](media/cat-3.JPG)

 ### Add Blog / Category

 Django class is used to render the form on page. material design bootstrap is used to beautify the page. While adding the blog user have to select the category in which category he is adding the blog.

 ![Add-Blog](media/Add-Blog.JPG)
 ![Add-Category](media/Add-Category.JPG)


 <a name="technologies-used"></a>
# 3. Technologies Used
 [Go to top](#table-of-contents)

 * Python
 * Javascript
 * HTML5
 * CSS
 * mdboostrap 4
 * Google Fonts
 * Postgresql
 * Balsamiq
 * GitHub

 <a name="testing"></a>
# 4. Testing
 [Go to top](#table-of-contents)

 ### Manual Checking
 
 While developing the app i have tested each and every page, url and view. I was also pylint in my editor since most the is in python. pylint gives me red or yellow lines according to the error which i solved while developing.

 During learing the course instructor told that django is MVT. If you want to create something you have to follow this procedure. So this technique help me alot to keep checking the flow. 

 On the other hand Oline tools Were also to check the code. for example in order to check html W3C was used. In order to check CSS Jigsaw was used to check PEP8 was along with pylint which was already installed in my editor.
 
 
 ## W3C
 W3C didin't help much in Check the code since python django synatxt is there.

 ## Jigsaw
 Jigsaw was used to check the css the error if there were any.

 ![Add-Category](media/css-check.JPG)

 ## PEP8
 PEP8 was used to check python code validation

 ![pep8-1](media/pep8-1.JPG)
 ![pep8-2](media/pep8-2.JPG)
