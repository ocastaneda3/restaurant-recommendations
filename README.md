## CPSC 362 - Software Enginerring
![PyPI](https://img.shields.io/badge/Python-v3.7.2-informational.svg) 
![PyPI](https://img.shields.io/badge/pip-v20.1-informational.svg)

### Problem Domain:
We are a software development startup whose market is to provide on demand and predictive ordering of services for customers.  When a customer comes to a lounge, relaxing area in companies, businesses, campuses, or restaurants, we want to provide a service to them.  Ideally this is through a mobile app, and we can target specific services to customers based on what they’ve ordered previously, or specials in the area.

### Solution:
You are going to develop a system that satisfies this problem domain.  You will develop and architect a system to support ordering, predictive advertising, analyzing previous orders/habits.

------

### Required Libraries:
#### [Simple Smart Pipe](https://pypi.org/project/sspipe/)
> SSPipe is a python productivity-tool for rapid data manipulation in python.<br><br>It helps you break up any complicated expression into a sequence of simple transformations, increasing human-readability and decreasing the need for matching parentheses!
```
$  pip install sspipe
```

#### [Requests](https://pypi.org/project/requests/)
> Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
```
$  pip install requests
```

#### [Geocoder](https://pypi.org/project/geocoder/)
> Many online providers such as Google & Bing have geocoding services, these providers do not include Python libraries and have different JSON responses between each other.<br><br>
It can be very difficult sometimes to parse a particular geocoding provider since each one of them have their own JSON schema.<br><br>
Here is a typical example of retrieving a Lat & Lng from Google using Python, things shouldn't be this hard.
```
$  pip install geocoder
```

------

#### Expected Output
<dd>Using Location [33.8353, -117.9145]</dd>
```command
$ python main.py
New Incoming Orders:
-------------------
Request ID:     KM0RS73ES
User ID:        157786422
Restaurant:     Chipotle Mexican Grill
Item:           Steak Burrito Bowl Combo
Price:          $9.61


Analyzing . . .


Recommendation:
Restaurant:     Don Pancho's Taquiza
Item:           Cheese Quesadilla   

New Incoming Orders:
-------------------
Request ID:     TEHRW92UH
User ID:        364804147
Restaurant:     Popeyes
Item:           Spicy Chicken Sandwich Combo
Price:          $8.31


Analyzing . . .


Recommendation:
Restaurant:     Sonic Drive-In
Item:           Bacon Ranch Monster Taco

New Incoming Orders:
-------------------
Request ID:     HSULLOJ7Y
User ID:        209641492
Restaurant:     Five Guys Burgers & Fries
Item:           Cheeseburger
Price:          $10.85


Analyzing . . .


Recommendation:
Restaurant:     In-N-Out Burger
Item:           Turkey Salad   

New Incoming Orders:
-------------------
Request ID:     5RUXUAS43
User ID:        854235124
Restaurant:     Chick-fil-A
Item:           Chick-fil-A Chicken Sandwich Combo
Price:          $8.35


Analyzing . . .


Recommendation:
Restaurant:     Five Guys
Item:           Little Cheeseburger

```
