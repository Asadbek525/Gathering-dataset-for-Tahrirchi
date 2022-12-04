from urllib.request import urlopen
import pandas as pd
from datetime import datetime


def get_page(url):
    return urlopen(url).read().decode('utf-8')

def get_dataset(url):
    page = get_page(url)
    # get body
    page = page[page.find('<body'):page.find('</body>')]
    
    # get text
    ptegs = []
    while True:
        start = page.find('<p')
        end = page.find('</p>')
        if start == -1 or end == -1:
            break
        ptegs.append(page[start:end+4])
        page = page[end+4:]

    # get content from ptegs
    content = []
    for p in ptegs:
        while True:
            start = p.find('<')
            end = p.find('>')
            if start == -1 or end == -1:
                break
            p = p[:start] + p[end+1:]
            
        p = p.replace('\n','')
        p = p.replace('\r','')
        p = p.replace("&ldquo;", '"')
        p = p.replace("&rdquo;", '"')
        p = p.replace("&nbsp;", ' ')
        p = p.replace("&mdash;", '-')
        p = p.replace("&ndash;", '-')
        p = p.replace("&rsquo;", "'")
        p = p.replace("&lsquo;", "'")
        p = p.replace("&hellip;", '...')
        p = p.replace("&quot;", '"')
        p = p.replace("&laquo;", '"')
        p = p.replace("&raquo;", '"')
        p = p.replace("&gt;", '>')
        p = p.replace("&lt;", '<')
        p = p.replace("&amp;", '&')
        p = p.strip()
        if p != '':
            content.append(p)
    
    # get words
    words = []
    punctuations = ['.',',','!','?',';',':','(',')','[',']','{','}','"','\'','«','»','-','—','\n','\r','\t']
    special_chars = ['0','1','2','3','4','5','6','7','8','9','*','/','+','-','=','<','>','&','|','^','%','$','#','@','~','`','\\']
    for p in content:
        for punc in punctuations:
            p = p.replace(punc, ' ')
        for word in p.split():
            if word.strip() != '':
                for char in special_chars:
                    if char in word:
                        break
                else:
                    if len(word) > 1:
                        words.append(word)
    
    # dataset of words
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    
    # sort dataset
    dictionary = dict(
        sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    # save dataset to csv file
    # columns: source_url, access_datetime, content, word, count
    df = pd.DataFrame(columns=['source_url', 'access_datetime', 'content', 'word', 'count'])
    for word in dictionary:
        df = pd.concat([df, pd.DataFrame([[url, datetime.now(), content, word, dictionary[word]]], columns=[
                       'source_url', 'access_datetime', 'content', 'word', 'count'])])
    
    return [df, dictionary]
