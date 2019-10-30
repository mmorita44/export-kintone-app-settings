import base64
import traceback
from datetime import datetime
from requests import Session

class Kintone:
    def __init__(self, domain, login_name, password):
        authorization = base64.b64encode((login_name + ':' + password).encode('utf-8'))
        self.headers = {'X-Cybozu-Authorization': authorization.decode('utf-8')}
        self.domain = domain
        self.file_format = 'app_{}_{}.json'

    def export(self, app_ids):
        try:
            session = Session()
            for app_id in app_ids:
                filename = self.file_format.format(app_id, datetime.today().strftime("%Y%m%d%H%M%S"))
                with open(filename, 'w') as file:
                    file.writelines('{')
                    # 一般設定
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/settings.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"一般設定": {resp.content.decode("utf-8")},')
                    # フィールドの一覧
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/fields.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"フィールドの一覧": {resp.content.decode("utf-8")},')
                    # フォームのレイアウト
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/layout.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"フォームのレイアウト": {resp.content.decode("utf-8")},')
                    # 一覧の設定
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/views.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"一覧の設定": {resp.content.decode("utf-8")},')
                    # アプリのアクセス権
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/acl.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"アプリのアクセス権": {resp.content.decode("utf-8")},')
                    # レコードのアクセス権
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/record/acl.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"レコードのアクセス権": {resp.content.decode("utf-8")},')
                    # フィールドのアクセス権
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/field/acl.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"フィールドのアクセス権": {resp.content.decode("utf-8")},')
                    # JavaScript/CSSカスタマイズ設定
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/customize.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"JavaScript/CSSカスタマイズ設定": {resp.content.decode("utf-8")},')
                    # プロセス管理の設定
                    resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/status.json?app={app_id}',
                                       headers=self.headers)
                    file.writelines(f'"プロセス管理の設定": {resp.content.decode("utf-8")}')
                    file.writelines('}')
            return 1
        except Exception:
            print(traceback.format_exc())
            return 0
