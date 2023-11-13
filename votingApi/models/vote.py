# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Vote(object):
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
        'poll_id': 'int',
        'choice_id': 'int',
        'user_id': 'str',
        'vote_time': 'datetime'
    }

    attribute_map = {
        'poll_id': 'poll_id',
        'choice_id': 'choice_id',
        'user_id': 'user_id',
        'vote_time': 'vote_time'
    }

    def __init__(self, poll_id=None, choice_id=None, user_id=None, vote_time=None):  # noqa: E501
        """Vote - a model defined in Swagger"""  # noqa: E501
        self._poll_id = None
        self._choice_id = None
        self._user_id = None
        self._vote_time = None
        self.discriminator = None
        if poll_id is not None:
            self.poll_id = poll_id
        if choice_id is not None:
            self.choice_id = choice_id
        if user_id is not None:
            self.user_id = user_id
        self.vote_time = vote_time

    @property
    def poll_id(self):
        """Gets the poll_id of this Vote.  # noqa: E501


        :return: The poll_id of this Vote.  # noqa: E501
        :rtype: int
        """
        return self._poll_id

    @poll_id.setter
    def poll_id(self, poll_id):
        """Sets the poll_id of this Vote.


        :param poll_id: The poll_id of this Vote.  # noqa: E501
        :type: int
        """

        self._poll_id = poll_id

    @property
    def choice_id(self):
        """Gets the choice_id of this Vote.  # noqa: E501


        :return: The choice_id of this Vote.  # noqa: E501
        :rtype: int
        """
        return self._choice_id

    @choice_id.setter
    def choice_id(self, choice_id):
        """Sets the choice_id of this Vote.


        :param choice_id: The choice_id of this Vote.  # noqa: E501
        :type: int
        """

        self._choice_id = choice_id

    @property
    def user_id(self):
        """Gets the user_id of this Vote.  # noqa: E501


        :return: The user_id of this Vote.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Vote.


        :param user_id: The user_id of this Vote.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def vote_time(self):
        """Gets the vote_time of this Vote.  # noqa: E501


        :return: The vote_time of this Vote.  # noqa: E501
        :rtype: datetime
        """
        return self._vote_time

    @vote_time.setter
    def vote_time(self, vote_time):
        """Sets the vote_time of this Vote.


        :param vote_time: The vote_time of this Vote.  # noqa: E501
        :type: datetime
        """
        if vote_time is None:
            raise ValueError("Invalid value for `vote_time`, must not be `None`")  # noqa: E501

        self._vote_time = vote_time

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
        if issubclass(Vote, dict):
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
        if not isinstance(other, Vote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other