# each of these is a Jinja template. see gdutils.strings.jinja_render()

summarise_text = """
Summarise the following. Be concise, concrete, and easy to understand. Provide only the summary itself, without any superfluous conversation, commentary etc. {{ granularity }}

----
{{ txt }}
"""


# UNTESTED
summarise_list_of_texts_as_one = """
Summarise the whole of the following list. Be concise, concrete, and easy to understand. Provide only the summary itself, without any superfluous conversation or commentary etc. {{ granularity }}

----
{% for txt in txts %}
- {{txt}}
{% endfor %}
----
"""
