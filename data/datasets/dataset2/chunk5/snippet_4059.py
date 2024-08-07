#Source: https://stackoverflow.com/questions/40916386/typeerror-when-searching-google-with-the-google-api-python-3
import requests, urllib, json

def search(search_string):
  query = urllib.parse.urlencode({'q': search_string})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.request.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  data = results['responseData']
  print('Total results: %s' % data['cursor']['estimatedResultCount'])
  hits = data['results']
  print('Top %d hits:' % len(hits))
  for h in hits: print(' ', h['url'])
  print('For more results, see %s' % data['cursor']['moreResultsUrl'])
  print(hits)

search(input('Enter search query:'))