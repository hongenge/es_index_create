from es_index.log_search import LogSearch
from es_index.log_download import LogDownload
from es_index.log_pre_download import LogPreDownload
from es_index.log_backend_operation import LogBackendOperation
from es_index.log_install import LogInstall
from es_index.log_community_search import LogCommunitySearch

def job():
    
    LogSearch().create_index()
    LogDownload().create_index()
    LogPreDownload().create_index()
    LogBackendOperation().create_index()
    LogInstall().create_index()
    LogCommunitySearch().create_index()

if __name__ == '__main__':
    job()