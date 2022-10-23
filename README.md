# Nature Scents
## Bring the aroma of nature into your home ✨
<br>
<img src="supporting_docs/design/am-i-responsive.png">
<br>
<br>

### A Full-stack Django-based E-commerce store with products that fill your home with the scents of the natural world, bringing calm, and brightening your day.
<br>
<br>

[]live link
<br>
<br>

## User Experience(UX)

### Strategy Plane
Target Audience:

- People aged 16-55
- Users who like natural scents
- Users who want to improve their home space
- Users interested in health, nature and natural products
- Users who want to regularly receive new products through subscription 

The user can purchase <strong>one off items</strong> on the site, which makes the site useful to anyone who visits looking to purchase a product. The site also offers <strong>product combination bundles</strong> for users who want to try out a range of products, possibly buy as gifts etc. The final option for users is to purchase a <strong>yearly membership</strong> where they will be <strong>'sent a new scent'</strong> every month from the essential oils product section. This yearly subscription keeps the user engaged with the site, and may also lead to further purchases. 

This e-commerce site is a B2C model. The goal of the site is to not only make one off sales but to encourage brand loyalty through subscription and a newsletter. The site uses minimal design, and a no frills up front approach to let the products speak for themselves.

### Strategy Roadmap

|                          Feature                                | Importance | Feasability |
| ---------------------------------------------------------------- | ------ | ----- |
| User can view a list of all products  | 5 | 5
| User can see a detailed view of selected product | 5 | 5
| User can add products to shopping bag and view bag | 5 | 5
| User Account Sign-up and Login | 5 | 5
| User Profile Page | 5 | 4
| User can edit their profile | 5 | 5
| User can delete their profile | 5 | 5
| User can recover a password | 5 | 5
| User can filter products by key word | 4 | 4
| User can purchase products using STRIPE payment | 5 | 5
| User can see reviews from other customers | 3 | 3
| User can see number of items in shopping bag with nav icon | 3 | 3
| Site owner can add products | 5 | 5
| Site owner can edit a product | 5 | 5
| Site owner can login to admin to edit products/approve users | 5 | 5

### User Stories
------

**Common user stories**:

- As a **user** I want to access the site on all screen sizes **so that I have** a seamless shopping experience
- As a **user** I want to easily understand the site navigation **so that I can** find what I need easily
- As a **user** I want to the site to have no broken links **so that I have** an uninterrupted experience

**Products**
- As a **user** I can filter products **so that I can** narrow down my search
- As a **user** I can view products **so that I can** add them to my shopping bag
- As a **user** I can view a detailed description of a product **so that I can** make a decision about purchasing it
- As a **user** I can select the quantity of a product **so that I can** add required amount to my order

**Basket**
- As a **user** I can add items to my shopping bag **so that I can** create a shopping bag of items to purchase
- As a **user** I can view my shopping bag **so that I can** review my purchase and add/edit as required
- As a **user** I can see a running total in my shopping bag **so that I can** see how much I am spending
- As a **user** I can process a payment **so that I can** pay for my order and receive confirmation

**User Account/Profile**
- As a **user** I am prompted to sign-up for an account **so that I can** benefit from having a profile and selecting a subscription
- As a **user** I can register for an account and login **so that I can** view my order information
- As a **user** I can see if I'm logged in or not **so that I can** login or logout
- As a **user** I can save my default shipping/billing details **so that I can** save time on my next visit
- As a **user** I can sign-up for for a scent subscription  **so that I can** receive new products each month

**Admin**
- As an **admin** I can login to Django administration **so that I can** access the site's backend
- As an **admin** I can add products to the site **so that I can** keep the site up to date and make products available to customers
- As an **admin** I can edit products/create sale items **so that I can** keep the site fresh and offer deals to customers
- As an **admin** I can make custom subscription products **so that I can** attract brand loyalty

**Marketing and SEO**

- As an **admin** I implement SEO keywords and meta tags **so that I can** attract customers and push my site up search engine listings
- As an **admin** I have created a Facebook Business Page **so that I can** increase my customer base
- As a **user** I can sign-up for a newsletter **so that I can** keep in the loop about new products/offers


## Scope Plane
-----------
In order to achieve the goals of the site owner and customer, the following features will be included in this release:

- Landing page with hero image 
- Responsive navbar that will navigate to the various pages throughout the site
- Shop page, that displays all products with the option to filter product category.
- Register/login feature using Django AllAuth so that users can create an account.
- Account page so logged in users can update their details, and see previous orders
- Custom 404 error page

