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


class V1alpha1VirtualMachineExportStatus(object):
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
        'conditions': 'list[V1alpha1Condition]',
        'links': 'V1alpha1VirtualMachineExportLinks',
        'phase': 'str',
        'service_name': 'str',
        'token_secret_ref': 'str',
        'ttl_expiration_time': 'K8sIoApimachineryPkgApisMetaV1Time'
    }

    attribute_map = {
        'conditions': 'conditions',
        'links': 'links',
        'phase': 'phase',
        'service_name': 'serviceName',
        'token_secret_ref': 'tokenSecretRef',
        'ttl_expiration_time': 'ttlExpirationTime'
    }

    def __init__(self, conditions=None, links=None, phase=None, service_name=None, token_secret_ref=None, ttl_expiration_time=None):
        """
        V1alpha1VirtualMachineExportStatus - a model defined in Swagger
        """

        self._conditions = None
        self._links = None
        self._phase = None
        self._service_name = None
        self._token_secret_ref = None
        self._ttl_expiration_time = None

        if conditions is not None:
          self.conditions = conditions
        if links is not None:
          self.links = links
        if phase is not None:
          self.phase = phase
        if service_name is not None:
          self.service_name = service_name
        if token_secret_ref is not None:
          self.token_secret_ref = token_secret_ref
        if ttl_expiration_time is not None:
          self.ttl_expiration_time = ttl_expiration_time

    @property
    def conditions(self):
        """
        Gets the conditions of this V1alpha1VirtualMachineExportStatus.

        :return: The conditions of this V1alpha1VirtualMachineExportStatus.
        :rtype: list[V1alpha1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1alpha1VirtualMachineExportStatus.

        :param conditions: The conditions of this V1alpha1VirtualMachineExportStatus.
        :type: list[V1alpha1Condition]
        """

        self._conditions = conditions

    @property
    def links(self):
        """
        Gets the links of this V1alpha1VirtualMachineExportStatus.

        :return: The links of this V1alpha1VirtualMachineExportStatus.
        :rtype: V1alpha1VirtualMachineExportLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this V1alpha1VirtualMachineExportStatus.

        :param links: The links of this V1alpha1VirtualMachineExportStatus.
        :type: V1alpha1VirtualMachineExportLinks
        """

        self._links = links

    @property
    def phase(self):
        """
        Gets the phase of this V1alpha1VirtualMachineExportStatus.

        :return: The phase of this V1alpha1VirtualMachineExportStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1alpha1VirtualMachineExportStatus.

        :param phase: The phase of this V1alpha1VirtualMachineExportStatus.
        :type: str
        """

        self._phase = phase

    @property
    def service_name(self):
        """
        Gets the service_name of this V1alpha1VirtualMachineExportStatus.
        ServiceName is the name of the service created associated with the Virtual Machine export. It will be used to create the internal URLs for downloading the images

        :return: The service_name of this V1alpha1VirtualMachineExportStatus.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this V1alpha1VirtualMachineExportStatus.
        ServiceName is the name of the service created associated with the Virtual Machine export. It will be used to create the internal URLs for downloading the images

        :param service_name: The service_name of this V1alpha1VirtualMachineExportStatus.
        :type: str
        """

        self._service_name = service_name

    @property
    def token_secret_ref(self):
        """
        Gets the token_secret_ref of this V1alpha1VirtualMachineExportStatus.
        TokenSecretRef is the name of the secret that contains the token used by the export server pod

        :return: The token_secret_ref of this V1alpha1VirtualMachineExportStatus.
        :rtype: str
        """
        return self._token_secret_ref

    @token_secret_ref.setter
    def token_secret_ref(self, token_secret_ref):
        """
        Sets the token_secret_ref of this V1alpha1VirtualMachineExportStatus.
        TokenSecretRef is the name of the secret that contains the token used by the export server pod

        :param token_secret_ref: The token_secret_ref of this V1alpha1VirtualMachineExportStatus.
        :type: str
        """

        self._token_secret_ref = token_secret_ref

    @property
    def ttl_expiration_time(self):
        """
        Gets the ttl_expiration_time of this V1alpha1VirtualMachineExportStatus.
        The time at which the VM Export will be completely removed according to specified TTL Formula is CreationTimestamp + TTL

        :return: The ttl_expiration_time of this V1alpha1VirtualMachineExportStatus.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._ttl_expiration_time

    @ttl_expiration_time.setter
    def ttl_expiration_time(self, ttl_expiration_time):
        """
        Sets the ttl_expiration_time of this V1alpha1VirtualMachineExportStatus.
        The time at which the VM Export will be completely removed according to specified TTL Formula is CreationTimestamp + TTL

        :param ttl_expiration_time: The ttl_expiration_time of this V1alpha1VirtualMachineExportStatus.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._ttl_expiration_time = ttl_expiration_time

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
        if not isinstance(other, V1alpha1VirtualMachineExportStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
