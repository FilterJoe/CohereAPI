# https://docs.cohere.com/docs/retrieval-augmented-generation-rag
# https://docs.cohere.com/docs/faster-web-search
# message="How many people in U.S. played Ultimate in 2012?",

import cohere
import json
import os


def print_citations(doc_dict: dict) -> None:
    """
    prints all citations in doc_dict. To print first citation only:
        print(response_dict['documents'][0]['title'])
        print(response_dict['documents'][0]['url'])
    :param doc_dict: response to cohere.Client.chat
    :return: None
    """
    for docs in response_dict['documents']:
        for attribute, value in docs.items():
            if attribute == 'title':
                print(attribute + ":", value)
            if attribute == 'url':
                print(attribute + ":", value)
                print()
    print()
        

api_key=os.environ.get("COHERE_API_KEY")
co = cohere.Client(api_key)
response = co.chat(
    message="Prepare table comparing memory bandwidth and maximum memory "
            "configuration of Apple's M2 and M3 chips including 3 variants for "
            "each: regular, Pro and Max. Label the columns Max and Bandwidth",
    model="command-r-plus",
    connectors=[{"id": "web-search",
    			 "user_access_token": api_key}]
)
# Two shorter options for connectors syntax:
#   connectors=[{"id": "web-search"}, ],
#   connectors = [cohere.ChatConnector(id="web-search")],

response_dict = response.dict()
print(response.text, "\n")
print_citations(response_dict)

# to see entire JSON dump
formatted_response = json.dumps(response_dict, indent=2)
print(formatted_response)

# to see one section at a time:
# print(response.text)
# print(response.citations)
# print(response.documents)
# print(response.search_queries)
# print(response.search_results)
# print(response.chat_history)
