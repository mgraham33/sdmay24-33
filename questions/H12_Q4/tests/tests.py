import armgrader
import random

class TestGrader(armgrader.ARMGrader):
    def tests(self):
        self.generateHeaders(
            # sets main file to add these headers to
            main_file="/grade/tests/main.c", # default /grade/tests/main.c
            # fill in variables in the c code
            memory_map=self.data['params']['memoryMap']
        )
        
        # compiles the program. student_file is the name of the student's code file, it gets copied to /grade/tests for compilation
        self.make(student_file="student.s")
        # runs the program and tests against exp_output. you can use the same arguments as any other test_run call.
        input = []
        exp_output = []
        b = self.data['params']['immed']
        for i in range(5):
            a = random.randint(0, 255)
            ans_flag = -1
            sign = self.data['params']['comparison']
            if sign == '<':
                ans_flag = 0 if a < b else 1
            elif sign == '>':
                ans_flag = 0 if a > b else 1
            elif sign == '<=':
                ans_flag = 0 if a <= b else 1
            elif sign == '>=':
                ans_flag = 0 if a >= b else 1
            exp_output.append(f"{i}: flag={ans_flag}\n")
            input.append(f'{a}')
        self.test_make_run(input="\n".join(input), exp_output=exp_output, highlight_matches=True, must_match_all_outputs=True, name='Testing with random inputs')
    
g = TestGrader()
g.start()
