from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('Ram.pdf')

docs = loader.load()

print(docs)
print(docs[1].page_content)
print(docs[1].metadata)