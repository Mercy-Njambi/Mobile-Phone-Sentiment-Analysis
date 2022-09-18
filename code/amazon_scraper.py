# imports
import requests
from bs4 import BeautifulSoup
from csv import writer
import time

# create a session object from requests, to emulate a browsing session
session = requests.Session()

# add header parameters
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "referer":'https://www.amazon.com/'}

# define the base url
base_url = "https://www.amazon.com"

# Get the product link
def get_product_links(url):
    """
    The function takes in a url
    returns all product links from that particular page

    get_product_links(url)
    """

    # Define the session and beautiful soup object
    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text, features="lxml")

    # create a list to hold the scraped links
    link_container = []
    # find all the links of interest
    link_articles = bsObj.find_all("h2", {"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})


    # loop through the links to access the target url
    for link in link_articles:
        if link == None:
            continue
        target_url = link.find('a', {"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})['href']
        link_container.append(target_url)

    # return a list of the target urls
    return link_container


# get the product details
def get_product_details(link):
    """
    The function takes in a product url link
    and returns the scraped details of that product, including:
    - product brand
    - product description
    - product price

    get_product_details(url)
    """

    # define our url by concatenating the product link to the base_url
    comment_link = base_url + link

    # create a request session and beautiful soup object
    req = session.get(comment_link, headers=headers)
    bsObj = BeautifulSoup(req.text, features="lxml")

    # create an empty list to contain the scraped data
    info_container = []

    # scrape the required details
    brand = bsObj.find("a", {"id":"bylineInfo"}).text
    info_container .append(brand)
    product_description = bsObj.find("span", {"id":"productTitle"}).text
    info_container .append(product_description)
    price = bsObj.find("span", {"class":"a-offscreen"}).text
    info_container .append(price)

    # return a list of the scraped product details
    return info_container


# get comment page link
def get_comment_page(link):
    """
    A function that scrapes the comment page of the particular product
    returns the link to the comments page
    """

    # try and access the reviews page, and catch the errors that might arise
    try:
        secondary_link = base_url + link
    except TypeError:
        print(None)
    except UnboundLocalError:
        print(None)

    # create a request session and a beautiful soup object
    req = session.get(secondary_link, headers=headers)
    bsObj = BeautifulSoup(req.text, features="lxml")

    # try and scrape the comment page, and catch any associated errors
    try:
        comments_page = bsObj.find("a", {"data-hook":"see-all-reviews-link-foot"})['href']
    except TypeError:
        comments_page = None

    # return the scraped comment page link
    return comments_page


# get the pagination link
def get_comment_pagination_link(url):
    """
    A function that takes in the a link(the review page link)
    and returns the pagination to help loop through all the reviews pages

    get_comment_pagination_link(url)
    """

    # try and create a concatenated url of the reviews page
    # and catch any errors that might arise
    try:
        tertiary_link = base_url + url
    except TypeError:
        print(None)
    except UnboundLocalError:
        print(None)

    # create a request session and a beautiful soup object
    req = session.get(tertiary_link, headers=headers)
    bsObj = BeautifulSoup(req.text, features="lxml")

    # try and scrape the pagination url while catching any errors that might arise from it
    try:
        comment_link = bsObj.find("ul", {"class":"a-pagination"})
        comment_link = comment_link.find("li", {"class":"a-last"})
        comment_anchor = comment_link.find("a")['href']
    except TypeError:
        print(None)
    except AttributeError:
        print(None)

    # try 
    try:
        all_comment_pages = [comment_anchor[:-26] + str(x) + '&reviewerType=all_reviews' for x in range(1,100)]
    except NameError:
        print(None)

    return all_comment_pages


# get the comments from the page
def get_comment_details(link, prod_desc):
    comment_link = "https://www.amazon.com" + link

    req = session.get(comment_link, headers=headers)
    bsObj = BeautifulSoup(req.text, features="lxml")

    article_data_container = bsObj.find_all("div", {"data-hook":"review"})

    # comment_container = []

    for item in article_data_container:
        try:
            comment_container = []

            rating_stars = item.find("span", {"class":"a-icon-alt"}).text
            comment_container.append(rating_stars)
            comment_title = item.find("a", {"data-hook":"review-title"}).text
            comment_container.append(comment_title)
            comment = item.find("span", {"data-hook":"review-body"}).text
            comment_container.append(comment)
            time_of_comment = item.find("span", {"data-hook":"review-date"}).text
            comment_container.append(time_of_comment)
            comment_container.extend(prod_desc)
            print(comment_container)
            save_data(comment_container)
            print("")
        except AttributeError:
            print(None)
        


# save data to csv file
# Import writer class from csv modul
def save_data(data_lst):
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('amazon_reviews_2.csv', 'a', encoding='UTF8', newline='') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data_lst)
    
        #Close the file object
        f_object.close()




for page in range(47,50):
    print("=================================")
    print(f'Now Scraping page {page}')
    print("=================================")
    print("")
    page_link = f"https://www.amazon.com/s?k=mobile+phones+unlocked&page={page}&qid=1662687603&ref=sr_pg_{page}"

    links = get_product_links(page_link)

    for link in links:
        if link == None:
            continue
        else:
            product_description = get_product_details(link)
            # if link == None:
            #     continue
            # else:
            reviews_pages = get_comment_pagination_link(get_comment_page(link))

            for page in reviews_pages:
                if page == None:
                    continue
                else:
                    comments = get_comment_details(page, product_description)
                    # time.sleep(5)



