def compile_code_inline(line):
    if line.count('`') == 3:
        return line

    parts = line.split('`')

    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            parts[i] = '<code>' + parts[i] + '</code>'
        return ''.join(parts)

    return line
result = compile_code_inline('alpha `beta` gamma `delta`')
print(result)

