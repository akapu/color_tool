import color

class TestLine:
    def test_no_fix(self):
        no_fix_lines = ("love.graphics.draw(gTextures['background'], "
                "backgroundX, 0)",
                "love.graphics.setColor(some_color, 255, 255, 255)")

        for line in no_fix_lines:
            assert color.fix_line(line) == line

    def test_simple_fix(self):
        simple_line = "love.graphics.setColor(255, 255, 255, 255)"
        fixed_simple_line = "love.graphics.setColor(1.00, 1.00, 1.00, 1.00)"

        assert color.fix_line(simple_line) == fixed_simple_line

    def test_complex_fix(self):
        complex_line = "love.graphics.setColor(255, 255, some_color, 255)"
        fixed_complex_line = ("love.graphics.setColor(1.00, 1.00, "
                "some_color, 255)")

        assert color.fix_line(complex_line) == fixed_complex_line

class TestNumber:
    def test_fix_number(self):
        numbers = ('255', '0', '128')
        fixed_numbers = (' 1.00', ' 0.00', ' 0.50')

        for number, fixed_number in zip(numbers, fixed_numbers):
            assert color.fix_number(number) == fixed_number

class TestFile:
    def test_file(self):
        with open("test-out.lua") as outfile:
            for line in color.fix_file("test.lua"):
                assert line == outfile.readline()

class TestFolder:
    def test_folder(self):
        raise Exception()

class TestFoldername:
    def test_outfolder(self):
        foldernames = ['a', 'a/', 'a/b/c']
        outfoldernames = ['a-out', 'a-out/', 'a-out/b/c']

        for foldername, outfoldername in zip(foldernames, outfoldernames):
            assert color.outfolder(foldername) == outfoldername
