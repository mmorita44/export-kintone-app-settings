import base64
import traceback
import json
from datetime import datetime
from pathlib import Path
from requests import Session


class Kintone:
    def __init__(self, domain, login_name, password):
        authorization = base64.b64encode(
            (login_name + ':' + password).encode('utf-8'))
        self.headers = {
            'X-Cybozu-Authorization': authorization.decode('utf-8')}
        self.domain = domain
        self.file_format = 'app_{}_settings.json'

    def export(self, app_ids):
        try:
            export_dir = Path(datetime.today().strftime("%Y%m%d%H%M%S"))
            export_dir.mkdir()
            session = Session()
            for app_id in app_ids:
                file_contents = {}
                # 一般設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/settings.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["一般設定"] = json.loads(
                    resp.content.decode("utf-8"))
                # フィールドの一覧
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/fields.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["フィールドの一覧"] = json.loads(
                    resp.content.decode("utf-8"))
                # フォームのレイアウト
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/layout.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["フォームのレイアウト"] = json.loads(
                    resp.content.decode("utf-8"))
                # 一覧の設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/views.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["一覧の設定"] = json.loads(
                    resp.content.decode("utf-8"))
                # アプリのアクセス権
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["アプリのアクセス権"] = json.loads(
                    resp.content.decode("utf-8"))
                # レコードのアクセス権
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/record/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["レコードのアクセス権"] = json.loads(
                    resp.content.decode("utf-8"))
                # フィールドのアクセス権
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/field/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["フィールドのアクセス権"] = json.loads(
                    resp.content.decode("utf-8"))
                # JavaScript/CSSカスタマイズ設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/customize.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["JavaScript/CSSカスタマイズ設定"] = json.loads(
                    resp.content.decode("utf-8"))
                # プロセス管理の設定
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/status.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception('[Error] app_id: {}, status_code: {}, content: {}'
                                    .format(app_id, resp.status_code, resp.content.decode("utf-8")))
                file_contents["プロセス管理の設定"] = json.loads(
                    resp.content.decode("utf-8"))

                filename = self.file_format.format(app_id)
                with export_dir.joinpath(filename).open(mode='w') as file:
                    json.dump(file_contents, file, ensure_ascii=False,
                              indent=2, sort_keys=True, separators=(',', ': '))
            return 0
        except Exception:
            print(traceback.format_exc())
            return 1
