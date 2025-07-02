from langchain_community.document_loaders import WebBaseLoader

url = 'https://en.wikipedia.org/wiki/Nepal'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs[0].page_content)