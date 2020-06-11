#Description: Scrape and Summarize News Articles

#pip install nltk
#pip install newspaper3k

#Import the libraries
import nltk
import newspaper


userinput = input("Please enter any keyword(press enter to continue):")


#Initialize Newspapers
NPR_paper = newspaper.build('https://www.npr.org/sections/news/', memoize_articles=False)

edgeNews_paper = newspaper.build('https://www.edge.org/', memoize_articles = False)

cnn_paper = newspaper.build('https://www.cnn.com/', memoize_articles = False)

#Function
def WriteNews(Title, Author, Summary):
	Document.write("Title: " + Title + "-" + "Author(s)" +str(Author) + '\n')
	Document.write(Summary)
	Document.write('\n' + " ")
	Document.write('\n')



Document = open('news_summary.txt', 'a')


# ##NPR Scrape
for article in NPR_paper.articles:
	try:
			article.download()
			article.parse()
			article.nlp()
	except:
			continue

	
	if userinput in article.keywords:
		
		Author = article.authors
		Title = article.title
		Summary = article.summary
		WriteNews(Title, Author, Summary)
	elif not userinput:
		Author = article.authors
		Title = article.title
		Summary = article.summary
		WriteNews(Title, Author, Summary)



##Edge.org Scrape
for article in edgeNews_paper.articles:
	try:
			article.download()
			article.parse()
			article.nlp()
	except:
			continue

	
	if userinput in article.keywords:
		
		Author = article.authors
		Title = article.title
		Summary = article.summary
		WriteNews(Title, Author, Summary)
	elif not userinput:
		Author = article.authors
		Title = article.title
		Summary = article.summary
		WriteNews(Title, Author, Summary)



##CNN Scrape
for article in cnn_paper.articles:
	try:
			article.download()
			article.parse()
			article.nlp()
	except:
			continue

	
	if userinput in article.keywords:
		
		Author = article.authors
		Title = article.title
		Summary = article.summary
		WriteNews(Title, Author, Summary)
	elif not userinput:
		Author = article.authors
		Title = article.title
		Summary = article.summary
		WriteNews(Title, Author, Summary)
		

Document.close()
