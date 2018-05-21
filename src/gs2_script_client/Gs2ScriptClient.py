# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2ScriptClient(AbstractGs2Client):

    ENDPOINT = "script"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2ScriptClient, self).__init__(credential, region)

    def create_script(self, request):
        """
        スクリプトを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_script_client.control.CreateScriptRequest.CreateScriptRequest
        :return: 結果
        :rtype: gs2_script_client.control.CreateScriptResult.CreateScriptResult
        """
        body = { 
            "name": request.get_name(),
            "script": request.get_script(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_script_client.control.CreateScriptRequest import CreateScriptRequest
        from gs2_script_client.control.CreateScriptResult import CreateScriptResult
        return CreateScriptResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/script",
            service=self.ENDPOINT,
            component=CreateScriptRequest.Constant.MODULE,
            target_function=CreateScriptRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_script(self, request):
        """
        スクリプトを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_script_client.control.DeleteScriptRequest.DeleteScriptRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_script_client.control.DeleteScriptRequest import DeleteScriptRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/script/" + str(("null" if request.get_script_name() is None or request.get_script_name() == "" else url_encoder.encode(request.get_script_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteScriptRequest.Constant.MODULE,
            target_function=DeleteScriptRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_script(self, request):
        """
        スクリプトの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_script_client.control.DescribeScriptRequest.DescribeScriptRequest
        :return: 結果
        :rtype: gs2_script_client.control.DescribeScriptResult.DescribeScriptResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_script_client.control.DescribeScriptRequest import DescribeScriptRequest

        from gs2_script_client.control.DescribeScriptResult import DescribeScriptResult
        return DescribeScriptResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/script",
            service=self.ENDPOINT,
            component=DescribeScriptRequest.Constant.MODULE,
            target_function=DescribeScriptRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_script(self, request):
        """
        スクリプトを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_script_client.control.GetScriptRequest.GetScriptRequest
        :return: 結果
        :rtype: gs2_script_client.control.GetScriptResult.GetScriptResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_script_client.control.GetScriptRequest import GetScriptRequest

        from gs2_script_client.control.GetScriptResult import GetScriptResult
        return GetScriptResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/script/" + str(("null" if request.get_script_name() is None or request.get_script_name() == "" else url_encoder.encode(request.get_script_name()))) + "",
            service=self.ENDPOINT,
            component=GetScriptRequest.Constant.MODULE,
            target_function=GetScriptRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_script(self, request):
        """
        スクリプトを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_script_client.control.UpdateScriptRequest.UpdateScriptRequest
        :return: 結果
        :rtype: gs2_script_client.control.UpdateScriptResult.UpdateScriptResult
        """
        body = { 
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_script() is not None:
            body["script"] = request.get_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_script_client.control.UpdateScriptRequest import UpdateScriptRequest
        from gs2_script_client.control.UpdateScriptResult import UpdateScriptResult
        return UpdateScriptResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/script/" + str(("null" if request.get_script_name() is None or request.get_script_name() == "" else url_encoder.encode(request.get_script_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateScriptRequest.Constant.MODULE,
            target_function=UpdateScriptRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))
