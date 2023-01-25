import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
from selenium import webdriver
from selenium.webdriver import Chrome

url = "https://hh.kz/search/vacancy?area=160&search_field=name&search_field=company_name&search_field=description&text=python&from=suggest_post&hhtmFrom=vacancy_search_list"


next_page = 0
job_titles=None
job_descriptions=None
company_names=None
driver = Chrome ()

with open("python_job_vacancies.csv", "w") as f:
        f.write("Job Title, Company Name, Job Description\n")
        while next_page != None:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            i=0
            while i < 50:
                url_job=soup.find_all('a', class_='serp-item__title')[i].get('href')
                print(i)
                i += 1 
                response2 = requests.get(url_job, headers={'User-Agent': UserAgent().chrome}, proxies=None)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                job_titles=soup2.find('h1').text
                job_descriptions=soup2.find('div', class_='g-user-content').text
                company_names=soup2.find('div', class_='vacancy-company-details').text
                f.write(f"{job_titles}, {company_names}, {job_descriptions}\n")
            next_page=soup.find(attrs={'data-qa': 'pager-next'})
            next_page='https://hh.kz'+next_page.get('href')
            url=next_page