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


class V1alpha1VirtualMachinePreferenceSpec(object):
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
        'clock': 'V1alpha1ClockPreferences',
        'cpu': 'V1alpha1CPUPreferences',
        'devices': 'V1alpha1DevicePreferences',
        'features': 'V1alpha1FeaturePreferences',
        'firmware': 'V1alpha1FirmwarePreferences',
        'machine': 'V1alpha1MachinePreferences'
    }

    attribute_map = {
        'clock': 'clock',
        'cpu': 'cpu',
        'devices': 'devices',
        'features': 'features',
        'firmware': 'firmware',
        'machine': 'machine'
    }

    def __init__(self, clock=None, cpu=None, devices=None, features=None, firmware=None, machine=None):
        """
        V1alpha1VirtualMachinePreferenceSpec - a model defined in Swagger
        """

        self._clock = None
        self._cpu = None
        self._devices = None
        self._features = None
        self._firmware = None
        self._machine = None

        if clock is not None:
          self.clock = clock
        if cpu is not None:
          self.cpu = cpu
        if devices is not None:
          self.devices = devices
        if features is not None:
          self.features = features
        if firmware is not None:
          self.firmware = firmware
        if machine is not None:
          self.machine = machine

    @property
    def clock(self):
        """
        Gets the clock of this V1alpha1VirtualMachinePreferenceSpec.
        Clock optionally defines preferences associated with the Clock attribute of a VirtualMachineInstance DomainSpec

        :return: The clock of this V1alpha1VirtualMachinePreferenceSpec.
        :rtype: V1alpha1ClockPreferences
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """
        Sets the clock of this V1alpha1VirtualMachinePreferenceSpec.
        Clock optionally defines preferences associated with the Clock attribute of a VirtualMachineInstance DomainSpec

        :param clock: The clock of this V1alpha1VirtualMachinePreferenceSpec.
        :type: V1alpha1ClockPreferences
        """

        self._clock = clock

    @property
    def cpu(self):
        """
        Gets the cpu of this V1alpha1VirtualMachinePreferenceSpec.
        CPU optionally defines preferences associated with the CPU attribute of a VirtualMachineInstance DomainSpec

        :return: The cpu of this V1alpha1VirtualMachinePreferenceSpec.
        :rtype: V1alpha1CPUPreferences
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this V1alpha1VirtualMachinePreferenceSpec.
        CPU optionally defines preferences associated with the CPU attribute of a VirtualMachineInstance DomainSpec

        :param cpu: The cpu of this V1alpha1VirtualMachinePreferenceSpec.
        :type: V1alpha1CPUPreferences
        """

        self._cpu = cpu

    @property
    def devices(self):
        """
        Gets the devices of this V1alpha1VirtualMachinePreferenceSpec.
        Devices optionally defines preferences associated with the Devices attribute of a VirtualMachineInstance DomainSpec

        :return: The devices of this V1alpha1VirtualMachinePreferenceSpec.
        :rtype: V1alpha1DevicePreferences
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """
        Sets the devices of this V1alpha1VirtualMachinePreferenceSpec.
        Devices optionally defines preferences associated with the Devices attribute of a VirtualMachineInstance DomainSpec

        :param devices: The devices of this V1alpha1VirtualMachinePreferenceSpec.
        :type: V1alpha1DevicePreferences
        """

        self._devices = devices

    @property
    def features(self):
        """
        Gets the features of this V1alpha1VirtualMachinePreferenceSpec.
        Features optionally defines preferences associated with the Features attribute of a VirtualMachineInstance DomainSpec

        :return: The features of this V1alpha1VirtualMachinePreferenceSpec.
        :rtype: V1alpha1FeaturePreferences
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this V1alpha1VirtualMachinePreferenceSpec.
        Features optionally defines preferences associated with the Features attribute of a VirtualMachineInstance DomainSpec

        :param features: The features of this V1alpha1VirtualMachinePreferenceSpec.
        :type: V1alpha1FeaturePreferences
        """

        self._features = features

    @property
    def firmware(self):
        """
        Gets the firmware of this V1alpha1VirtualMachinePreferenceSpec.
        Firmware optionally defines preferences associated with the Firmware attribute of a VirtualMachineInstance DomainSpec

        :return: The firmware of this V1alpha1VirtualMachinePreferenceSpec.
        :rtype: V1alpha1FirmwarePreferences
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this V1alpha1VirtualMachinePreferenceSpec.
        Firmware optionally defines preferences associated with the Firmware attribute of a VirtualMachineInstance DomainSpec

        :param firmware: The firmware of this V1alpha1VirtualMachinePreferenceSpec.
        :type: V1alpha1FirmwarePreferences
        """

        self._firmware = firmware

    @property
    def machine(self):
        """
        Gets the machine of this V1alpha1VirtualMachinePreferenceSpec.
        Machine optionally defines preferences associated with the Machine attribute of a VirtualMachineInstance DomainSpec

        :return: The machine of this V1alpha1VirtualMachinePreferenceSpec.
        :rtype: V1alpha1MachinePreferences
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """
        Sets the machine of this V1alpha1VirtualMachinePreferenceSpec.
        Machine optionally defines preferences associated with the Machine attribute of a VirtualMachineInstance DomainSpec

        :param machine: The machine of this V1alpha1VirtualMachinePreferenceSpec.
        :type: V1alpha1MachinePreferences
        """

        self._machine = machine

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
        if not isinstance(other, V1alpha1VirtualMachinePreferenceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
