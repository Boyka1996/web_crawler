class UrlManager():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None or len(url)==0:
            return
        elif url in self.new_urls or url in self.old_urls:
            return
        else:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        pass

    def get_url(self):
        pass

    def has_new_url(self):
        pass
