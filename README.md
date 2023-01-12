# Web Scraping Live Dashboard with Python and MongoDB

<div align="center">
    <img src=images/webapp.png>
</div>

## <div align="center">Use Python, MongoDB and HTML a Web-Based Dashboard that Scrapes Web Articles,</div>
## <div align="center">Images and Other Information in order to Display as a Live Feed</div>

<p align="center">
<a href="#goals">Goals</a> &nbsp;&bull;&nbsp;
<a href="#dataset">Dataset</a> &nbsp;&bull;&nbsp;
<a href="#tools-used">Tools Used</a>
</p>

# <div align="center">Goals</div>

She's really eager to create her application, and she has a list of websites she plans to use for scraping.

She's really excited about actually scraping live data. The script we're building is designed to scrape the most recent data—that means that each time we run the script, we'll pull the newest data available. As long as the website continues to be updated with new articles, which is likely, we'll have a constant influx of new information at our fingertips. The data Robin wants to collect from this particular website is the most recent news article along with its summary. Remember, the code for this will eventually be used in an application that will scrape live data with the click of a button—this site is dynamic and the articles will change frequently, which is why Robin is removing the manual task of retrieving each new article.


# <div align="center">Dataset</div>

We'll use our web application to scrape news articles and high-quality images, a collection of facts is a solid addition to her web app. from three different websites, store them in MongoDB, and display them in our webpage via Flask

- [Red Planet Science:](https://redplanetscience.com/) Our app will extract Mars news articles from this website
- [Space Images Mars:](https://spaceimages-mars.com/) Our app will extract featured images from the Jet Propulsion Laboratory
- [Space Images Mars:](https://galaxyfacts-mars.com/) Our app will extract featured images from the Jet Propulsion Laboratory

# <div align="center">Tools Used</div>
- **Python:** Programming language used to build automated auditing solution
    - **Splinter:** Python tool that will automate our web browser as we begin scraping
    - **Beautiful Soup:** Python package used for parsing HTML and XML documents
    - **Flask:** Python tool used for developing web applications
- **MongoDB:** NoSQL database used to store unstructrued data, such as images
- **HTML:** Hypertext Markup Language used to build and design webpages
- **Jupyter Notebook:** Open source web based application used to run our python code

[Back to top](#web-scraping-live-dashboard-with-python-and-mongoDB)