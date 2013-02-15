import os, sys
import urllib3
import json
import time

def goarchweet(query):
	nb_results = 0

	json_file_name = "%s/%s.json" % ( os.getcwd(), query.replace(' ','') )
	json_file = open(json_file_name, 'w')

	http = urllib3.PoolManager()
	fields = {
		'q': query.replace(' ', '+'),
		'rpp': 100,
		'page' : 1,
	}
	r = http.request('GET', 'http://search.twitter.com/search.json', fields)
	response = json.loads(r.data, encoding='utf-8')
	results = response['results']
	since_id = results[0]['id']
	for each in results:
		json_file.write(json.dumps(each) + '\n')
	json_file.close()
	nb_results += len(results)
	print nb_results

	while True:
		if 'next_page' in response:
			fields['page'] += 1
			fields['max_id'] = response['max_id_str']
			r = http.request('GET', 'https://api.twitter.com/1.1/search/tweets.json', fields)
			response = json.loads(r.data, encoding='utf-8')
			results = response['results']
			json_file = open(json_file_name, 'a')
			for each in results:
				json_file.write(json.dumps(each) + '\n')
			json_file.close()
			nb_results += len(results)
			print nb_results
		else:
			time.sleep(300)
			fields['page'] = 1
			try:
				del fields['max_id']
			except:
				pass
			fields['since_id'] = since_id
			r = http.request('GET', 'http://search.twitter.com/search.json', fields)
			response = json.loads(r.data, encoding='utf-8')
			results = response['results']
			if len(results) == 0:
				pass
			else:
				since_id = results[0]['id']
				json_file = open(json_file_name, 'a')
				for each in results:
					json_file.write(json.dumps(each) + '\n')
				json_file.close()
				nb_results += len(results)
				print nb_results

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'one query within quote please !'
		sys.exit(2)
	else:
		query = sys.argv[1]
		print "archweeting for query: %s" % sys.argv[1]
		goarchweet(query)
