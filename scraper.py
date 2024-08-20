from langchain_community.document_transformers import Html2TextTransformer
from langchain_community.document_loaders.web_base import WebBaseLoader



print(1)
urls=["https://searchengineland.com/guide/what-is-seo",
       "https://business.adobe.com/blog/basics/content-marketing",
       "https://www.wordstream.com/ppc",
       "https://www.constantcontact.com/blog/what-is-social-media-management/",
       ]
print(2)
loader = WebBaseLoader(urls, bs_get_text_kwargs={"strip": True})
print(2.5)
docs = loader.load()
print(3)
h2t= Html2TextTransformer()
print(4)
material= h2t.transform_documents(docs)
print(5)
with open("info.txt" ,"a") as f :
    f.write(material)
print("end")
