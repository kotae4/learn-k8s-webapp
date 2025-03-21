# coding: utf-8

"""
    learn-k8s-apiserver-net

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Choice(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'choice_id': 'int',
        'poll_id': 'int',
        'value': 'str'
    }

    attribute_map = {
        'choice_id': 'choiceId',
        'poll_id': 'pollId',
        'value': 'value'
    }

    def __init__(self, choice_id=None, poll_id=None, value=None):  # noqa: E501
        """Choice - a model defined in Swagger"""  # noqa: E501
        self._choice_id = None
        self._poll_id = None
        self._value = None
        self.discriminator = None
        if choice_id is not None:
            self.choice_id = choice_id
        if poll_id is not None:
            self.poll_id = poll_id
        self.value = value

    @property
    def choice_id(self):
        """Gets the choice_id of this Choice.  # noqa: E501


        :return: The choice_id of this Choice.  # noqa: E501
        :rtype: int
        """
        return self._choice_id

    @choice_id.setter
    def choice_id(self, choice_id):
        """Sets the choice_id of this Choice.


        :param choice_id: The choice_id of this Choice.  # noqa: E501
        :type: int
        """

        self._choice_id = choice_id

    @property
    def poll_id(self):
        """Gets the poll_id of this Choice.  # noqa: E501


        :return: The poll_id of this Choice.  # noqa: E501
        :rtype: int
        """
        return self._poll_id

    @poll_id.setter
    def poll_id(self, poll_id):
        """Sets the poll_id of this Choice.


        :param poll_id: The poll_id of this Choice.  # noqa: E501
        :type: int
        """

        self._poll_id = poll_id

    @property
    def value(self):
        """Gets the value of this Choice.  # noqa: E501


        :return: The value of this Choice.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Choice.


        :param value: The value of this Choice.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Choice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Choice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
