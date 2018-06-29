# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.node import Node  # noqa: F401,E501
from swagger_server import util


class VC(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, nnodes=None, owner=None, fe=None, nodes=None):  # noqa: E501
        """VC - a model defined in Swagger

        :param name: The name of this VC.  # noqa: E501
        :type name: str
        :param description: The description of this VC.  # noqa: E501
        :type description: str
        :param nnodes: The nnodes of this VC.  # noqa: E501
        :type nnodes: int
        :param owner: The owner of this VC.  # noqa: E501
        :type owner: str
        :param fe: The fe of this VC.  # noqa: E501
        :type fe: Node
        :param nodes: The nodes of this VC.  # noqa: E501
        :type nodes: List[Node]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'nnodes': int,
            'owner': str,
            'fe': Node,
            'nodes': List[Node]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'nnodes': 'nnodes',
            'owner': 'owner',
            'fe': 'fe',
            'nodes': 'nodes'
        }

        self._name = name
        self._description = description
        self._nnodes = nnodes
        self._owner = owner
        self._fe = fe
        self._nodes = nodes

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VC of this VC.  # noqa: E501
        :rtype: VC
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this VC.


        :return: The name of this VC.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VC.


        :param name: The name of this VC.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VC.


        :return: The description of this VC.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VC.


        :param description: The description of this VC.
        :type description: str
        """

        self._description = description

    @property
    def nnodes(self):
        """Gets the nnodes of this VC.


        :return: The nnodes of this VC.
        :rtype: int
        """
        return self._nnodes

    @nnodes.setter
    def nnodes(self, nnodes):
        """Sets the nnodes of this VC.


        :param nnodes: The nnodes of this VC.
        :type nnodes: int
        """

        self._nnodes = nnodes

    @property
    def owner(self):
        """Gets the owner of this VC.


        :return: The owner of this VC.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this VC.


        :param owner: The owner of this VC.
        :type owner: str
        """

        self._owner = owner

    @property
    def fe(self):
        """Gets the fe of this VC.


        :return: The fe of this VC.
        :rtype: Node
        """
        return self._fe

    @fe.setter
    def fe(self, fe):
        """Sets the fe of this VC.


        :param fe: The fe of this VC.
        :type fe: Node
        """

        self._fe = fe

    @property
    def nodes(self):
        """Gets the nodes of this VC.


        :return: The nodes of this VC.
        :rtype: List[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this VC.


        :param nodes: The nodes of this VC.
        :type nodes: List[Node]
        """

        self._nodes = nodes