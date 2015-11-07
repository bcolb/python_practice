'''mars module. Get the temperature on mars'''
import urllib.request
import simplejson
def report():
    url = "http://marsweather.ingenology.com/v1/latest/?format=json"
    mars_results = urllib.request.urlopen(url)
    json_results = simplejson.loads(mars_results.read())
    results = json_results['report']
    for result in results:
        print(result + ': ' + str(results[result]))
if __name__ == '__main__':
    report()
