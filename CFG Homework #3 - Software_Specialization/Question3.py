"""
A

Simulate clicking around the CFG Website. Keep track of the URL changes and
print the current URL after each move.
● You will need to display the options for each link, and include an option for
‘Back’ if not on the Base URL.
● You do not need to worry about error handling
● You are recommended to keep the simulation going within a while True loop
so the logic keeps looping until an exit is forced.
You only need to consider the following URLs for your solution:
1. Base URL: https://codefirstgirls.com/
2. Category URLs: /courses ,/opportunities/
3. Sub-category URLs: /courses/cfgdegree/ , /opportunities/ambassadors/
"""

base_url = "https://codefirstgirls.com/"
current_url = base_url # Starting at the base url

while True:
    print(f"You are currently on the URL {current_url}\nWhere are you clicking?""")

    # Display options according to current URL
    # Homepage
    if current_url == base_url:
        print("Options: Courses, Opportunities")
    # Courses
    elif current_url == base_url + "courses":
        print("Options: CFGDegree, Back")
    # Opportunities
    elif current_url == base_url + "opportunities":
        print("Options: Ambassadors, Back")
    # CFGDegree
    elif current_url == base_url + "courses" + "/cfgdegree":
        print("Options: Back")
    # Ambassadors
    elif current_url == base_url + "opportunities" + "/ambassadors":
        print("Options: Back")

    user_choice = input().lower()

    # Update the current URL according to user choice
    if user_choice  == "courses" and current_url == base_url:
        current_url = base_url + user_choice
    elif user_choice  == "back" and current_url == base_url + "courses":
        current_url = base_url
    elif user_choice  == "cfgdegree" and current_url == base_url + "courses":
        current_url = base_url + "courses/" + user_choice
    elif user_choice  == "back" and current_url == base_url + "courses" + "/cfgdegree":
        current_url = base_url + "courses"
    elif user_choice  == "opportunities" and current_url == base_url:
        current_url = base_url + user_choice
    elif user_choice  == "back" and current_url == base_url + "opportunities":
        current_url = base_url
    elif user_choice  == "ambassadors" and current_url == base_url + "opportunities":
        current_url = base_url + "opportunities/" + user_choice
    elif user_choice  == "back" and current_url == base_url + "opportunities" + "/ambassadors":
        current_url = base_url + "opportunities"
    else:
        print("Your choice is invalid. Please start again.")
        break


"""
B
"""

"""
The time complexity is O(n) because we are printing phrases as long as we are looping.
We do not know how long we will be inside the loop because it depends on the user choice.
So time complexity is linear therefore O(n).

The space complexity is 0(1) since while when we are looping we are only saving constants
such as user_choice, base_url and current_url, which are strings.
So space complexity is constant therefore 0(n).

As for assumptions, we assume that the user_choice, the current and base URLs are single
strings and do not depend on functions or other data structures, being constants.
"""