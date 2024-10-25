import requests
import json

# GitHub GraphQL API URL
GRAPHQL_API_URL = "https://api.github.com/graphql"



with open('config.json', 'r') as f:
    config = json.load(f)

query = f'''
{{
  user(login: "{config['github_username']}") {{
    projectsV2(first: 100) {{
      nodes {{
        title
        url
        number
        items(first: 100) {{
          nodes {{
            id
            content {{
              ... on Issue {{
                title
                url
                state
              }}
              ... on DraftIssue {{
                title
              }}
            }}            
          }}
        }}
      }}
    }}
  }}
}}
'''

headers = {
    "Authorization": f"Bearer {config['github_token']}"
}

# Make the request to the GraphQL API
r = requests.post(GRAPHQL_API_URL, json={"query": query}, headers=headers)
r.raise_for_status()

print(r.json()  )


