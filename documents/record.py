"""
Document record system.

Defines the data model for all documents in the archive:
field reports, memos, intercepted transmissions, directives,
research analyses, incident reports, and diagnostic files.

Every document carries proper classification markings, provenance,
and cross-reference links to related records.
"""

from enum import Enum
from typing import Optional
from dataclasses import dataclass, field


class Classification(Enum):
    """Security classification levels."""
    UNCLASSIFIED = "UNCLASSIFIED"
    RESTRICTED = "RESTRICTED"
    CONFIDENTIAL = "CONFIDENTIAL"
    SECRET = "SECRET"
    TOP_SECRET = "TOP SECRET"
    TOP_SECRET_YORHA = "TOP SECRET // YORHA EYES ONLY"
    ABOVE_TOP_SECRET = "TOP SECRET // BLACK CLEARANCE"     # Commander and N2 only
    MACHINE_INTERNAL = "[MACHINE NETWORK - INTERCEPTED]"   # Decoded intercepts


class DocumentType(Enum):
    """Categories of documents in the archive."""
    FIELD_REPORT = "FIELD REPORT"
    MEMORANDUM = "MEMORANDUM"
    DIRECTIVE = "OPERATIONAL DIRECTIVE"
    INTERCEPT = "SIGNAL INTERCEPT"
    DOSSIER = "PERSONNEL DOSSIER"
    RESEARCH = "RESEARCH ANALYSIS"
    INCIDENT = "INCIDENT REPORT"
    DIAGNOSTIC = "DIAGNOSTIC / AUTOPSY"
    BRIEFING = "INTELLIGENCE BRIEFING"
    TRANSCRIPT = "TRANSCRIPT"
    AFTER_ACTION = "AFTER-ACTION REPORT"
    AMENDMENT = "AMENDMENT / ERRATA"


@dataclass
class Document:
    """A single document in the archive."""

    doc_id: str                                     # e.g. "RPT-2B-0847", "MEMO-CMD-0012"
    title: str
    doc_type: DocumentType
    classification: Classification
    date: str                                       # In-universe date, e.g. "11945.03.14"
    author: str
    body: str                                       # The full text content
    subject_tags: list[str] = field(default_factory=list)   # Searchable tags
    cross_references: list[str] = field(default_factory=list)  # Related doc IDs
    distribution: str = "STANDARD"                  # Who may receive this
    status: str = "ACTIVE"                          # ACTIVE, ARCHIVED, REDACTED, RESCINDED
    addendum: Optional[str] = None                  # Appended notes / updates
    redacted_sections: int = 0                      # Number of [REDACTED] blocks in body

    def matches_query(self, query: str) -> bool:
        """Check if this document matches a search query (case-insensitive)."""
        q = query.lower()
        searchable = (
            f"{self.doc_id} {self.title} {self.author} {self.body} "
            f"{' '.join(self.subject_tags)} {self.doc_type.value} "
            f"{self.classification.value}"
        ).lower()
        return q in searchable

    def matches_filters(self, doc_type: Optional[DocumentType] = None,
                        classification: Optional[Classification] = None,
                        tag: Optional[str] = None) -> bool:
        """Check if this document matches structured filters."""
        if doc_type and self.doc_type != doc_type:
            return False
        if classification and self.classification != classification:
            return False
        if tag and tag.lower() not in [t.lower() for t in self.subject_tags]:
            return False
        return True

