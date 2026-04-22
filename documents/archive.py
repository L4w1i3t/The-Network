"""
Document archive - queryable store for all classified records.
"""

from typing import Optional

from documents.record import Document, DocumentType, Classification
from utils.encryption import Encryption


class Archive:
    """
    Central document archive with query, filter, and retrieval capabilities.
    """

    def __init__(self):
        self._documents: dict[str, Document] = {}
        self._access_log: list[dict] = []

    @property
    def count(self) -> int:
        return len(self._documents)

    def ingest(self, doc: Document):
        """Add a document to the archive."""
        self._documents[doc.doc_id] = doc

    @staticmethod
    def _bounded_limit(limit: int) -> int:
        """Normalize result limits so negative values do not become reverse slices."""
        return max(0, limit)

    def get(self, doc_id: str) -> Optional[Document]:
        """Retrieve a single document by ID."""
        doc = self._documents.get(doc_id.upper())
        if doc:
            self._log("RETRIEVE", doc_id)
        return doc

    def search(self, query: str, limit: int = 25) -> list[Document]:
        """Full-text search across all document fields."""
        self._log("SEARCH", query)
        results = [d for d in self._documents.values() if d.matches_query(query)]
        return results[:self._bounded_limit(limit)]

    def filter(self, doc_type: Optional[DocumentType] = None,
               classification: Optional[Classification] = None,
               tag: Optional[str] = None,
               limit: int = 25) -> list[Document]:
        """Retrieve documents matching structured filters."""
        self._log("FILTER", f"type={doc_type} cls={classification} tag={tag}")
        results = [
            d for d in self._documents.values()
            if d.matches_filters(doc_type, classification, tag)
        ]
        return results[:self._bounded_limit(limit)]

    def list_all(self, limit: int = 50) -> list[Document]:
        """Return all documents (up to limit), sorted by date descending."""
        docs = sorted(self._documents.values(), key=lambda d: d.date, reverse=True)
        return docs[:self._bounded_limit(limit)]

    def list_by_type(self, doc_type: DocumentType, limit: int = 25) -> list[Document]:
        return self.filter(doc_type=doc_type, limit=limit)

    def list_by_tag(self, tag: str, limit: int = 25) -> list[Document]:
        return self.filter(tag=tag, limit=limit)

    def all_tags(self) -> list[str]:
        """Return all unique tags across the archive."""
        tags = set()
        for doc in self._documents.values():
            tags.update(t.lower() for t in doc.subject_tags)
        return sorted(tags)

    def stats(self) -> dict:
        """Return archive statistics."""
        type_counts = {}
        cls_counts = {}
        for doc in self._documents.values():
            type_counts[doc.doc_type.value] = type_counts.get(doc.doc_type.value, 0) + 1
            cls_counts[doc.classification.value] = cls_counts.get(doc.classification.value, 0) + 1

        return {
            "Total Documents": self.count,
            "By Type": type_counts,
            "By Classification": cls_counts,
            "Unique Tags": len(self.all_tags()),
            "Access Log Entries": len(self._access_log),
        }

    def get_access_log(self, count: int = 20) -> list[dict]:
        return self._access_log[-count:]

    def _log(self, action: str, detail: str):
        self._access_log.append({
            "timestamp": Encryption.generate_timestamp(),
            "action": action,
            "detail": detail,
        })
