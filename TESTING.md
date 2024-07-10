# **RE.view API - Testing**

## **Table of Contents (Testing):**

1. [**Testing Overview**](#testing-overview)
1. [**Testing Throughout Development**](#testing-throughout-development)
   - [**Manual Testing**](#manual-testing)
   - [**Automated Testing**](#automated-testing)
   - [**Noteworthy Bugs During Development**](#noteworthy-bugs-during-development)
1. [**Product Development Testing**](#product-development-testing)
   - [**Code Validation**](#code-validation)
   - [**Unresolved Bugs**](#unresolved-bugs)
1. [**User Story Testing**](#user-story-testing)
   - [**Navigation & Authentication**](#user-stories-navigation--authentication)
   - [**Creating & Editing Products**](#user-stories-creating--editing-products)
   - [**Viewing Products**](#user-stories-viewing-products)
   - [**Likes and Dislikes**](#user-stories-likes-and-dislikes)
   - [**Reviews**](#user-stories-reviews)
   - [**Profiles**](#user-stories-profiles)

## **Testing Overview**

Here, I have documented the testing procedures performed throughout the development of this repository's code.

For details on front-end testing, please refer to this project's [**_front end repository's TESTING.md document_**](https://github.com/emmacadavra/RE.view-react/blob/main/TESTING.md).

## **Testing Throughout Development**

### **Manual Testing**

During the development process, I employed various methods to test my API code iteratively. Notably, I used numerous print statements to pinpoint exactly what code was being passed from one section to another and to identify issues when things didn't work as intended. Using a print statement at each step of the code's journey, in some cases, greatly enhanced my understanding of how data flows between functions, models, and views.

While writing the API code, it was common for me to run the `python3 manage.py runserver` command to see real-time results from the API, which helped identify errors or conflicts.

Since the API is mostly URL-based, I often tested URL paths by entering incorrect URLs or logging out/in as different users to ensure error handling was working correctly.

When working with both the back-end and the front-end, I kept my local server running even when the front-end accessed the deployed API, allowing me to cross-reference the returned objects in each API call with what I expected to receive in my React app.


### **Noteworthy Bugs During Development**

As the largest and most complex project I have worked on to date, I encountered numerous bugs throughout development. Some issues arose from using newer versions of frameworks than I was accustomed to, while others stemmed from incorrectly connecting models to views or improperly configuring serializers. Additionally, although I had experience with Django, I was new to Django REST at the start of this project, leading to several misunderstandings of expected behavior.


Below are some of the noteworthy bugs I encountered during the development process.



#### Likes and Dislikes + Like_Review

I encountered several bugs while implementing Likes and Dislikes. Initially, despite providing choices from the start which resulted in incorrect data being pulled through to the API. Once fixed, the likes and dislikes worked, but I had only included a single 'count' field in the product view, so I couldn't pull the counts for each type of like or dislike—only the total count. To fix this, I added individual count fields to the queryset.

Another bug related to likes and dislikes occurred when filtering products by those a user had liked or disliked. I still received all products in the list, regardless of whether or not I had liked or disliked them. This was due to incorrectly adding `likes__owner__profile` to the 'ordering_fields' in the product view, instead of the 'filterset_fields'.

Late in development, while testing the front-end like and dislike functionality, I discovered two more bugs. First, I was only collecting the like or dislike ID to send to the front-end, without linking it to the type. I resolved this by adding the product serializer field 'current_user_like_or_dislike' and defining the 'get_current_user_like_or_dislike' function to return an object containing both the ID and type.

Lastly, in the product view, I realized I had forgotten to declare 'distinct=True' for each individual like and dislike count. This caused a peculiar bug where a product with one like would show a like count equal to the number of reviews if the product had reviews, despite only one like being stored in the database. Adding 'distinct=True' to each like and dislike count fixed this.

Like_Review is the ability to like a review, and connects a count and an id to the review, this shall be expanded in the future with in the inclusion of a filter set which should filter the most liked reviews.

## **Product Development Testing**

### **Code Validation**

I used two resources to validate my Python code: the VSCode extension 'Flake8' and the [**_Code Institute Python Linter_**](https://pep8ci.herokuapp.com/#).

Most of this project's code passed without issues, and where there were issues, they were due to lines being too long. These occurred in my main settings.py file and some urls.py files. I found that it is advised not to shorten items in settings.py (especially where automatically set by Django), and there seemed to be no clean way to shorten some of the URLs in the url files.

Overall, my code adheres to PEP8 guidelines.

### **Unresolved Bugs**

To the best of my knowledge, there are currently no unresolved bugs in the code within this repository.

## **User Story Testing**
### Authorised user

- User story: Be able to sign in to my account
- Test : When signed out, I navigated to the navbar, as well as used links and buttons that are present across the site that push vistors to the sign in page, and filled the form to sign in
- Result : Entered my details and clicked the submit button to be redirected to the  home page. In subsequent visits, the form auto-filled the sign in fields which as a user made my life easier
- Verdict : Test passed


- User story: Follow or unfollow another account
- Test: Navigated to a profile page account and pressed follow and unfollow
- Result: The function captured the click which increased and decreased followers and following count 
- Verdict: Test passed

- User story: Like or dislike another post
- Test: Navigated to a unique post which I didn't own and liked and unliked a post
- Result: The like count increased and decreased
- Verdict: Test passed


- User story: Can't like/dislike my own product
- Test : Navigated to a unique product that I own and clicked the like/dislike icon
- Result: The like ignored my request as I own the product. A Tooltip message is flagged to the user informing them it's not possible to like/dislike one's own product
- Verdict: Test passed

- User story: Review on one's own product, as well as others
- Test: Navigated to my own product as well as another user's and submitted a comment
- Result: The review appeared in both cases
- Verdict: Test passed


- User story: View a list of products
- Test: Added test products and when to Productlist view URL to check they are displayed
- Result: Instances were displayed as intended
- Verdict: Test passed

