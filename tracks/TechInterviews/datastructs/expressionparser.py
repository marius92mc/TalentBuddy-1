import re

def perform_op(a, op, b):
    return a + b if op == "+" else a - b

def replace(match):
    return str(perform_op(int(match.group(1)), match.group(2), int(match.group(3))))

def compute_expression(expr):
    while not re.match("^-?\d+$", expr):
        expr = re.sub(r"(-?\d+)([+\-])(-?\d+)", replace, expr)
        expr = re.sub(r"\((-?\d+)\)", "\\1", expr)
        # print "Currently: %s\n" % expr
    print expr
