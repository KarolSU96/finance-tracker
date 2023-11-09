# Django Finance Tracker

This is my milestone 4 project of the Code Institute Full Stack Web Development Course.
The goal of the project is to build a Full-Stack Web application using an MVC (Model-Template-View) framework.
Finance Tracker is a web applicaton for managing your financial expenses which utilises Django as a framework.

This tracker should provide everyone with a simple tool to plan their monthly budget or maybe a even their next vacation.


## UX 

The finance tracker has simple and easy to use design. The colour aesthetic and font work well together and have a modern aesthetic.
The pages are responsive and apporpriate for all devices. The functionality stays the same on both mobile and desktop.


### Design
Thanks to Bootstrap the pages stay responsive and look good on all devices.


### Typography
The font used throughout the application is Lato, which means summer in polish.
It's a sans serif typeface, designed in Summer 2010 by Lukas Dziedzic.
It has a fresh, aesthetic and is highly readable.

-[Lato](https://fonts.google.com/specimen/Lato?preview.text=Finance%20Tracker)

### User Stories

"As a user, I would like to**: ________"

- be able to sign up so thath I can have a personalized account on the website.
- create a plan by adding details such a  budget amount, plan name and description so that I can efficiently manage nad plan my budget.
- see a plans overview, including total budget, total spent and remaining balance, so I can make informed decisions about my finances at glance.
- open a specific plan, revealing a list of transactions so that I can gain insights into my spending patterns.
- add a transaction easily, specifying amount, category and description so that I can keep an accurate record of my spendings.
- add a new plan for a different month or puropse so that I can effectively track my budget across various time periods.
- delete transactions so that I mantail accurate financial records by removing innaccuracies.
- edit transactions so that I can reflect the changes in my spending patterns or bills.
- delete plans so that I keep the dashboard oranized removing unused or outdated plans.
- be notified about changes that I make to the transactinons and plans so that I have better awareness of the changes and enhanced user experience.


### Site Admin

"As a site administrator, I can :________"
- Access and analyze overall application data to monitor user activity, identify trends and encure the platform's optimal performance.
- Manage the categories by adding and deleting them to mantain a relevant and organized classification system for user transactions.


## Wireframes




## Features
1. User Authentication: 
- Secure sign-up, log-in and log out functionalities.
- Encures user data privacy and protection.

2. Plan Management:
- Create and delete financial plans efortlessly.
- Quick overview for existing plans.

3. Transaction Management:
- Add new transaction to plans, specifying the amount, category and description.
- Edit and delete transactions to maintain accurate financial records.

4. Category Management:
- Categorize transactions to track spending patterns.

5. User-Friendly Interface:
- Intuitive and responsive design for seamless navigation.

6. Alerts and Notifications:
- Notifies user for successfull actions (e.g., login, plan creation, transaction addition)

7. User-Friendly Forms:
- Easy-to-use forms for adding and editing transactions.

 
## Future Fratures
- Edit Plan  functionality
- Data Visualisation: Diagrams for displaying the patterns in spendings.
- Enchanced site styling

## Bugs

How great would it be to not be restrictedby time? Unfortunatley for us, 3 dimensional beings, the time flows and I didn't have enough of it to fix all the bugs. So here they are:
- SweetAlerts notifications taking a bit too much space on mobile. I tired numerous ways to style it differently but nothing has worked yet. In the docs it says that the width should be editable when we fire the swal as one of the properties of the object. Will defenitely fix this in the future when I have time.
- Plan table is a bit too big on some mobile devices. It still displays the informations nicely but sometimes the nuser needs to scroll a bit to the right, to see the plan description for example.

## Technologies Used
- HTML 5 for structuring the markup text
- CSS3 used for styling, altough most of the styling was done with Bootstrap
- JavaScript - used for displaying the notifications
- Django: Web framework for Pyhton
- Bootstrap: Front-end framework
- SweetAlert: Customizable alerts for better user experience
- Git Hub used for secure online code storage
- Codeanywhere used as a cloud-based IDE for developlment
  

## Testing

I planned and performed various tests to fix bugs and validated the HTML, CSS, JavaScript and Python code. Results can be seen below.

### HTML

I used the recommended [HTML W3C Validator](https://validator.w3.org) to validate my HTML files.

| Page | Screenshot | Passed / Notes |
| --- | --- | --- |
Homepage - index.html | ![Home Page](./documentation/home.png) | No warnings.


| --- | --- | --- |
Add Plan - add_plan.html | ![Add Plan Page](./documentation/add-plan.png) | There is a bug which shows that there is a h1 element in the line 40- couldn't find anything like this in my code.


| --- | --- | --- |
Plan details - plan_details.html | ![Plan Details Page](./documentation/plan-details.png) | 1 warning, possibly a bug, because I am aria-labeling the modal that has an attribute of aria-hidden.


| --- | --- | --- |
Edit Transaction Page - edit_transaction.html | ![Edit Transaction Page](./documentation/edit-transaction.png)| There is a bug which shows that there is a h1 element in the line 40- couldn't find anything like this in my code.

### CSS

I used the recommended [Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
![Jigsaw Validator](./documentation/jigsaw.png)
No errors. 216 warrnings that target bootstrap classes.

### JavaScricpt

I used the recommeded [JShint Vadalidator](https://jshint.com) to validate my JS file.
Two warnings about ES6, which can be ignored.
Swal is a SweetAlert variable.


### Python

I used the recommended [PEP8 Python Validator](https://pep8ci.herokuapp.com) to validate my Python Files.


### Lighthouse Testing


## Deployment
  1. Clone the Repository
  2. Navigate to Project Directory
  3. Intall Dependencies
  4. Configure Enviromental Variables
  5. Apply Database Migrations
  6. Run Development Server
  7. Access the Application

## Credits
- This web app uses Code Institute Full Template.
- SweetAlert for beautiful alerts
- Bootstrap team for making my life easier when it comes to styling of my page.