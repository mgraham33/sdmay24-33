import cgrader
import random

testhtext = """
#ifndef TEST_H_
#define TEST_H_

"""

class TestGrader(cgrader.CGrader):
    def tests(self):
        global testhtext
        for i in range(4):
            testhtext += f"#define TODO{i+1} {self.data['submitted_answers'][f'q{i+1}']}\n"
        testhtext += "#endif"
        with open('/grade/tests/test.h', 'w') as testh:
            testh.write(testhtext)
        
        self.compile_file("/grade/tests/main.c", "main", add_c_file=[
            "/grade/tests/answer.c",
            "/grade/tests/test.c"
        ])
        
        inputs = self.data['params']['inputs_part1']

        with open('inputs.txt', 'w') as datafile:
            datafile.write(str(inputs[0]) + "\n")
        self.test_run("./main", "1\n", exp_output="QUESTION 1 PASSED\n", name="Testing 'q1'")

        with open('inputs.txt', 'w') as datafile:
            datafile.write("\n".join(map(str, inputs[1:4])) + "\n")
        self.test_run("./main", "2\n", exp_output="QUESTION 2 PASSED\n", name="Testing 'q2'")

        with open('inputs.txt', 'w') as datafile:
            datafile.write("\n".join(map(str, inputs[4:8])) + "\n")
        self.test_run("./main", "3\n", exp_output="QUESTION 3 PASSED\n", name="Testing 'q3'")

        with open('inputs.txt', 'w') as datafile:
            datafile.write(str(inputs[8]) + "\n")
        self.test_run("./main", "4\n", exp_output="QUESTION 4 PASSED\n", name="Testing 'q4'")
    
g = TestGrader()
g.start()
