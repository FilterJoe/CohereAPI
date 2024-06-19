# Cohere's Web Search API Example

Command R+ can be used on [Cohere's playground](https://coral.cohere.com/).

Click on web search mode, ask a factual question, and you'll see that Command R+ does a good job of answering accurately and citing sources.

To do the same thing (but not as pretty) on your own system using Cohere's API:

* Create a Cohere account
* [Get a trial key](https://dashboard.cohere.com/api-keys) from Cohere
* pip install cohere
* copy web_test.py
* set up your Cohere key in your env (or alternatively place the key string directly into the code)

web_test.py shows you the result, and how to pick apart the JSON response which includes not just the query and references, but the text of each web page sourced and other metadata.
