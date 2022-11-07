import pathlib
import re
from dataclasses import dataclass
from typing import List
import helper


@dataclass
class FileGeneratorOptions:
    template_path: str | pathlib.Path
    replace_tags: List[str]
    replace_strings: List[str]
    output_directory: str
    filename: str


class FileGenerator:
    def __init__(self, file_generator_options: FileGeneratorOptions):
        self.__options = file_generator_options

    @property
    def options(self):
        return self.__options

    def read_template(self) -> str:
        return helper.read_filedata(self.options.template_path)

    def create_file(self) -> None:
        template_data: str = self.read_template()
        for tag in self.options.replace_tags:
            template_data = re.sub(tag, "", template_data)
        with open(f"{self.options.output_directory}/{self.options.filename}", "w") as f:
            f.write(template_data)
