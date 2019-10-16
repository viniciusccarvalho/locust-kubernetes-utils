import os


class ManifestMaker:

    def __init__(self, config):
        self.config = config
        self.templates = os.path.join(os.path.dirname(__file__), 'resources/')

    def master_deployment(self):
        return self.__template_parse("locust-master.yaml")

    def worker_deployment(self):
        return self.__template_parse("locust-worker.yaml")

    def master_service(self):
        return self.__template_parse("locust-master-service.yaml")

    def master_service_lb(self):
        return self.__template_parse("locust-master-service-lb.yaml")

    def __template_parse(self, template):
        template = os.path.join(self.templates, template)
        tmpl = open(template, 'rt').read()
        text = tmpl.format(**self.config)
        return text
