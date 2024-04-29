import armgrader
import random

class TestGrader(armgrader.ARMGrader):
    def tests(self):
        self.generateHeaders(
            # sets main file to add these headers to
            main_file="/grade/tests/main.c", # default /grade/tests/main.c
            # fill in variables in the c code
            memory_map=self.data['params']['memoryMap'],
            functions=[f'int A_ind = {self.data["params"]["A_ind"]};\n']
        )
        
        # compiles the program. student_file is the name of the student's code file, it gets copied to /grade/tests for compilation
        self.make(student_file="student.s")
        # runs the program and tests against exp_output. you can use the same arguments as any other test_run call.
        input = []
        exp_output = []
        for i in range(5):
            ch1 = random.randint(0, 255)
            # we do % 256 because if the random value is close to 255, adding anything to it will cause an overflow and wrap to 0
            ans_ch1 = (ch1 + self.data['params']['add_amnt']) % 256
            exp_output.append(f"{i}: A[{self.data['params']['A_ind']}]={ans_ch1}\n")
            input.append(f'{ch1}')
        self.test_make_run(input="\n".join(input), exp_output=exp_output, highlight_matches=True, must_match_all_outputs=True, name='Testing with random inputs')
    
g = TestGrader()
g.start()
