import armgrader
import random

class TestGrader(armgrader.ARMGrader):
    def tests(self):
        self.generateHeaders(
            main_file="/grade/tests/main.c",
            memory_map=self.data['params']['memoryMap'],
            functions=f"#define NUM_INPUTS {self.data['params']['length']}\n"
        )
        
        # compiles the program. student_file is the name of the student's code file, it gets copied to /grade/tests for compilation
        self.make(student_file="student.s")
        # runs the program and tests against exp_output. you can use the same arguments as any other test_run call.
        input = []
        exp_output = []
        max = 0
        for _ in range(self.data['params']['length']):
            x_i = random.randint(11, 255)
            input.append(str(x_i))
            max = x_i if (x_i > max if self.data['params']['minmax'] == 'MAXIMUM' else x_i < max) else max
        exp_output.append(f"minmax={max}\n")
        self.test_make_run(input="\n".join(input), exp_output=exp_output, highlight_matches=True, must_match_all_outputs=True, name='Testing with random inputs')
    
g = TestGrader()
g.start()
