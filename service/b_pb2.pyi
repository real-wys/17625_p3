from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    class GenreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CLASSIC: Book.GenreType
    CRIME: Book.GenreType
    FANTASY: Book.GenreType
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.GenreType
    publishingYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.GenreType, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    class GenreType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CLASSIC: CreateRequest.GenreType
    CRIME: CreateRequest.GenreType
    FANTASY: CreateRequest.GenreType
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: CreateRequest.GenreType
    publishingYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[CreateRequest.GenreType, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ["Created"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    Created: bool
    def __init__(self, Created: bool = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: int
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[int] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["Exist", "book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    EXIST_FIELD_NUMBER: _ClassVar[int]
    Exist: bool
    book: Book
    def __init__(self, Exist: bool = ..., book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "id", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    BOOK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    book: Book
    id: int
    status: InventoryItem.Status
    def __init__(self, id: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.Status, str]] = ...) -> None: ...
