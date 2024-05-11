cns_3 = '''Principles of public key crypto systems, 
Topic 2
Topic 3 
<< Remaining topics pasted here >> '''

import webbrowser
def openBrowser(text,posttext):
    query = text + posttext 
    search_url = "https://www.google.com/search?q=" + '+'.join(query.split())
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Path to Chrome executable may vary
    webbrowser.get(chrome_path).open(search_url)

def searchQuery(topics_sub):
    topics,subject = topics_sub
    for topic in topics.split("\n"):
        openBrowser(topic, subject + " Notes , Videos ,Content")
        print(topic)
searchQuery((cns_3," in Cryptography and network security"))
