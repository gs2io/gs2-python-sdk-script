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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_script_client.Gs2Script import Gs2Script


class UpdateScriptRequest(Gs2BasicRequest):

    class Constant(Gs2Script):
        FUNCTION = "UpdateScript"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateScriptRequest, self).__init__(params)
        if params is None:
            self.__script_name = None
        else:
            self.set_script_name(params['scriptName'] if 'scriptName' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__script = None
        else:
            self.set_script(params['script'] if 'script' in params.keys() else None)

    def get_script_name(self):
        """
        スクリプトの名前を指定します。を取得
        :return: スクリプトの名前を指定します。
        :rtype: unicode
        """
        return self.__script_name

    def set_script_name(self, script_name):
        """
        スクリプトの名前を指定します。を設定
        :param script_name: スクリプトの名前を指定します。
        :type script_name: unicode
        """
        if script_name and not (isinstance(script_name, str) or isinstance(script_name, unicode)):
            raise TypeError(type(script_name))
        self.__script_name = script_name

    def with_script_name(self, script_name):
        """
        スクリプトの名前を指定します。を設定
        :param script_name: スクリプトの名前を指定します。
        :type script_name: unicode
        :return: this
        :rtype: UpdateScriptRequest
        """
        self.set_script_name(script_name)
        return self

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        if description and not (isinstance(description, str) or isinstance(description, unicode)):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: UpdateScriptRequest
        """
        self.set_description(description)
        return self

    def get_script(self):
        """
        Luaスクリプトを取得
        :return: Luaスクリプト
        :rtype: unicode
        """
        return self.__script

    def set_script(self, script):
        """
        Luaスクリプトを設定
        :param script: Luaスクリプト
        :type script: unicode
        """
        if script and not (isinstance(script, str) or isinstance(script, unicode)):
            raise TypeError(type(script))
        self.__script = script

    def with_script(self, script):
        """
        Luaスクリプトを設定
        :param script: Luaスクリプト
        :type script: unicode
        :return: this
        :rtype: UpdateScriptRequest
        """
        self.set_script(script)
        return self
