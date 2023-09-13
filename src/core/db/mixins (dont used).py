# """Database module, including the SQLAlchemy database object and DB-related utilities."""
# from typing import Optional, Type, TypeVar
#
# T = TypeVar("T", bound="PkModel")
#
# # Alias common SQLAlchemy names
# Column = db.Column
# relationship = db.relationship
#
#
# class CRUDMixin:
#     """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""
#
#     @classmethod
#     def create(cls, **kwargs):
#         """Create a new record and save it the database."""
#         instance = cls(**kwargs)
#         return instance.save()
#
#     def update(self, commit=True, **kwargs):
#         """Update specific fields of a record."""
#         for attr, value in kwargs.items():
#             setattr(self, attr, value)
#         if commit:
#             return self.save()
#         return self
#
#     def save(self, commit=True):
#         """Save the record."""
#         session.add(self)
#         if commit:
#             session.commit()
#         return self
#
#     def delete(self, commit: bool = True) -> None:
#         """Remove the record from the database."""
#         session.delete(self)
#         if commit:
#             return session.commit()
#         return
#
#
# class Model(CRUDMixin, db.Model):
#     """Base model class that includes CRUD convenience methods."""
#
#     __abstract__ = True
#
#
# class PkModel(Model):
#     """Base model class that includes CRUD convenience methods, plus adds a 'primary key' column named ``id``."""
#
#     __abstract__ = True
#     id = Column(db.Integer, primary_key=True)
#
#     @classmethod
#     def get_by_id(cls: Type[T], record_id) -> Optional[T]:
#         """Get record by ID."""
#         if any(
#             (
#                 isinstance(record_id, (str, bytes)) and record_id.isdigit(),
#                 isinstance(record_id, (int, float)),
#             )
#         ):
#             return cls.query.get(int(record_id))
#         return None
