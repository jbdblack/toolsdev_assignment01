#Description: Scrape and Summarize News Articles

#pip install nltk
#pip install newspaper3k

#Import the libraries
import nltk
import newspaper

def userinput:
	userinput = input("Please enter any keyword(press enter to continue):")
	return userinput


CalNewport_paper = newspaper.build('https://www.calnewport.com/blog', memoize_articles=False)

edgeNews_paper = newspaper.build('https://www.edge.org/', memoize_articles = False)

AoM_paper = newspaper.build('https://www.artofmanliness.com/', memoize_articles = False)

#Edge Article Scrape
# for article in edgeNews_paper.articles:
# 	article.download()
# 	article.parse()
# 	article.nlp()
# 	if userinput in article.keywords:
# 		print(article.title)
# 		file = open('news_summary.txt', 'a')
# 		file.write("Title: " + str(article.title) + "- Author(s): " + str(article.authors)+ '\n' + '\n')
# 		file.close
# 	elif not userinput:
# 		print(article.title)
# 		file = open('news_summary.txt', 'a')
# 		file.write("Title: " + str(article.title) + "- Author(s): " + str(article.authors) + '\n' + '\n')
# 		file.close



#Cal Newport Article Scrape
# for article in CalNewport_paper.articles:
# 	article.download()
# 	article.parse()
# 	article.nlp()
# 	if userinput in article.keywords:
# 		print(article.title)
# 		file = open('news_summary.txt', 'a')
# 		file.write("Title: " + str(article.title) + "- Author(s): " + str(article.authors)+ '\n' + '\n')
# 		file.close
# 	elif not userinput:
# 		print(article.title)
# 		file = open('news_summary.txt', 'a')
# 		file.write("Title: " + str(article.title) + "- Author(s): " + str(article.authors) + '\n' + '\n')
# 		file.close

#AoM Article Scrape
for article in AoM_paper.articles:
	article.download()
	article.parse()
	article.nlp()
	if userinput in article.keywords:
		print(article.title)
		file = open('news_summary.txt', 'a')
		file.write("Title: " + str(article.title) + "- Author(s): " + str(article.authors)+ '\n' + '\n')
		file.close
	elif not userinput:
		print(article.title)
		file = open('news_summary.txt', 'a')
		file.write("Title: " + str(article.title) + "- Author(s): " + str(article.authors) + '\n' + '\n')
		file.close


