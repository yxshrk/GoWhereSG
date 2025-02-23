Distinctiveness and Complexity.

The web application serves as an itinerary planner for Singaporeans to be able to find activities to do over the weekend. People are often left wondering about how they can spend their time on the weekends
in a meaningful manner that ensures that their time is utilized properly. When users log in to the web application, they are brought to a homeapage that allows them to start planning their itineraries by bringing them
to a category selection page. The two categories listed are Productivity and Leisure because this would allow people using the website to strike a good balance between completing important tasks
such as work or errands alongside setting aside time to relax. The website is not a social network as users are not able to see what others are doing and the content in each user's session is unique.
Users are brought to pages that suggest activities for them to participate in, in both the productivity and leisure categories. These are based on past selections users have made, and if a user removes the activity from their personal itinerary
it is removed from the suggestions page. From the productivity or leisure suggested activities page, users can choose an activity by clicking on the view button that gives them the option to
add the activity to their general itinerary that appears under the section titled "Recently Added Activities". They are also allowed to add any remarks if they want to make a note of whether they like the activity.
Under the suggested activities page, only the superuser is allowed to edit activities alongisde creating activities. Other users can choose to add remarks for suggested activities and add them to their general itinerary
to edit. Once a user has added the activity to their general itinerary, they are brought to the recently added activities page where they can view the added activities. In this page, they have the option to
remove the activity from their general itinerary if they change their mind, or they can choose to add it to their final personal itineraries that are categorised based on Productivity or Leisure as well.
There is a button available for them to add the activities to their itinerary after editting them or they can choose to leave the activity as it is and submit it to their personal itinerary.
Under their personal itinerary page, users are allowed to edit their activities, add remarks and create their own activities by rendering a form on the page. They can remove the activities from their
personal itinerary as well that would remove the activity from their suggested page as well. All pages have a paginator attribute for users to scroll through multiple activities on different pages.
Finally, there is a maps page in the web application that allows users to use an embedded dynamic map to search for places, find movie timings online and book tickets for leisure activities
at Singapore's Sentosa Island. It is mainly for users to plan their leisure activities but they can also use the map to search for cafes, offices or stores to do their productive activities.


In the views.py file, all the functions required to run the application are contained. This ranges from functions that asynchronously fetch data from forms to update the database with new activities or editted activities,
to functions that render the different pages. The general itinerary page is created using a watchlist model unique to each user that selects activities from the overall Productivity model that contains all activitiies.
The personal itinerary page is rendered by filtering activities by user and category, as reflected in views.py. The categories.html page allows users to make a selection of the category from which they want to view
suggested activities and the category.html page filters activities by category. The createactivities.html page allows the superuser to add new suggested activities for users that can be accessed by him/her only.
The index.html page serves as the homepage from which users can get started on creating their activities. The itineraries.html page serves as a selection page for users to select which
personal itinerary they would like to view according to the categories. The itinerary page renders the specific activities that fall under the specific category referenced. The recentlyaddeditems.html page shows the general itinerary
consisting of activities in the general itinerary before they are added to the personal itinerary. The view activity page allows users to add activities to their general itinerary and add remarks, while the review_personal.html page
allows users to edit activities as well before adding them to their personal itineraries alongside removing activities from their general itinerary. The view activity 2 html file allows users to remove activities from their personal itinerary alongside editting them and
adding their own remarks.

Network.js is a javascript file that contains the code required to asynchronously load forms and post data to update the activities database. Javascript is also contained in the html files with functions such as the
datetimepicker and asynchronous toggling of forms being implemented. The maps html page uses javascript to load the map with an API and provide an input to the map when the user is searching for a place using the search box.
The application is mobile responsive as well due to the css styling of the elements on the pages.