from flask import Flask, request, render_template, jsonify
from googleapiclient.discovery import build
import httplib2
from bs4 import BeautifulSoup, SoupStrainer


CSE_ID = 'XXXX'
API_KEY = 'XXXX'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


def rank_determination(domain, result):
    final_output = {
        'found': False,
        'rank': 'No match found',
        'page': 'No page found',
        'domain': 'No match found in top 10 google results or domain provided is incorrect',
    }
    for ind, each_item in enumerate(result['items']):
        if each_item['displayLink'] == domain:
            final_output['found'] = True
            final_output['rank'] = ind + 1
            final_output['page'] = each_item['formattedUrl']
            final_output['domain'] = domain
            return final_output
    return final_output


def extract_anchor_tags(domain):
    anchor_tags = []
    if domain != 'No page found':
        http = httplib2.Http()
        status, response = http.request(domain)
        for link in BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                anchor_tags.append(link['href'])
    return anchor_tags


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    keywords = request.args.get('keywords')
    domain = request.args.get('domain')
    google_search_result = google_search(keywords, API_KEY, CSE_ID)
    final_output = rank_determination(domain, google_search_result)
    anchor_tags_urls = extract_anchor_tags(final_output['page'])
    final_output['anchor_tags'] = anchor_tags_urls
    return jsonify(final_output)


if __name__ == '__main__':
    app.run()
