from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer('all-MiniLM-L6-v2')

class MatchQuestion:
  def __init__(self):
      # with open("question_mapper.json", "r") as f:
          # self.question_bank = list(json.load(f).keys())
      
      self.question_bank = [
          "Download and process the files in  which contains three files with different encodings: data1.csv: CSV file encoded in CP-1252 data2.csv: CSV file encoded in UTF-8 data3.txt: Tab-separated file encoded in UTF-16 Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches ‘ OR ‡ OR œ across all three files.What is the sum of all values associated with these symbols?",

          """Write a web application that exposes an API with a single query parameter: ?country=. It should fetch the Wikipedia page of the country, extracts all headings (H1 to H6), and create a Markdown outline for the country. The outline should look like this:


          ## Contents

          # Vanuatu

          ## Etymology

          ## History

          ### Prehistory

          ...
          API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.
          Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
          Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.
          Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
          Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.""",

          """Your Task
          Source: Utilize IMDb's advanced web search at https://www.imdb.com/search/title/ to access movie data.
          Filter: Filter all titles with a rating between 5 and 7.
          Format: For up to the first 25 titles, extract the necessary details: ID, title, year, and rating. The ID of the movie is the part of the URL after tt in the href attribute. For example, tt10078772. Organize the data into a JSON structure as follows:

          [
            { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
            { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },
            // ... more titles
          ]
          Submit: Submit the JSON data in the text box below.""",
      ]
      self.question_bank_embeddings = model.encode(self.question_bank, convert_to_tensor=True)
  
  def match_question(self, ques):
      ques_embedding = model.encode(ques, convert_to_tensor=True)
      similarities = util.pytorch_cos_sim(ques_embedding, self.question_bank_embeddings)
      most_similar_idx = similarities.argmax().item()
      return self.question_bank[most_similar_idx]