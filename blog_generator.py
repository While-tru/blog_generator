import cohere
from dotenv import dotenv_values
config = dotenv_values('.env')
cohere_api_key = config['API_KEY']
co = cohere.Client(cohere_api_key)

def generate_blog(paragraph_topic):
    response = co.generate(
        model='command',  # You can also try 'command-nightly' or 'command-light' if available
        prompt=f"Write a paragraph about the following topic: {paragraph_topic}",
        max_tokens=400,
        temperature=0.3
    )

    retrieve_blog = response.generations[0].text
    return retrieve_blog.strip()

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False