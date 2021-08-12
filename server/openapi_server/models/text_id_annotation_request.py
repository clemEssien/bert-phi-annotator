# coding: utf-8

from __future__ import absolute_import
from openapi_server.models.base_model_ import Model
from openapi_server.models.note import Note
from openapi_server import util


class TextIdAnnotationRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator
      (https://openapi-generator.tech).
    Do not edit the class manually.
    """

    def __init__(self, note=None):  # noqa: E501
        """TextIdAnnotationRequest - a model defined in OpenAPI

        :param note: The note of this TextIdAnnotationRequest.  # noqa: E501
        :type note: Note
        """
        self.openapi_types = {
            'note': Note
        }

        self.attribute_map = {
            'note': 'note'
        }

        self._note = note

    @classmethod
    def from_dict(cls, dikt) -> 'TextIdAnnotationRequest':
        """Returns the dict as a model
        :param dikt: A dict.
        :type: dict
        :return: The TextIdAnnotationRequest of this TextIdAnnotationRequest.  # noqa: E501
        :rtype: TextIdAnnotationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def note(self):
        """Gets the note of this TextIdAnnotationRequest.
        :return: The note of this TextIdAnnotationRequest.
        :rtype: Note
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TextIdAnnotationRequest.
        :param note: The note of this TextIdAnnotationRequest.
        :type note: Note
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note
