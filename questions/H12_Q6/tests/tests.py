import armgrader
import random

class TestGrader(armgrader.ARMGrader):
    def tests(self):
        self.generateHeaders(
            main_file="/grade/tests/main.c",
            memory_map=self.data['params']['memoryMap'],
            functions=f"#define NUM_INPUTS {self.data['params']['length']}"
        )
        
        # compiles the program. student_file is the name of the student's code file, it gets copied to /grade/tests for compilation
        self.make(student_file="student.s")
        # runs the program and tests against exp_output. you can use the same arguments as any other test_run call.
        input = []
        exp_output = []
        length = self.data['params']['length']
        for i in range(length):
            x_i = random.randint(10, 255)
            exp_output.append(f"Y[{i}]={x_i}\n")
            input.append(str(x_i))
        for i in range(10-length):
            exp_output.append(f"Y[{i+length}]={i+length}\n")
        self.test_make_run(input="\n".join(input), exp_output=exp_output, highlight_matches=True, must_match_all_outputs=True, name='Testing with random inputs')
    
g = TestGrader()
g.start()
