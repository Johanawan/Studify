from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.
def jobSearch(request):

    list_of_listings = []

    if request.method == "POST":

        # Get inputs from user
        job_title_raw = request.POST.get("jobsearch")
        job_location_raw = request.POST.get("location")

        # remove whitespaces and replace with + for indeed url
        job_title = job_title_raw.replace(" ", "+")
        job_location = job_location_raw.replace(" ", "+")

        # List of the first 4 pages of the paginator
        pages = [""]

        for page in pages:
            # Create url format link
            url = "https://uk.indeed.com/jobs?q={}&l={}&start={}".format(job_title, job_location, page)
            

            html = requests.get(url)
            #print(html.status_code)

            src = html.content
            bs = BeautifulSoup(src, "html.parser")
            
            job_listings = bs.find_all("div", {"class": "jobsearch-SerpJobCard"})

            print(len(job_listings))

            listings = {}

            for listing in job_listings:
                
                # Get job title
                job_title = listing.find("a", {"title": True})["title"]
                listings["job_title"] = job_title

                # Get Url
                get_url = "https://uk.indeed.com" + listing.find("a", {"title":True})["href"] 
                listings["urls"] = get_url
                
                # Get company name
                company = listing.find("span", {"class": "company"}).get_text(strip=True)
                listings["company"] = company

                # Get location
                try:
                    location = listing.find("span", {"class": "location"}).get_text()
                    listings["location"] = location
                except AttributeError:
                    listings["location"] = job_location

                # Get salary data
                try:
                    salary = listing.find("span", {"class": "salaryText"}).text[2:]
                    listings["salary"] = salary
                except AttributeError:
                    listing["salary"] = "-"

                # Get date added
                date_added = listing.find("span", {"class": "date"}).get_text()
                listings["date_added"] = date_added

                # Produce a new copy of a dictionary to prevent the data being cleared out below.
                dict1 = listings.copy()

                # Append listings to list of listings
                list_of_listings.append(dict1)

                listings.clear()

                
        #print(list_of_listings)
        #print(listings)

    context = {
        "listings": list_of_listings,
    }

    return render(request, "jobsearch/jobsearch.html", context)