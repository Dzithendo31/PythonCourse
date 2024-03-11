import json
from pprint import pprint
#Read and write toa JSON
with open("day15raw.json","r") as file:
    data = json.load(file)

post_summary = []
for post in data['posts']:
    post_sum = {}
    post_sum['title'] = post['title']
    post_sum['author'] = post['author']
    post_sum['number_of_comments'] = len(post['comments'])
    post_summary.append(post_sum)

with open("posts_summary.json", 'w') as output_file:
    json.dump({"posts_summary":post_summary}, output_file, indent=4)
pprint(post_summary)
#Expected output
{
  "posts_summary": [
    {
      "title": "The Future of AI",
      "author": "Alice",
      "number_of_comments": 3
    },
    {
      "title": "Learning Python",
      "author": "Bob",
      "number_of_comments": 1
    },
    {
      "title": "Web Development Trends",
      "author": "Charlie",
      "number_of_comments": 0
    }
  ]
}
