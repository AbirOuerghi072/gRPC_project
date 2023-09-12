from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class state(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PublishSuccess: _ClassVar[state]
    Publish_Success: _ClassVar[state]
    PublishFailed: _ClassVar[state]
    Connexion_Lost: _ClassVar[state]
    Client_NOT_Connected: _ClassVar[state]
    Client_Connected: _ClassVar[state]
    Incorrect_Proto_Version: _ClassVar[state]
    Bad_Client_ID: _ClassVar[state]
    Server_Unvailable: _ClassVar[state]
    Bad_User_Pw: _ClassVar[state]
    Not_AUTH: _ClassVar[state]
PublishSuccess: state
Publish_Success: state
PublishFailed: state
Connexion_Lost: state
Client_NOT_Connected: state
Client_Connected: state
Incorrect_Proto_Version: state
Bad_Client_ID: state
Server_Unvailable: state
Bad_User_Pw: state
Not_AUTH: state

class ComingData(_message.Message):
    __slots__ = ["Topic", "Payload", "Qos"]
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    QOS_FIELD_NUMBER: _ClassVar[int]
    Topic: str
    Payload: str
    Qos: int
    def __init__(self, Topic: _Optional[str] = ..., Payload: _Optional[str] = ..., Qos: _Optional[int] = ...) -> None: ...

class ReturnType(_message.Message):
    __slots__ = ["Acknowledgment"]
    ACKNOWLEDGMENT_FIELD_NUMBER: _ClassVar[int]
    Acknowledgment: state
    def __init__(self, Acknowledgment: _Optional[_Union[state, str]] = ...) -> None: ...
