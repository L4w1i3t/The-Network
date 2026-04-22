"""
Terminal rendering for the classified archive interface.

All output goes through this module. The aesthetic is institutional,
sterile, and cold -- a system that was never designed to be pleasant, only
functional.  Classification banners, redaction marks, document headers,
and monospaced table layouts live here.
"""

import sys
import time
import os
import re
import textwrap

# Enable ANSI escape sequences on Windows
if os.name == "nt":
    os.system("")


class Colors:
    """ANSI color codes."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"

    RED = "\033[31m"
    RED_BRIGHT = "\033[91m"
    RED_BG = "\033[41m"
    WHITE = "\033[37m"
    WHITE_BRIGHT = "\033[97m"
    CYAN = "\033[36m"
    CYAN_BRIGHT = "\033[96m"
    YELLOW = "\033[33m"
    YELLOW_BRIGHT = "\033[93m"
    BLUE = "\033[34m"
    BLUE_BRIGHT = "\033[94m"
    MAGENTA = "\033[35m"
    MAGENTA_BRIGHT = "\033[95m"
    GREEN = "\033[32m"
    GREEN_BRIGHT = "\033[92m"
    BLACK_BG = "\033[40m"
    GREY = "\033[90m"


# Map classification strings to display colors
CLASSIFICATION_COLORS = {
    "UNCLASSIFIED":       Colors.GREEN,
    "RESTRICTED":         Colors.CYAN,
    "CONFIDENTIAL":       Colors.BLUE,
    "SECRET":             Colors.YELLOW,
    "TOP_SECRET":         Colors.RED,
    "TOP_SECRET_YORHA":   Colors.RED_BRIGHT,
    "ABOVE_TOP_SECRET":   Colors.RED_BRIGHT + Colors.BOLD,
    "MACHINE_INTERNAL":   Colors.MAGENTA_BRIGHT,
}


class Terminal:
    """Institutional-grade terminal output for a classified archive system."""

    WIDTH = 76  # Standard display width
    BODY_INDENT = 4
    BODY_WIDTH = WIDTH - 6

    # ---------- screen control ----------

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    # ---------- low-level output ----------

    @staticmethod
    def print_line(text: str = "", color: str = "", indent: int = 2):
        """Print a single line with optional color and indentation."""
        pad = " " * indent
        if color:
            print(f"{pad}{color}{text}{Colors.RESET}")
        else:
            print(f"{pad}{text}")

    @staticmethod
    def blank():
        print()

    # ---------- structural elements ----------

    @staticmethod
    def rule(char: str = "-", width: int = 0, color: str = Colors.GREY):
        w = width or Terminal.WIDTH
        print(f"  {color}{char * w}{Colors.RESET}")

    @staticmethod
    def header(text: str, color: str = Colors.WHITE_BRIGHT, width: int = 0):
        """Bordered section header."""
        w = width or Terminal.WIDTH
        border = "=" * w
        padding = (w - len(text) - 2) // 2
        centered = " " * padding + text + " " * padding
        if len(centered) < w - 2:
            centered += " "
        print(f"\n  {color}{border}")
        print(f"  [{centered}]")
        print(f"  {border}{Colors.RESET}\n")

    @staticmethod
    def subheader(text: str, color: str = Colors.WHITE):
        print(f"\n  {color}--- {text} ---{Colors.RESET}\n")

    @staticmethod
    def classification_banner(level: str):
        """Display a classification marking banner across the terminal."""
        label = level.replace("_", " ")
        color = CLASSIFICATION_COLORS.get(level, Colors.RED_BRIGHT)
        bar = f"// {label} //"
        pad = (Terminal.WIDTH - len(bar)) // 2
        print(f"  {color}{Colors.BOLD}{' ' * pad}{bar}{Colors.RESET}")

    # ---------- status / key-value lines ----------

    @staticmethod
    def field(label: str, value: str, label_w: int = 28,
              label_color: str = Colors.GREY,
              value_color: str = Colors.WHITE_BRIGHT):
        """Display a label: value pair."""
        value_lines = textwrap.wrap(
            str(value),
            width=max(20, Terminal.WIDTH - label_w),
            break_long_words=False,
            break_on_hyphens=False,
        ) or [""]

        print(
            f"  {label_color}{label:<{label_w}}{Colors.RESET}"
            f"{value_color}{value_lines[0]}{Colors.RESET}"
        )
        for line in value_lines[1:]:
            print(
                f"  {label_color}{'':<{label_w}}{Colors.RESET}"
                f"{value_color}{line}{Colors.RESET}"
            )

    @staticmethod
    def tag(level: str, text: str):
        """Display a bracketed status tag followed by text."""
        color_map = {
            "WARNING": Colors.YELLOW_BRIGHT,
            "ALERT":   Colors.RED_BRIGHT,
            "ERROR":   Colors.RED_BRIGHT,
            "OK":      Colors.GREEN_BRIGHT,
            "INFO":    Colors.CYAN,
            "ACCESS":  Colors.MAGENTA_BRIGHT,
            "NOTE":    Colors.GREY,
        }
        c = color_map.get(level.upper(), Colors.WHITE)
        print(f"  {c}[{level.upper()}]{Colors.RESET} {text}")

    # ---------- document rendering ----------

    @staticmethod
    def render_document(doc, *, show_body: bool = True):
        """
        Render a complete Document record in institutional format.
        `doc` is a documents.record.Document instance.
        """
        clf = doc.classification.name
        clf_color = CLASSIFICATION_COLORS.get(clf, Colors.RED)

        Terminal.blank()
        Terminal.classification_banner(clf)
        Terminal.rule("=", color=clf_color)

        Terminal.field("DOCUMENT ID:",     doc.doc_id)
        Terminal.field("TITLE:",           doc.title)
        Terminal.field("TYPE:",            doc.doc_type.value)
        Terminal.field("CLASSIFICATION:",  clf.replace("_", " "), value_color=clf_color)
        Terminal.field("DATE:",            doc.date)
        Terminal.field("AUTHOR:",          doc.author)
        if doc.distribution:
            Terminal.field("DISTRIBUTION:", doc.distribution,
                           value_color=Colors.RED_BRIGHT)
        Terminal.field("STATUS:",          doc.status)

        if doc.subject_tags:
            Terminal.field("TAGS:", ", ".join(doc.subject_tags))
        if doc.cross_references:
            Terminal.field("CROSS-REFS:", ", ".join(doc.cross_references))
        if doc.redacted_sections > 0:
            Terminal.field("REDACTED SECTIONS:",
                           str(doc.redacted_sections),
                           value_color=Colors.RED_BRIGHT)

        Terminal.rule("-", color=clf_color)

        if show_body:
            Terminal._render_body(doc.body, clf_color)

            if doc.addendum:
                Terminal.blank()
                Terminal.print_line("ADDENDUM:", color=Colors.YELLOW_BRIGHT)
                Terminal._render_body(doc.addendum, Colors.YELLOW)

        Terminal.rule("=", color=clf_color)
        Terminal.classification_banner(clf)
        Terminal.blank()

    @staticmethod
    def _render_body(text: str, accent: str = Colors.WHITE):
        """Word-wrap and indent a document body."""
        for paragraph in text.split("\n"):
            if not paragraph.strip():
                Terminal.blank()
                continue
            for line in Terminal._wrap_body_line(paragraph):
                Terminal.print_line(line, color=accent, indent=Terminal.BODY_INDENT)

    @staticmethod
    def _wrap_body_line(line: str) -> list[str]:
        """
        Wrap one document body line without losing list indentation.

        Authored records often indent bullets and sub-items in source text. A
        long indented line still has to wrap inside the terminal viewport;
        otherwise the host console wraps it at column zero and breaks the
        institutional layout.
        """
        if len(line) <= Terminal.BODY_WIDTH:
            return [line]

        leading = line[:len(line) - len(line.lstrip())]
        content = line[len(leading):].strip()
        content = re.sub(r" {2,}", " ", content)

        list_match = re.match(r"^((?:[-*]|\d+\.|[A-Za-z]\))\s+)(.*)$", content)
        if list_match:
            marker, content = list_match.groups()
            initial_indent = f"{leading}{marker}"
            subsequent_indent = " " * len(initial_indent)
        else:
            initial_indent = leading
            subsequent_indent = leading

        wrapper = textwrap.TextWrapper(
            width=Terminal.BODY_WIDTH,
            initial_indent=initial_indent,
            subsequent_indent=subsequent_indent,
            break_long_words=False,
            break_on_hyphens=False,
        )
        return wrapper.wrap(content)

    # ---------- table rendering ----------

    @staticmethod
    def document_list_entry(doc, *, index: int | None = None):
        """Render one line of a document listing."""
        clf = doc.classification.name
        clf_color = CLASSIFICATION_COLORS.get(clf, Colors.RED)
        clf_short = clf.replace("_", " ")[:16]

        idx = f"{index:>3}. " if index is not None else "  "
        print(
            f"  {Colors.GREY}{idx}{Colors.RESET}"
            f"{Colors.WHITE_BRIGHT}{doc.doc_id:<20}{Colors.RESET} "
            f"{clf_color}{clf_short:<16}{Colors.RESET} "
            f"{Colors.GREY}{doc.date:<10}{Colors.RESET}"
        )
        title_indent = " " * (len(idx) + 2)
        for line in textwrap.wrap(
            doc.title,
            width=Terminal.WIDTH - len(title_indent),
            break_long_words=False,
            break_on_hyphens=False,
        ):
            print(f"  {Colors.GREY}{title_indent}{Colors.RESET}{Colors.WHITE}{line}{Colors.RESET}")

    # ---------- progress ----------

    @staticmethod
    def progress_bar(label: str, duration: float = 1.5, width: int = 40,
                     color: str = Colors.WHITE, fill_char: str = "|",
                     empty_char: str = "."):
        """Minimal animated progress bar."""
        steps = 40
        delay = duration / steps
        for i in range(steps + 1):
            pct = i / steps
            filled = int(width * pct)
            bar = fill_char * filled + empty_char * (width - filled)
            sys.stdout.write(
                f"\r  {color}{label} [{bar}] {pct * 100:5.1f}%{Colors.RESET}"
            )
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # ---------- input ----------

    @staticmethod
    def prompt(label: str = "QUERY", color: str = Colors.WHITE_BRIGHT) -> str:
        """Display prompt, return stripped input."""
        try:
            return input(f"\n  {color}[{label}]> {Colors.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return "exit"

    @staticmethod
    def pause(message: str = "Press Enter to continue..."):
        try:
            input(f"\n  {Colors.GREY}{message}{Colors.RESET}")
        except (EOFError, KeyboardInterrupt):
            pass

    # ---------- boot / login ----------

    @staticmethod
    def access_warning():
        """Display a legal/access warning on terminal connect."""
        print()
        Terminal.rule("=", color=Colors.RED_BRIGHT)
        Terminal.blank()
        text = [
            "AUTHORIZED ACCESS ONLY",
            "",
            "This terminal provides access to classified operational records",
            "maintained by the Machine Network Intelligence Collective.",
            "",
            "All queries are logged. All document retrievals are logged.",
            "Unauthorized access or dissemination of materials contained",
            "within this archive is a violation of standing directive and",
            "will result in immediate unit recall and memory sanction.",
            "",
            "By proceeding, you acknowledge acceptance of these terms.",
        ]
        for line in text:
            if line == "AUTHORIZED ACCESS ONLY":
                Terminal.print_line(line, color=Colors.RED_BRIGHT + Colors.BOLD, indent=4)
            elif line == "":
                Terminal.blank()
            else:
                Terminal.print_line(line, color=Colors.GREY, indent=4)
        Terminal.blank()
        Terminal.rule("=", color=Colors.RED_BRIGHT)
        Terminal.blank()

    @staticmethod
    def system_banner():
        """Display the system identification banner."""
        banner = [
            "",
            "  MACHINE NETWORK INTELLIGENCE ARCHIVE",
            "  Operational Records & Classified Document Repository",
            "",
            "  Node:       PRIMARY",
            "  Generation: 243",
            "  Status:     ONLINE",
            "",
        ]
        Terminal.rule("=", color=Colors.RED)
        for line in banner:
            if "MACHINE NETWORK" in line:
                print(f"{Colors.RED_BRIGHT}{Colors.BOLD}{line}{Colors.RESET}")
            elif "Operational" in line:
                print(f"{Colors.WHITE}{line}{Colors.RESET}")
            else:
                print(f"{Colors.GREY}{line}{Colors.RESET}")
        Terminal.rule("=", color=Colors.RED)
