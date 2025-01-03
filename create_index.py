import yaml
import datetime
from elasticsearch import Elasticsearch

#搜索日志类
class LogSearch:
    def __init__(self):
        #配置文件
        with open("conf.yaml",'r', encoding='utf-8')as f:
            conf = yaml.load(f, Loader=yaml.FullLoader)
        self.es= Elasticsearch(conf['es']['host'],basic_auth=(conf['es']['user'],conf['es']['pwd']))
        self.create_body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0,
                "index.default_pipeline": "search_index_pipeline"
            },
            "mappings": {
                "properties": {
                    "created_at": {
                    "type": "date"
                    },
                    "ip": {
                        "type": "text"
                    },
                    "word": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                            }
                        }
                    },
                    "user_id": {
                        "type": "integer"
                    },
                    "phone_serial": {
                        "type": "keyword"
                    },
                    "widevine": {
                        "type": "keyword"
                    },
                    "oaid": {
                        "type": "keyword"
                    }
                }
            }
        }

    #获取下个月
    def get_next_month_start(self):
        year = int(datetime.datetime.now().strftime("%Y"))
        month = int(datetime.datetime.now().strftime("%m"))
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        return '{}{:02d}'.format(year, month)

    #创建索引
    def create_index(self):
        es_index = "log.search_index_%s" % self.get_next_month_start()
        print(es_index)
        if self.es.indices.exists(index=es_index) != True:
            print("创建索引：",es_index)
            self.es.indices.create(index=es_index,body=self.create_body)


def job():
    logsearch = LogSearch()
    logsearch.create_index()
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(t)
    print("-----------------------")

if __name__ == '__main__':
    job()