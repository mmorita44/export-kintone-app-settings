import base64
import traceback
import json
from datetime import datetime
from pathlib import Path
from requests import Session


class Kintone:
    ERROR_MESSAGE = "[Error] app_id: {}, api_name: {}, status_code: {}, content: {}"

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
                api_name = ""
                # 一般設定
                api_name = "一般設定"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/settings.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # フィールドの一覧
                api_name = "フィールドの一覧"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/fields.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # フォームのレイアウト
                api_name = "フォームのレイアウト"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/form/layout.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # 一覧の設定
                api_name = "一覧の設定"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/views.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # アプリのアクセス権
                api_name = "アプリのアクセス権"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # レコードのアクセス権
                api_name = "レコードのアクセス権"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/record/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # フィールドのアクセス権
                api_name = "フィールドのアクセス権"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/field/acl.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # JavaScript/CSSカスタマイズ設定
                api_name = "JavaScript/CSSカスタマイズ設定"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/customize.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # プロセス管理の設定
                api_name = "プロセス管理の設定"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/status.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # アプリの条件通知
                api_name = "アプリの条件通知"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/notifications/general.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # レコードの条件通知
                api_name = "レコードの条件通知"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/notifications/perRecord.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # リマインダーの条件通知
                api_name = "リマインダーの条件通知"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/notifications/reminder.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # アプリのグラフ設定の取得
                api_name = "アプリのグラフ設定の取得"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/reports.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))
                # アプリのアクションの設定の取得
                api_name = "アプリのアクションの設定の取得"
                resp = session.get(f'https://{self.domain}.cybozu.com/k/v1/app/actions.json?app={app_id}',
                                   headers=self.headers)
                if resp.status_code != 200:
                    raise Exception(self.ERROR_MESSAGE.format(
                        app_id, api_name, resp.status_code, resp.content.decode("utf-8")))
                file_contents[api_name] = json.loads(
                    resp.content.decode("utf-8"))

                filename = self.file_format.format(app_id)
                with export_dir.joinpath(filename).open(mode='w') as file:
                    json.dump(file_contents, file, ensure_ascii=False,
                              indent=2, sort_keys=True, separators=(',', ': '))
            return 0
        except Exception:
            print(traceback.format_exc())
            return 1
