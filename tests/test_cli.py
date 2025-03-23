import unittest
from src.nomina.cli.make_parser import make_parser


class TestCli(unittest.TestCase):
    def setUp(self):
        self.parser = make_parser()
        self.valid_package_name = ["numpy", "requests"]

    def test_valid_single_package(self):
        args = self.parser.parse_args([self.valid_package_name[0]])
        self.assertEqual(args.name, [self.valid_package_name[0]])

if __name__ == "__main__":
    unittest.main()
