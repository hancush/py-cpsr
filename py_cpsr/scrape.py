import requests


class ICPSR(requests.Session):

    BASE_STUDY_URL = 'http://www.icpsr.umich.edu/cgi-bin/bob/zipcart2'

    def __init__(self, username, password):
        super().__init__()

        rv = self._login(username, password)


    def _login(self, username, password):

        rv = self.get('https://www.icpsr.umich.edu/mydata')

        params = {
            'email': username,
            'password': password,
            'path': '',
            'request_uri': 'https://www.icpsr.umich.edu/mydata',
            'noautoguest': '',
        }

        parts = self.multipart_encode(params)

        return self.post('https://www.icpsr.umich.edu/rpxlogin', files=parts)


    def multipart_encode(self, params):

        parts = {}

        for field, value in params.items():
            parts[field] = (None, value)

        return parts


    def agree_to_terms(self, params):

        terms_url = 'http://www.icpsr.umich.edu/cgi-bin/terms'
        rv = self.get(terms_url, params=params)

        agree_params = params.copy()

        agree_params.update({'agree': 'yes'})
        parts = self.multipart_encode(agree_params)

        return self.post(terms_url, files=parts)


    def _format_study_name(self):
        raise NotImplementedError


    def download(self, study_id):

        params = {
            'path': 'ICPSR',
            'study': study_id,
            'bundle': '',
            'ds': '',
            'dups': 'yes'
        }

        self.get(self.BASE_STUDY_URL, params=params)

        self.agree_to_terms(params)

        rv = self.get(self.BASE_STUDY_URL, params=params)

        if rv.ok:
            with open('icpsr-{0}.zip'.format(study_id), 'wb') as f:
                f.write(rv.content)
