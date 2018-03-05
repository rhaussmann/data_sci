import requests
from bs4 import BeautifulSoup

topic = 'Data_science'
url = 'https://en.wikipedia.org/wiki/{0}'.format(topic)
print 'making request to: {0}'.format(url)
r = requests.get(url)
print 'status code: {0}'.format(r.status_code)
# Note that it's best to explicitly use html.parser
soup = BeautifulSoup(r.text, 'html.parser')
print

print 'first paragraph:'
print soup.find('p').text
print 'number of paragraphs: {0}'.format(len(soup.find('p')))
print

print 'first image:'
print soup.find('img')
print "first image's source:\n{0}".format(soup.find('img')['src'])
print

print 'sections:'
sections = soup.find_all(class_='toctext')
print '\n'.join(section.text for section in sections)