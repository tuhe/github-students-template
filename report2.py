from unitgrade.framework import Report
from unitgrade.evaluate import evaluate_report_student
from homework1 import add, reverse_list
from unitgrade import UTestCase, cache  # !s
import homework1


class Week1(UTestCase):
    def test_add(self):
        self.assertEqualC(add(2,2))
        self.assertEqualC(add(-100, 5))

    def test_reverse(self):
        self.assertEqualC(reverse_list([1, 2, 3])) #!s

    def test_output_capture(self):
        with self.capture() as out:
            print("hello world 42")                     # Genereate some output (i.e. in a homework script)
        self.assertEqual(out.numbers[0], 42)            # out.numbers is a list of all numbers generated
        self.assertEqual(out.output, "hello world 42")  # you can also access the raw output.

class Week1Titles(UTestCase): #!s=b
    """ The same problem as before with nicer titles """
    def test_add(self):
        """ Test the addition method add(a,b) """
        self.assertEqualC(add(2,2))
        print("output generated by test")
        self.assertEqualC(add(-100, 5))
        # self.assertEqual(2,3, msg="This test automatically fails.")

    def test_reverse(self):
        ls = [1, 2, 3]
        reverse = reverse_list(ls)
        self.assertEqualC(reverse)
        # Although the title is set after the test potentially fails, it will *always* show correctly for the student.
        self.title = f"Checking if reverse_list({ls}) = {reverse}"  # Programmatically set the title #!s

    def ex_test_output_capture(self):
        with self.capture() as out:
            print("hello world 42")                     # Genereate some output (i.e. in a homework script)
        self.assertEqual(out.numbers[0], 42)            # out.numbers is a list of all numbers generated
        self.assertEqual(out.output, "hello world 42")  # you can also access the raw output.


class Question2(UTestCase): #!s=c
    @cache
    def my_reversal(self, ls):
        # The '@cache' decorator ensures the function is not run on the *students* computer
        # Instead the code is run on the teachers computer and the result is passed on with the
        # other pre-computed results -- i.e. this function will run regardless of how the student happens to have
        # implemented reverse_list.
        return reverse_list(ls)

    def test_reverse_tricky(self):
        ls = (2,4,8)
        ls2 = self.my_reversal(tuple(ls))                   # This will always produce the right result, [8, 4, 2]
        print("The correct answer is supposed to be", ls2)  # Show students the correct answer
        self.assertEqualC(reverse_list(ls))                 # This will actually test the students code.
        return "Buy world!"                                 # This value will be stored in the .token file  #!s=c


class Report2(Report):
    title = "CS 106a"
    questions = [(Week1, 10), (Week1Titles, 6)]
    pack_imports = [homework1]

if __name__ == "__main__":
    evaluate_report_student(Report2(), unmute=True)
