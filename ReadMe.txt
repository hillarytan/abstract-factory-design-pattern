Hello!

This project is a search algorithm designed using Django.

Prerequesites:

Download python
Get the python extension 
To install pip: py -m ensurepip --upgrade
To install django: pip3 install Django
To install beautiful soup: pip install beautifulsoup4
To install requests: python -m pip install requests

to run:
make sure you are in the "Data-project" directory
in your terminal type: "py manage.py runserver"
click on the link while holding control



Once you run the web application you will be directed into the main page.
from here you can either enter a string in the search box and hit the search button, 
or you can visit the universities page on the top right corner.

In case you went with the former, you will be directed into the search page.

the purpose of this project is to help students in Lebanon to find universities
where they can study their major.

if a student provides the search box with "Computer engineering", it will return 
a table containing several universities indicating whether they have computer engineering
as a major or not. The search can also provide a cost per credit for the major if available.

We designed the web application using the abstract factory design pattern.
Where the universisites are the factories and their products are the majors and tuition fees.

To gather data, we used web scraping and stored the information in lists.