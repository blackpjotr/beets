from typing import Literal

EventType = Literal[
    "pluginload",
    "import",
    "album_imported",
    "album_removed",
    "item_copied",
    "item_imported",
    "before_item_moved",
    "item_moved",
    "item_linked",
    "item_hardlinked",
    "item_reflinked",
    "item_removed",
    "write",
    "after_write",
    "import_task_created",
    "import_task_start",
    "import_task_apply",
    "import_task_before_choice",
    "import_task_choice",
    "import_task_files",
    "library_opened",
    "database_change",
    "cli_exit",
    "import_begin",
    "trackinfo_received",
    "albuminfo_received",
    "before_choose_candidate",
    "mb_track_extract",
    "mb_album_extract",
]
