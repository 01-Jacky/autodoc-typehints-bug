class Foo:
    """Class to demo a bug"""

    def __init__(self, magic_num: int) -> None:
        """Creates the Foo

        :param magic_num: some magic number

        """
        self.magic_num = magic_num