## Structure Plane
-----
<br>
<br>

### Data Schema
<hr>
<br>
<img src="supporting_docs/flow/nature-scents-schema.png">
<br>

**Site flow**

<img src="supporting_docs/flow/guest-user.png">
<br>
<br>
<img src="supporting_docs/flow/authenticated-user.png">
<br>
<br>
<hr>
<br>

**Apps**
<br>

- <strong>Home App</strong>
<br>
The Home App contains the templates for the home page, subscription page and philosophy page. It is a simple app that exists with views, and urls to render these pages on the website.
<br>

- <strong>Products App</strong>
<br>
The Products App is the main hub of the site, where all users are drawn in order to view products, see them in detail and add them to their shopping cart. The app contains two models: The <strong>Product</strong> model and the <strong>Category</strong>
model. There is a product detail view linked to a product detail template so that users can clic into an individual product and see further details about it, and if they decide add it to their shopping cart.
<br>
Site owners have the ability to add products to the database from the frontend using the add_product view, they can also edit or delete poroducts from the database, using the edit_product, and delete_product views respectively.
<br>
<br> 

## Current state of custom models:
<hr>

I have two custom models in the Products App, Review and mood. As detailed in the issues section the Review model and it's application are still showing bugs. The intention of the Mood model is to seperate products into different moods e.g. Calming, Energising. Depending on their mood a symbol can be displayed beside the product. Unfortunately I have ran out of time to implement this fully in the projects current form.

- <strong>Shopping Cart App</strong>
<br>
The Shopping Cart App has 4 views, cart, add_to_cart, adjust_cart and remove_from_cart. The cart view renders the contents of the users shopping cart into the cart template. The other 3 views allow the user to either add to their cart, adjust the quantity of the product in question or if they change their mind they can remove products from their cart..
<br>

- <strong>Checkout App</strong>
<br>
The Checkout App consist of two models, Order and OrderLineItem. This app's function is to take what is in the users shoppign cart and enable them to go through the process of payment and order completion.
<br>
The Order Line Item model has a Foriegn Key to product, and order. It captures the product, quantity and price of the items in the users shopping cart.
<br>
The Order model contains all the users' shipping/billing details, contact details etc. It has a Foreign Key to the User_Profile model, and captures the total cost of the order, also calculating if the customer has hit the free delivery threshold of €50. It also contains information regarding the payment, the stripe PID and has an original cart field to be sent to the admin.
<br>

- <strong>Profile App</strong>
<br>
The Profile App allows authenticated users to see 2 things about their account. Firstly they are able to see their default address/contact details for orders, using a Form called UserProfileForm. When they are logged in ans go to checkout their default information prepopulates the checkout form which makes for a better user experience. The second thing they are able to access from this app is a run down of their order history, with unique id that is generated from the checkout app. It contains one model, UserProfile.
<br>

- <strong>Newsletter App</strong>
<br>
The Newsletter App has one model NewsletterInput, with an email field. This app links to a frontend input positioned in the footer of the site, which enables users to enter their email to sign-up for news updates, special offers etc.


## Skeleton Plane
----------

**Mobile View Wireframes**
<br>
<br>
<img src="supporting_docs/wireframes/homepagemobile.png">
<br>
<br>
<img src="supporting_docs/wireframes/philosophymobile.png">
<br>
<br>
<img src="supporting_docs/wireframes/productpagesmobile.png">
<br>
<br>
<img src="supporting_docs/wireframes/shoppingcartmobile.png">
<br>
<br>
<img src="supporting_docs/wireframes/checkoutmobile.png">
<br>
<br>
<img src="supporting_docs/wireframes/subscriptionmobile.png">
<br>
<br>
<hr>
<br>

**Desktop View Wireframes**
<br>
<br>
<img src="supporting_docs/wireframes/homepagedesktop.png">
<br>
<br>
<img src="supporting_docs/wireframes/philosophydesktop.png">
<br>
<br>
<img src="supporting_docs/wireframes/productpagesdesktop.png">
<br>
<br>
<img src="supporting_docs/wireframes/shoppingcartdesktop.png">
<br>
<br>
<img src="supporting_docs/wireframes/checkoutdesktop.png">
<br>
<br>
<img src="supporting_docs/wireframes/subscriptiondesktop.png">
<br>
<br>

## Surface Plane
-------------

