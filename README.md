### Problem Domain:
We are a software development startup whose market is to provide on demand and predictive ordering of services for customers.  When a customer comes to a lounge, relaxing area in companies, businesses, campuses, or restaurants, we want to provide a service to them.  Ideally this is through a mobile app, and we can target specific services to customers based on what they’ve ordered previously, or specials in the area.

### Solution:
You are going to develop a system that satisfies this problem domain.  You will develop and architect a system to support ordering, predictive advertising, analyzing previous orders/habits.

### Required Libraries:
#### [Simple Smart Pipe](https://pypi.org/project/sspipe/)
> SSPipe is a python productivity-tool for rapid data manipulation in python.<br><br>It helps you break up any complicated expression into a sequence of simple transformations, increasing human-readability and decreasing the need for matching parentheses!
```python
pip install sspipe
```

#### [Requests](https://pypi.org/project/requests/)
> Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
```python
pip install requests
```

#### [Geocoder](https://pypi.org/project/geocoder/)
> Many online providers such as Google & Bing have geocoding services, these providers do not include Python libraries and have different JSON responses between each other.<br><br>
It can be very difficult sometimes to parse a particular geocoding provider since each one of them have their own JSON schema.<br><br>
Here is a typical example of retrieving a Lat & Lng from Google using Python, things shouldn't be this hard.
```python
pip install geocoder
```
