# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1DataVolumeCheckpoint(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'current': 'str',
        'previous': 'str'
    }

    attribute_map = {
        'current': 'current',
        'previous': 'previous'
    }

    def __init__(self, current=None, previous=None):
        """
        V1beta1DataVolumeCheckpoint - a model defined in Swagger
        """

        self._current = None
        self._previous = None

        self.current = current
        self.previous = previous

    @property
    def current(self):
        """
        Gets the current of this V1beta1DataVolumeCheckpoint.
        Current is the identifier of the snapshot created for this checkpoint.

        :return: The current of this V1beta1DataVolumeCheckpoint.
        :rtype: str
        """
        return self._current

    @current.setter
    def current(self, current):
        """
        Sets the current of this V1beta1DataVolumeCheckpoint.
        Current is the identifier of the snapshot created for this checkpoint.

        :param current: The current of this V1beta1DataVolumeCheckpoint.
        :type: str
        """
        if current is None:
            raise ValueError("Invalid value for `current`, must not be `None`")

        self._current = current

    @property
    def previous(self):
        """
        Gets the previous of this V1beta1DataVolumeCheckpoint.
        Previous is the identifier of the snapshot from the previous checkpoint.

        :return: The previous of this V1beta1DataVolumeCheckpoint.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous):
        """
        Sets the previous of this V1beta1DataVolumeCheckpoint.
        Previous is the identifier of the snapshot from the previous checkpoint.

        :param previous: The previous of this V1beta1DataVolumeCheckpoint.
        :type: str
        """
        if previous is None:
            raise ValueError("Invalid value for `previous`, must not be `None`")

        self._previous = previous

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1DataVolumeCheckpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
