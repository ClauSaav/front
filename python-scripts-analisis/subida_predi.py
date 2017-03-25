import json  
import sys
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

args=sys.argv
#in case of using crontab add absolute path

with open(args[2]+'.json') as data_file:

        datajson=json.load(data_file)

es.index(index='skynet_beeva', doc_type=args[1], id=args[2], body= datajson)


ela_bancomer = es.get(index='skynet_beeva', doc_type=args[1], id=args[2])
