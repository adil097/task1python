import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
import time
from selenium import webdriver
from selenium.webdriver import Chrome

url = "https://hh.kz/search/vacancy?area=160&search_field=name&search_field=company_name&search_field=description&text=python&from=suggest_post&hhtmFrom=vacancy_search_list"
driver = Chrome ()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

i=0
with open("python_job_vacancies.csv", "w") as f:
    f.write("Job Title, Company Name, Experience, Salary Low, Salary High, Keywords, Job Description\n")
    while i < 49:
        i += 1
        #print(i)
        url_job=soup.find_all('a', class_='serp-item__title')[i].get('href')
        response2 = requests.get(url_job, headers={'User-Agent': UserAgent().chrome}, proxies=None)
        soup2 = BeautifulSoup(response2.text, 'html.parser')
        job_titles=soup2.find('h1').text
        #experience=soup2.find('div', class_='vacancy-company-details').text
        #salary1=soup2.find('div', class_='vacancy-company-details').text
        #salary2=soup2.find('div', class_='vacancy-company-details').text
        #keyword=soup2.find('div', class_='vacancy-company-details').text
        job_descriptions=soup2.find('div', class_='g-user-content').text
        company_names=soup2.find('div', class_='vacancy-company-details').text
        f.write(f"{job_titles}, {company_names}, {job_descriptions}\n")
    