import base64
import traceback
from datetime import datetime
from requests import Session

class Kintone:
    def __init__(self, domain, login_name, password):
        authorization = base64.b64encode((login_name + ':' + password).encode('utf-8'))
        self.headers = {'X-Cybozu-Authorization': authorization.decode('utf-8')}
        self.domain = domain
        self.file_format = 'app_{}_{}.txt'

    def export(self, app_ids):
        try:
            session = Session()
            for app_id in app_ids:
                filename = self.file_format.format(app_id, datetime.today().strftime("%Y%m%d%H%M%S"))
                with open(filename, 'w') as file:
                    # アプリのアクセス権
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/acl.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(resp.content.decode('utf-8') + '\n')
                    # レコードのアクセス権
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/record/acl.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(resp.content.decode('utf-8') + '\n')
                    # フィールドのアクセス権
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/field/acl.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(resp.content.decode('utf-8') + '\n')
                    # JavaScript/CSSカスタマイズ設定
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/customize.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(resp.content.decode('utf-8') + '\n')
                    # プロセス管理の設定
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/status.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(resp.content.decode('utf-8') + '\n')
            return 1
        except Exception:
            print(traceback.format_exc())
            return 0