**Colour Scheme**
<br>
<br>
<img src="supporting_docs/design/colourscheme.png">
<br>
<br> 
I have chosen this colour scheme as it is a combination or warm and calming tones which I feel matches the mood of the site, and the products on offer. The pink and orange contrast well with the darker blue and grey tones. 

**Fonts**
<br>
<br>
<img src="supporting_docs/design/fonts.png">
<br>
<br>
I chose Josefin Sans as the main font on the site, as it is simple and clean. I combined this with the Cardo font.
<br>
<br>
<img src="supporting_docs/design/fonts2.png">
<br>
<br>

**Images**
<br>
<br>
All images were found on [Pexels](http://www.pexels.com/)
<br>
<br>
Sources are as follows:
<br>
Photos by Meruyert Gonullu

Photos by Tara Winstead

Photos by MART PRODUCTION

Photoss by Monstera from Pexels 

Photos by Alesia Kozik from Pexels

Photos by EKATERINA BOLOVTSOVA from Pexels

Photo by Dominika Roseclay from Pexels


## Project Planning/Agile
<br>
I have utilised Github's projects section to create a project board with issues in the planning and implementation of the project.

The project board can be found [here] (https://github.com/users/kreilly86/projects/4)
<br>

## Features

### Existing Features
<br>
<hr>

 ### Navigation

<br>
<strong>Main navigation</strong>
<br>
<br>
<img src="supporting_docs/design/main-nav.png">
<br>
The main navigation is fixed to the top of the page, with a simple logo, a menu, and three icons which link to account functionality, a search bar and the shopping cart. The shop title on the menu bar is a drop down where the user can select what product category to open and browse.
<br>
<br>
<strong>Mobile navigation</strong>
<br>
The mobile navigation containers a burger style menu, which drops down on the left side. 
<br>
<img src="supporting_docs/design/mobile-nav.png">
<br>
When the dropdown menu is clicked, the content is centered and easy to access.
<br>
<img src="supporting_docs/design/navbar-drop-mobile.png">
<br>
<br>
<strong>Search Bar</strong>
<br>
When the font awesome magnifiying glass is clicked on the navbar a search bar pops down. Users can search for keywords, and if they exisit within a product name/decription the results will be rendered.
<br>
<br>
<img src="supporting_docs/design/search-bar.png">
<br>
<br>

### Footer

<br>
<strong>Desktop Footer</strong>
<br>
The footer is simple and clean, with the background matching the nav bar. The footer contains a newsletter sign-up input, copyright information and social media icon links.
<br>
<img src="supporting_docs/design/main-footer.png">
<br>
<strong>Mobile/Tablet Footer</strong>
<br>

The footer contents stack on mobile and tablet view:
<br>

<img src="supporting_docs/design/mobile-footer.png">
<br>
<strong>Home Page</strong>
<br>

The home page contains a hero image with natural products and an H1 title with bootstrap class 'display-4'. It is follwed by a lead description expplaining to the user what the site is about, "Bring the aroma of nature into your home".
<br>

<img src="supporting_docs/design/homepage-top.png">
<br>

The bottom half of the home page contains a 'Shop' button to take users to the products page and below a bootstrap carousel of images showing the different category of productd available.

<br>
<img src="supporting_docs/design/homepage-carousel.png">
<br>

<strong>Philosophy Page</strong>
<br>
The Philosophy page is simple, with a short description of the company's ethos. It contains a striking image and bold title in white
<br>
<img src="supporting_docs/design/philosophy-page.png">
<br>

<strong>Subscription Page</strong>
<br>
The subscription page is similar to the Philosophy page in that is has a striking ikage and cold title in white. Below is a deacription of the yearly membership, which provides users with a monthly delivery of new 'scents' to their door. I have use a zoom effect on the images inspired by the Code Institute Love running club project effect. This brings a bit of life to the page. Users can then click on the more info button and the subscription product is displayed in the product detail template. From there they can add the product to their shopping cart.
<br>
<img src="supporting_docs/design/subscription-page.png">
<br>
<img src="supporting_docs/design/subscription-detail.png">
<br>

<strong>Products Page</strong>
<br>
Users can access the products page from the main nav bar by clicking 'Shop' and selecting a type of products, or 'all products'. This will filter the products into sections, with the all selection showing the titles of all the categories at the top of the page.
<br>
<img src="supporting_docs/design/products-page.png">
<br>
<img src="supporting_docs/design/shop-menu.png">
<br>
<img src="supporting_docs/design/all-products.png">
<br>

<strong>Product Detail</strong>
<br>
When a user clicks on one of the products they are taken to the product detail page. This displays an image of the product, a description, the price, a quantity selector, and an add to cart button. Once the user clicks on add to cart they see a bootstrap success message pop up. Otherwise they can can click on keep shopping to be taken back to the products page, which shows all products.
<br>
<img src="supporting_docs/design/product-detail-page.png">
<br>
<img src="supporting_docs/design/cart-success.png">
<br>

<strong>Cart Page</strong>
<br>
The cart page displays all items the user has addedd, displayed stacked in a bootstrap col-12 div. The user can click to delete the item from the cart, or edit the quantity. The total price is displayed including delivery, which is free over €50. The checkout button brings the user to the final step in the process.
<br>
<img src="supporting_docs/design/cart-view.png">
<br>

<strong>Checkout Page</strong>
<br>
The checkout page contains a simple form, with address details, and a card input box made using Stripe. Once the users enters all information they are given a warning of how much they will be charged before proceeding. There is also a checkbox if logged in users would like to save their address details for future purchases. When the payment is processed the user is shown a success pop up, and message thanking them for their order.
<br>
<img src="supporting_docs/design/checkout-page.png">
<br>
<br>
<img src="supporting_docs/design/card-charge.png">
<br>
<br>
<img src="supporting_docs/design/thank-you-order.png">
<br>

<strong>Profile Page</strong>
<br>
The profile page displays the users billing/shipping details, along with a list of previous orders. The user is able to update their shipping info by clicking the 'Update Information' button.
<br>
<img src="supporting_docs/design/profile-page.png">
<br>

<strong>Admin</strong>
<br>
When the site admin is logged in they are able to add, edit, or delete products to the database from the Frontend. 
<br>
<img src="supporting_docs/design/admin-orders.png">
<br>
<img src="supporting_docs/design/product-management.png">
<br>

### Future Features
<br>
<br>
- I would like to extend the store product base
- The site could also benefit from further information on the ingredients used in the products, perhaps a blog with useful articles an customer interaction
- A display on the shopping cart alerting the user to how many items they have in their cart

## Marketing and SEO
<br>
<br>

I have created a (Facebook business page)[https://www.facebook.com/nature.scents.irl]
<br>
<br>
<img src="supporting_docs/design/facebook.png">
<br>
Keywords have been used in meta tags based in the base.html file. I have kept the site simple, and didn't overcomplicate this process with lengthy descriptions.
<br>
<br>

## Issues
<br>
<br>
The Django Secret_Key was accidentally pushed to git hub, this has been changed and secured in an env.py file. 
<br>
<br>

### App Checkout:
<hr>
<br>
As I had not implemented a free delivery threshold, the postage charges generated for orders were quite excessive. e.g. €14. I changed this by creating a free delivery threshold of €50 in settings.py
<br>
<img src="supporting_docs/design/delivery-cost.png">
<br>

### Issue with Stripe Credit card input box when deployed to Heroku
<hr>
<br>
During testing I came up across an issue with the checkout page, specifically the credit/debit card input box. When running locally it was showing up as expected, but on Heroku it was a blank input with no way to input card details. I had various stages of trying to resolve this issue with Tutor Support:
<br>
<img src="supporting_docs/flow/stripe_element.js-load-fail.png">
<br>
- I first tried to remove the DISABLE_COLLECTSTATIC variable from the config vars in Heroku, and re-deploy the site. This didn't work and gave activity feedback of : '$ python manage.py collectstatic --noinput'
<br>
- I noticed that I had installed whitenoise early on in the project to process the static files for Heroku, but since switching over to AWS I had forgotten to remove this package from settings and uninstall. I tried doing this but it still didn't give me the result I needed.
<br>
- I checked to make sure static files were being served by AWS and they were:
<br>
<img src="supporting_docs/flow/AWS-static.png">
<br>
- I then realised a setting in my settings.py could have been causing the issue,I compared it to the Boutique Ado code and changed it, but it still didn't fix the issue
<br>
<img src="supporting_docs/flow/incorrect-settings.py.png">
<br>
- Finally, with the help of tutor support we discovered there was a clash with a previously installed Django plug-in called 'fontawesomefree'. I removed this package, and the stripe input worked as intended in the deployed Heroku version.
<br>

### Issues with image files loading
<hr>
<br>
Throughout the project I had issues with images not rendering, mostly this was due to incorrect url format. In the example below I was not using the correct Django url tags:
<br>
<img src="supporting_docs/design/logo-fail.png">
<br>
<br>
<img src="supporting_docs/design/incorrect-url.png">
<br>
<br>
Once I chaged this to '{{ MEDIA_URL }}nature-logo.png', the logo loaded correctly.
<br>
<br>

### Review app
<hr>
<br>
I have used a youtube tutorial, found here: https://www.youtube.com/watch?v=eIN1nZCt7Ww to create a custom review model for products. This is a form on the front end in the product_detail page. I have set up the models, urls, views and made a template on the product detail page but am receiving an error when I test the review:
<br>
<img src="supporting_docs/flow/test-review.png">
<br>
<img src="supporting_docs/flow/error-msg-review-1.png">
<br>
<img src="supporting_docs/flow/error-msg-review-2.png">
<br>
<br>

### Technologies Used
<br>
<hr>

Python - This project uses Python as its' core language
Django - This project is built with the Django framework
Bootstrap - Bootstrap is used throughout the site to add style, and responsiveness to the site
GitHub - Used to store code for the project
Git - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
Gitpod - Used as the development environment.
Heroku - Used to deploy and host the final application.
Google Fonts - Used for website fonts
Google Developer Tools - I used google developer tools throughout the build process to test the site, fix issues etc
Font Awesome - Used for navigation icons and social links
SQLite - Was used to run the project localy
AWS - Amazon Web Services S3  was used to host static files
PostgreSQL - Heroku's PostgreSQL was used to store data of the deployed site
Stripe- For payment processing
Balsamic - Used for wireframe drawings and planning

### Code Validation
<br>
<br>
- W3C Mark-up Validation
- W3C CSS Validtion
- Lighthouse
- Pep 8

<br>

### Deployment
<hr>
<br>

#### Local Deployment 
<br>
<br>

I used Github and Gitpod to build and run this project locally. The repositiory was built using Code Institute's template:

Found [here](https://github.com/Code-Institute-Org/gitpod-full-template)

<br>
Steps:

- Click the Use This Template button in the github repository menu
- Create your own repository name, and description
- Click the Create Repository from template to create repository
- Click Gitpod to open the development environment workspace for the new respository
- Use this workspace each time, rather than repeat above steps, to ensure any installed dependencies are accessible each time
- Use git to add commit messages and push regularly to keep track of progress:
<br>
- git add . (adds all modified files to a staging area)
- git commit -m "Insert explanation of commit here": commits all changes to the repository
- git push: pushes all committed changes to your Github repository.
<br>
For this project I didn't use the fork or clone option in GitHub, but these are useful tools. If you want to make changes without affecting the code already pushed you can clone the workspac to work on your repository and 'test' out code and changes. On reflection this would have been a useful tool rather than making changes to the original, and sometimes getting a bit lost as to how any changes were made on one sitting. 
<br>
<br>

#### Heroku Deployment
<br>
<br>

Steps to Deploy to Heroku:
<br> 
* Note Ensure debug mode is FALSE in final deployment to ensure project security
<br>

Sign into Heroku account and select create a new app.
<br>
<img src="supporting_docs/flow/heroku-part1.png">
<br>
Choose app name and select Europe region, click create app
<br>
<img src="supporting_docs/flow/heroku-part2.png">
<br>
In local GitPod environment at project level create a Procfile with the following: web: gunicorn *project name here *_database.wsgi
<br>
<img src="supporting_docs/flow/heroku-part3.png">
<br>
Click on resources tab in Heroku, and add-ons and select Heroku Postgres
<br>
<img src="supporting_docs/flow/heroku-part4.png">
<br>
Click Settings tab and select reveal Config Vars
<br>
<img src="supporting_docs/flow/heroku-part5.png">
<br>
Copy DATABASE_URL value to an env.py file in GitPod (os.environ["DATABASE_URL"] = 'insert value here'), and also create a SECRET_KEY here which is added as a key and value in confing vars on Heroku.
<br>
When ready to deploy under deployment tab Select Github as deployment method and type in repository name of project
Click search and hit connect on repository name
Next hit deploy branch, and you will see "your app has been deployed", click on link to go to the deployed project
<br>
<img src="supporting_docs/flow/heroku-part6.png">
<br>

## Credits 
<br>
<br>
Code and structure for this e-commerce site has largely come from Code Institute's Boutique Ado walkthrough project: 
<br>
https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/9ed36dc2c07228041b56b28174dd96ee56e6c59a
<br>
My mentor Simen Daehiln for encouragement and help with project planning and implementation.
<br>
Code Institute Tutors for technical help on many occasions!
<br>

