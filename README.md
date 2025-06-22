# Flask Framework
Flask is a lightweight WSGI web application framework & Flask leverages Jinja2 as its template engine. 
### WSGI = 
WSGI, which stands for Web Server Gateway Interface, is a specification that defines a standard interface between web servers and Python web applications or frameworks.
### Jinja2 =
 Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document.
                               !pip install Jinja2
1.WSGI  :-
Host any server like Apache , IIS , etc…

2.Jinja2 = 
web templates system along with serten data source , this data source dynamically put or integrate this web template with a data source, and final AIM that to render dynamic pages

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The resust is passed</h1></body></html>"  
   --- return "<html><body><h1>The resust is passed</h1></body></html>" hardcodeing the html is not a good idea
create a html page and call it over here
###### jinja2 templetes engine technique
<head>
 <link rel="stylesheet"  href="{{ url_for('static',filename='css/style.css') }}">---<link> this way adding external file,using an external "style.css" file
</head>
<head>
 <link rel="stylesheet"  href="{{ url_for('static',filename='css/style.css') }}">
<script>
  alert("This page has been loaded")--- javascripts
</script>
</head>