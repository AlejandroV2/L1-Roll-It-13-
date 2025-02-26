def make_statement(statement, decoration):
    """Adds/ emoji / additional character to the start and en of headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# Main routine
make_statement(statement="ts pmo rn icl", decoration="💔")
make_statement(statement="Round Results", decoration="=")
