import cgrader
import random

testhtext = """
#ifndef TEST_H_
#define TEST_H_

"""

class TestGrader(cgrader.CGrader):
    def tests(self):
        global testhtext
        for i in range(3):
            testhtext += f"#define TODO{i+1} {self.data['submitted_answers'][f'q{i+1}']}\n"
        testhtext += "#endif"
        with open("/grade/tests/test.h", "w") as testh:
            testh.write(testhtext)

        self.compile_file("/grade/tests/main.c", "main", add_c_file=[
            "/grade/tests/answer.c",
            "/grade/tests/test.c"
        ])

        maskOnes = self.data['params']['maskOnes']
        maskZeroes = self.data['params']['maskZeroes']

        with open('inputs.txt', 'w') as datafile:
            datafile.write(f"{maskOnes}\n{maskZeroes}\n")

        self.test_run('./main', '1\n', exp_output="QUESTION 1 PASSED\n", name="Testing 'q1'")
        self.test_run('./main', '2\n', exp_output="QUESTION 2 PASSED\n", name="Testing 'q2'")
        self.test_run('./main', '3\n', exp_output="QUESTION 3 PASSED\n", name="Testing 'q3'")

g = TestGrader()
g.start()
