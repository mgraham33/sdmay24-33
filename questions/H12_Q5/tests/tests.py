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
        for i in range(3):
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c = random.randint(0, 9)
            d = random.randint(0, 9)

            sign = self.data['params']['comparison_ab']
            if sign == '<':
                ab = a < b
            elif sign == '>':
                ab = a > b
            elif sign == '<=':
                ab = a <= b
            elif sign == '>=':
                ab = a >= b

            sign = self.data['params']['comparison_cd']
            if sign == '<':
                cd = c < d
            elif sign == '>':
                cd = c > d
            elif sign == '<=':
                cd = c <= d
            elif sign == '>=':
                cd = c >= d

            logic = self.data['params']['logic']
            if logic == '&&':
                flag = ab and cd
            else:
                flag = ab or cd

            ans_flag = 1 if flag else 0
            exp_output.append(f"{i}: flag={ans_flag}\n")
            input.append(f'{a} {b} {c} {d}')
        self.test_make_run(input="\n".join(input), exp_output=exp_output, highlight_matches=True, must_match_all_outputs=True, name='Testing with random inputs')
    
g = TestGrader()
g.start()
