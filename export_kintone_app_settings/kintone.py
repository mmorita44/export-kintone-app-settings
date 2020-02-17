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
                file_contents = []
                file_contents.append('{')
                # 一般設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/settings.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"一般設定": {resp.content.decode("utf-8")},\n')
                # フィールドの一覧
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/fields.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"フィールドの一覧": {resp.content.decode("utf-8")},\n')
                # フォームのレイアウト
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/layout.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"フォームのレイアウト": {resp.content.decode("utf-8")},\n')
                # 一覧の設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/views.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"一覧の設定": {resp.content.decode("utf-8")},\n')
                # アプリのアクセス権
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"アプリのアクセス権": {resp.content.decode("utf-8")},\n')
                # レコードのアクセス権
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/record/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"レコードのアクセス権": {resp.content.decode("utf-8")},\n')
                # フィールドのアクセス権
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/field/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"フィールドのアクセス権": {resp.content.decode("utf-8")},\n')
                # JavaScript/CSSカスタマイズ設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/customize.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"JavaScript/CSSカスタマイズ設定": {resp.content.decode("utf-8")},\n')
                # プロセス管理の設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/status.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents.append(f'"プロセス管理の設定": {resp.content.decode("utf-8")}\n')
                file_contents.append('}')

                filename = self.file_format.format(app_id, datetime.today().strftime("%Y%m%d%H%M%S"))
                with open(filename, 'w') as file:
                    file.writelines(file_contents)
            return 0
        except Exception:
            print(traceback.format_exc())
            return 1
