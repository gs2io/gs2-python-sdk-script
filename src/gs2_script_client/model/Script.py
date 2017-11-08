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

class Script(object):

    def __init__(self, params=None):
        if params is None:
            self.__script_id = None
            self.__create_at = None
            self.__name = None
            self.__script = None
            self.__owner_id = None
            self.__update_at = None
            self.__description = None
        else:
            self.set_script_id(params['scriptId'] if 'scriptId' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_script(params['script'] if 'script' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)


    def get_script_id(self):
        """
        スクリプトGRNを取得
        :return: スクリプトGRN
        :rtype: unicode
        """
        return self.__script_id

    def set_script_id(self, script_id):
        """
        スクリプトGRNを設定
        :param script_id: スクリプトGRN
        :type script_id: unicode
        """
        self.__script_id = script_id

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_name(self):
        """
        スクリプト名を取得
        :return: スクリプト名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        スクリプト名を設定
        :param name: スクリプト名
        :type name: unicode
        """
        self.__name = name

    def get_script(self):
        """
        スクリプトデータを取得
        :return: スクリプトデータ
        :rtype: unicode
        """
        return self.__script

    def set_script(self, script):
        """
        スクリプトデータを設定
        :param script: スクリプトデータ
        :type script: unicode
        """
        self.__script = script

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

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
        self.__description = description

    def to_dict(self):
        return { 
            "scriptId": self.__script_id,
            "createAt": self.__create_at,
            "name": self.__name,
            "script": self.__script,
            "ownerId": self.__owner_id,
            "updateAt": self.__update_at,
            "description": self.__description,
        }