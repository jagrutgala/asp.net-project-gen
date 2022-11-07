from typing import Callable, Dict
import argparse

ParserBuilderFuncType = Callable[[], argparse.ArgumentParser]


class ParserBuilder:
    def __init__(self) -> None:
        self.parser_map: Dict[str, ParserBuilderFuncType] = dict()

    def register_builder(self, name: str, build_func: ParserBuilderFuncType):
        self.parser_map[name] = build_func

    def unregister_builder(self, name: str):
        self.parser_map.pop(name)

    def build_parser(self, name:str) -> argparse.ArgumentParser:
        return self.parser_map.get(name)()


def get_model_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N",  "--namespace_name", type=str,
                        action="store", dest="namespace_name", required=True)
    parser.add_argument("-O", "--output_path", type=str,
                        action="store", dest="output_path", required=True)

    parser.add_argument("-i", action="store_false",
                        dest="do_injection", required=False)

    parser.add_argument("classnames", type=str, metavar='N', nargs="+")

def get_controller_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N",  "--namespace_name", type=str,
                        action="store", dest="namespace_name", required=True)
    parser.add_argument("-O", "--output_path", type=str,
                        action="store", dest="output_path", required=True)

    parser.add_argument("-i", action="store_false",
                        dest="do_injection", required=False)
    parser.add_argument("-e", action="store_true",
                        dest="keep_empty", required=False)

    parser.add_argument("classnames", type=str, metavar='N', nargs="+")

def get_service_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N",  "--namespace_name", type=str,
                        action="store", dest="namespace_name", required=True)
    parser.add_argument("-O", "--output_path", type=str,
                        action="store", dest="output_path", required=True)

    parser.add_argument("-i", action="store_false",
                        dest="do_injection", required=False)
    parser.add_argument("-e", action="store_true",
                        dest="keep_empty", required=False)

    parser.add_argument("classnames", type=str, metavar='N', nargs="+")

def get_context_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N",  "--namespace_name", type=str,
                        action="store", dest="namespace_name", required=True)
    parser.add_argument("-O", "--output_path", type=str,
                        action="store", dest="output_path", required=True)
    parser.add_argument("--Db", type=str, action="store",
                        dest="db_context", required=False)

    parser.add_argument("-i", action="store_false",
                        dest="do_injection", required=False)
    parser.add_argument("-e", action="store_true",
                        dest="keep_empty", required=False)

    parser.add_argument("classnames", type=str, metavar='N', nargs="+")

def get_context_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-N",  "--namespace_name", type=str,
                        action="store", dest="namespace_name", required=True)
    parser.add_argument("-O", "--output_path", type=str,
                        action="store", dest="output_path", required=True)
    parser.add_argument("--Db", type=str, action="store",
                        dest="db_context", required=False)

    parser.add_argument("-i", action="store_false",
                        dest="do_injection", required=False)
    parser.add_argument("-e", action="store_true",
                        dest="keep_empty", required=False)

    parser.add_argument("classnames", type=str, metavar='N', nargs="+")

def get_command_parser() -> argparse.ArgumentParser:
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("-N",  "--namespace_name", type=str,
                           action="store", dest="namespace_name", required=True)
    my_parser.add_argument("-O", "--output_path", type=str,
                           action="store", dest="output_path", required=True)
    my_parser.add_argument("classnames", type=str, metavar='N', nargs="+")

    return my_parser

def get_query_parser() -> argparse.ArgumentParser:
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("-N",  "--namespace_name", type=str,
                           action="store", dest="namespace_name", required=True)
    my_parser.add_argument("-O", "--output_path", type=str,
                           action="store", dest="output_path", required=True)
    my_parser.add_argument("classnames", type=str, metavar='N', nargs="+")

    return my_parser
