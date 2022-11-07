import pathlib

from file_generator import FileGenerator, FileGeneratorOptions

# program command [options]


def make_command():
    base_path = ""
    common_tags = ["#{namespace}", "#{cls}"]
    command_file_options = FileGeneratorOptions(
        template_path= pathlib.Path(),
        replace_tags=common_tags,
        replace_strings=["", "Command"],
        output_directory="",
        filename=""
    )

    command_file_generator = FileGenerator(command_file_options)
    command_file_generator.create_file()

    handler_file_options = FileGeneratorOptions(
        template_path="./templates/cqrs/cqrs_command_handler.txt",
        replace_tags=[],
        replace_strings=[],
        output_directory="",
        filename=""
    )

    handler_file_generator = FileGenerator(handler_file_options)
    handler_file_generator.create_file()

    dto_file_options = FileGeneratorOptions(
        template_path="./templates/cqrs/cqrs_command_dto.txt",
        replace_tags=[],
        replace_strings=[],
        output_directory="",
        filename=""
    )

    dto_file_generator = FileGenerator(dto_file_options)
    dto_file_generator.create_file()


def main():
    make_command()


if __name__ == "__main__":
    # Code Here
    main()
