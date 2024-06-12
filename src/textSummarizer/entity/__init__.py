from dataclasses import dataclass
from pathlib import Path
import sys
import os

# Add the src directory to the Python path
current_working_directory = os.getcwd()
src_directory = os.path.join(current_working_directory, '/Users/aneeshgrover/PROJECTS/Text-Summarizer-Project/src')
sys.path.insert(0, src_directory)

from textSummarizer.utils.common import read_yaml, create_directories

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list