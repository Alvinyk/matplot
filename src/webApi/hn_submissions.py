import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code:",r.status_code)

submission_ids = r.json()
submission_dicts = []
for submision_id in submission_ids[:30]:
	url = ('https://hacker-news.firebaseio.com/v0/item/'+str(submision_id)+'.json')
	submision_r = requests.get(url)
	print(submision_r.status_code)
	response_dict = submision_r.json()
	
	submision_dict = {
	'title':response_dict['title'],
	'link':'https://news.ycombinator.com/item?id='+str(submision_id),
	'comments':response_dict.get('descendants',0)
	}
	submision_dicts.append(submision_dict)
	
submision_dicts = sort(submision_dicts,key=itemgetter('comments'),reverse=True)

for submision_dict in submision_dicts:
	print('\nTitles:',submision_dict['title'])
	print('Discussion link:',submision_dict['link'])
	print('Comments:',submision_dict['comments'])

