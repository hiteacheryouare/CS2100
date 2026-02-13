'''
    CS2100
    spring 2026
    Starter code for class on 2/9/26

    The starter code:
    - has a main that: (1) gathers image data for all the dates we specified. 
        (2) for each image, renders it in a matplotlib plot. (3) for ALL images,
        puts them into a basic HTML page.
    - has a function to display image data using matplotlib
    - has a function to generate a basic, ugly HTML page with a bunch of images

    In class, we'll..
    - write the request_api function using the requests library and try/except
    - write the generate_image_data function that returns a list of dictionaries,
        with each dictionary repping an image's: url, title, and date.

'''

from typing import Any, Optional
from urllib.request import urlopen
from PIL import Image
import matplotlib.pyplot as plt
import requests

API_KEY = "IeKfM0gnN1MghI7wXALScIQYhftYtPv2na66gxlq"
BASE_URL = "https://api.nasa.gov/planetary/apod"
DATES= ["2026-01-07", "2025-10-31", "2000-01-01"]



def request_api(base_url: str, params: dict[str, str]) -> Optional[Any]:
    ''' request (get) an API from a URL, and return json data

        parameters: 
            url(str), the URL to request using request.get
            params (dct[str, str]), the parameters to pass along with the URL

        returns: 
            get response, in JSON format. Or None, if request not completed.
        
    '''
    try:
        return requests.get(base_url, params=params, timeout=10).json()
    except:
        return None

def generate_image_data(url: str, params: dict[str, str],
                        dates: list[str]) -> list[dict[str, str]]:
    ''' generate image data by making get requests to the given API 

        parameters:
            url (str), the URL of the API function we're calling
            params (dict of {str: str}), the parameters to pass to the API function
        
        returns:
            list of dict[str, str], including "url", "date", "title" info returned 
            from API call
        
        raises:
            ValueError if given list of dates is empty
            ValueError if None returned from API call
            KeyError if data returned does not include all expected keys:
                url, date, title
    '''
    if dates == []:
        raise ValueError("no")
    image_data = []
    for date in dates:
        data = request_api(url, params | {"date": date})
        if data:
            image_data.append({
                "date": data[date],
                "url": data["url"],
                "title": data["title"]
            })
        else:
            raise ValueError("no no no")

def create_html_page(image_data: list[dict[str, str]],
                        output_file: str = "cs2100_planets.html") -> None:
    ''' Create a very basic, ugly HTML page with all the images given

        parameters:
            image_data: list of dicts with 'url', 'date', 'title' keys
            output_file: name of HTML file to create (defaults to cs2100_planets.html")
        
        returns: none
    '''
    html_content = """<!DOCTYPE html>
    <html>
    <head>
    <title>CS2100 - Astronomy Pictures of the Day</title>
    </head>
    <body>
    <h1>CS2100 - APODs :)</h1>"""

    for item in image_data:
        html_content += f"""
    <h2>{item['title']}</h2>
    <p>{item['date']}</p>
    <img src="{item['url']}" width="200">
    <hr>"""

    html_content += """</body></html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    
def display_image_from_url(url: str,  date: str,
                            title: str = "Astronomy Picture of the Day") -> None:
    ''' call a NASA API function that returns an image, and render it
        along with a description.

        parameters: 
            url(str), the url to open
            caption (str), defaults to "", the caption for the image rendered
            title (str), default to "APOtD", the title to include on the rendering
        returns:
            nothing, just renders the image
    '''
    image = Image.open(urlopen(url))
    plt.imshow(image, origin = "upper")
    plt.tick_params(left = False, bottom = False,
                        labelleft = False, labelbottom = False)
    plt.title(title)
    plt.xlabel(date)
    plt.show()

def main() -> None:
    ''' call a NASA API for the APOD, for all given dates,
        render each image and generate a basic web page with all of them '''
    params = {"api_key": API_KEY}
    images = generate_image_data(BASE_URL, params, DATES)
    for image in images:
        display_image_from_url(image["url"], date = image["date"],
                            title = image["title"])

    # Create HTML page with all images
    create_html_page(images)

if __name__ == "__main__":
    main()
