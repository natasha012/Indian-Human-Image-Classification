import requests
from bs4 import BeautifulSoup
import os

#url = 'https://www.gettyimages.in/photos/indian-faces?page=2&phrase=indian%20faces&sort=mostpopular'

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
        print("processing")
    except:
        print("passed")
        pass
    print("folder made")
    os.chdir(os.path.join(os.getcwd(), folder))
    print("getting in")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')  # converts to a html parser
    images=soup.find_all('img')
    print("images:",images)
    for image in images:
        try:
            name = image['alt']  #image->inspect->alt=name
            link = image['src']  #image->inspect->src=source
            with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                im = requests.get(link)
                f.write(im.content)
                print('Writing: ', name)
        except:
            pass


imagedown('https://www.gettyimages.in/photos/exotic-cars?page=2&phrase=exotic%20cars&sort=mostpopular', 'non_human_images')
