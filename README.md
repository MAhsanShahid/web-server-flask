# web-server-flask
 Sending request to Google cloud platform custom search JSON API for google search and sending a response to client using Rest API
 
Also implemented the simple frontend on HTML5 and JavaScript just to send a request to the API and better visualization of the JSON responses. Google custom search JSON API has been used to search the keywords for checking the domain ranking in the top 10 google results. And to run the project you have to generate an API Key and Customized search engine ID and put it at the top of app.py file. You can simply do it using the following links:
- https://developers.google.com/custom-search/v1/overview (To Get a key)
- https://cse.google.com/cse/all (To build a programmable search engine)
### Disclaimer: The results from a customized programmable search engine might differ from actual google searches and I came to know about it while performing testing. It is not a problem in my task execution but from Google API Results as mentioned on their official developer platform.  
 - source: https://support.google.com/programmable-search/answer/70392?hl=en

When you will open app.py file, you can see the following lines of code where you have to provide your own generated id and key instead of 'XXXX'. I have removed my key and id as it Is something not secure.
 - CSE_ID = 'XXXX'
 - API_KEY = 'XXXX'
Once everything goes fine and you will be able to run it then you just have to open a browser and open the ' http://127.0.0.1:5000/ ' (in my case) in your browser and you will see the interface to operate it. You can also see the URL and port in the terminal on what it is running and just have to copy and paste it in the browser. If you will face any problem while running it or have any question regarding it just feel free to write me. I would like to answer it as soon as possible.

I had built Flask-web-server using PyCharm. It would be great if you can open it on PyCharm and run it as it renders static JavaScript and CSS files and also renders index.html files. Then you don't have to put any extra effort to make it work. 

