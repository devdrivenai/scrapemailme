from bs4 import BeautifulSoup
import requests

def get_site_content(url):
    resp = requests.get(url)
    resp.raise_for_status()
    if resp.status_code != 204:    
        content = resp.content
        # returns type 'bytes'
        return content
    return 'Bummer!'

def soup_instance(html_content):
    # returns <class 'bs4.BeautifulSoup'>
    return BeautifulSoup(html_content, 'html.parser')

## IDS ##

# if we just want the one elem with 'id', including tag, children, etc
def get_elem_by_id(soup_instance, id):
    # return <class 'bs4.element.Tag'>
    # i.e.: the whole tag plus its contents and/or children
    return soup_instance.find(id=id)

## TEXT CONTENTS ##
# if we want to get the text of elem and its children
def get_elem_and_child_str(elem):
    # returns type 'str' 
    return elem.text

## CLASSES ##
# if we want all the elements that has 'class'
def get_elems_by_class(soup_instance, class_str):
    result = soup_instance.css.select(f'.{class_str}')
    # returns <class 'bs4.element.ResultSet'>
    return result

def get_classes_elem_str(elems_set):
    classes_elem_str = ''
    for result in elems_set:
        # each result is of type -> bs4.element.Tag
        elem_str = get_elem_and_child_str(result)
        clean_str = clean_text(elem_str)
        classes_elem_str += '\n' + clean_str
    # returns 'str'
    return classes_elem_str

## UTILS ##
def clean_text(text):
    clean_str = ''.join([char for char in text if char != '\n'])
    return clean_str


## GENERAL MANAGER ##
def web_scrape_manager(scraping_info):
    final_str = ''
    for website in scraping_info:
        final_str += f'Result for {website["name"]}:'
        site_content = get_site_content(website['url'])
        soup = soup_instance(site_content)
        if 'id' in website:
            elems = get_elem_by_id(soup, website['id'])
            elems_str = get_elem_and_child_str(elems)
        elif 'class' in website:
            elems = get_elems_by_class(soup, website['class'])
            elems_str = get_classes_elem_str(elems)
        clean_str = clean_text(elems_str)
        final_str += '\n' + clean_str + '\n'
        final_str += '*-*-' * 20 + '\n'
    return final_str
