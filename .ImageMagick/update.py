#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Tools"))

from dependency_updater import Step, Updater

GITHUB_URL = "https://github.com/freetype/freetype/archive/refs/tags/VER-{version_dash}.tar.gz"
SOURCE_URL = "https://download.savannah.gnu.org/releases/freetype/freetype-{version}.tar.xz"


def update_source(updater):
    updater.replace_source(SOURCE_URL)
    updater.remove(".github")
    updater.update_config()


updater = Updater(__file__, "freetype", GITHUB_URL)
updater.run([
    Step("Replace the source with the release and update Config.txt", update_source,
        "Updated FreeType to {version}"),
    updater.clone_dependencies_step(),
])
