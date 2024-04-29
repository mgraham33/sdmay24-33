import cgrader
import random

# imports from cgrader.CGrader that allows partial_credit_run to work
import json
import os
import pathlib
import re
import shlex
import subprocess
import tempfile

import lxml.etree as ET

class TestGrader(cgrader.CGrader):
    def partial_credit_run( # edited version of test_run that allows partial credit calculation
        self,
        command,
        input=None,
        exp_output=None,
        must_match_all_outputs=False,
        partial_credit=False,
        reject_output=None,
        field=None,
        ignore_case=True,
        timeout=1,
        size_limit=10240,
        ignore_consec_spaces=True,
        args=None,
        name=None,
        msg=None,
        max_points=1,
        highlight_matches=False,
    ):
        if args is not None:
            if not isinstance(args, list):
                args = [args]
            args = list(map(str, args))

        if name is None and input is not None:
            name = 'Test with input "%s"' % " ".join(input.splitlines())
        elif name is None and args is not None:
            name = 'Test with arguments "%s"' % " ".join(args)
        elif name is None and isinstance(command, list):
            name = "Test command: %s" % command[0]
        elif name is None:
            name = "Test command: %s" % command

        if exp_output is None:
            exp_output = []
            must_match_all_outputs = True
        elif not isinstance(exp_output, list):
            exp_output = [exp_output]

        if reject_output is None:
            reject_output = []
        elif not isinstance(reject_output, list):
            reject_output = [reject_output]

        def compile_re(t):
            if isinstance(t, re.Pattern):
                return (t.pattern, t)
            # If t is not a string, convert it to its string representation
            t = str(t)
            return (
                t.strip(),
                re.compile(
                    "\\s+".join(map(re.escape, re.split("\\s+", t)))
                    if ignore_consec_spaces
                    else re.escape(t),
                    re.I if ignore_case else 0,
                ),
            )

        exp_output = [compile_re(t) for t in exp_output]
        reject_output = [compile_re(t) for t in reject_output]

        out = self.run_command(
            command if args is None else ([command] + args),
            input,
            sandboxed=True,
            timeout=timeout,
        )

        outcmp = out
        if highlight_matches and out:
            for _, r in exp_output:
                out = r.sub(r"\033[32m\g<0>\033[0m", out)
            for _, r in reject_output:
                out = r.sub(r"\033[31m\g<0>\033[0m", out)
        if not out:
            out = "(NO OUTPUT)"
        elif not out.endswith("\n"):
            out += "\n(NO ENDING LINE BREAK)"

        if msg is None and exp_output:
            comment = (
                ""
                if len(exp_output) == 1
                else " all of"
                if must_match_all_outputs
                else " one of"
            )
            join_str = "\n\n" if any("\n" in t for t, _ in exp_output) else "\n\t"
            msg = f"Expected{comment}:{join_str}" + join_str.join(
                f"\033[32m{t}\033[0m"
                if highlight_matches and r.search(outcmp) is not None
                else t
                for t, r in exp_output
            )
            if reject_output:
                join_str = (
                    "\n\n" if any("\n" in t for t, _ in reject_output) else "\n\t"
                )
                msg += f"\nBut not:{join_str}" + join_str.join(
                    f"\033[31m{t}\033[0m"
                    if highlight_matches and r.search(outcmp) is not None
                    else t
                    for t, r in reject_output
                )
        elif msg is None:
            msg = ""

        points = max_points
        if timeout and "TIMEOUT" in outcmp:
            points = 0
        elif size_limit and len(outcmp) > size_limit:
            out = out[0:size_limit] + "\nTRUNCATED: Output too long."
            points = 0
        elif partial_credit:
            pts_per_test = max_points / len(exp_output)
            points = 0
            for _, r in exp_output:
                points += pts_per_test if r.search(outcmp) is not None else 0
        elif not (all if must_match_all_outputs else any)(
            r.search(outcmp) is not None for _, r in exp_output
        ) or any(r.search(outcmp) is not None for _, r in reject_output):
            points = 0

        return self.add_test_result(
            name,
            points=points,
            msg=msg,
            output=out,
            max_points=max_points,
            field=field,
        )

    def tests(self):
        self.test_compile_file(["initialize.c"], "main", points=1, add_c_file=[
            "/grade/tests/main.c",
            "/grade/tests/globals.c",
            "/grade/tests/answer.c",
            "/grade/tests/util.c"
        ])

        self.partial_credit_run("./main", exp_output=[
            "Timer initialization succeeded."
        ], reject_output=[
            "Timer initialization failed."
        ], max_points=5, highlight_matches=True, partial_credit=True, msg="")

g = TestGrader()
g.start()
