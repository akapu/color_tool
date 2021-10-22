import color
import os

class TestLine:
    def test_no_fix(self, capsys):
        no_fix_lines = ("love.graphics.draw(gTextures['background'], "
                "backgroundX, 0)",
                "love.graphics.setColor(some_color, 255, 255, 255)")
        statuses = ('ok\n', 'ok\n', 'warning\n')

        for line, status in zip(no_fix_lines, statuses):
            assert color.fix_line(line) == line
            captured = capsys.readouterr()
            assert captured.out == status

    def test_simple_fix(self, capsys):
        simple_line = "love.graphics.setColor(255, 255, 255, 255)"
        fixed_simple_line = "love.graphics.setColor(1.00, 1.00, 1.00, 1.00)"

        assert color.fix_line(simple_line) == fixed_simple_line
        captured = capsys.readouterr()
        assert captured.out == 'ok\n'

    def test_complex_fix(self, capsys):
        complex_line = "love.graphics.setColor(255, 255, some_color, 255)"
        fixed_complex_line = ("love.graphics.setColor(1.00, 1.00, "
                "some_color, 255)")

        assert color.fix_line(complex_line) == fixed_complex_line
        captured = capsys.readouterr()
        assert captured.out == 'warning\n'

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
        color.fix_folder('test')
        assert check_folder('test', 'test-out')

class TestFoldername:
    def test_outfolder(self):
        foldernames = ['a', 'a/', 'a/b/c']
        outfoldernames = ['a-out', 'a-out', 'a-out/b/c']

        for foldername, outfoldername in zip(foldernames, outfoldernames):
            assert color.outfolder(foldername) == outfoldername

def check_folder(left, right):
    with os.scandir(left) as lefts:
        with os.scandir(right) as rights:
            lefts_names = {entity.name for entity in lefts}
            rights_names = {entity.name for entity in rights}

            if lefts_names != rights_names:
                return False

            sdirs = (sdir.name for sdir in rights if sdir.is_dir())

            for sdir in sdirs:
                nleft = left + '/' + sdir
                nright = right + '/' + sdir
                if not check_folder(nleft, nright):
                    return False

            return True


