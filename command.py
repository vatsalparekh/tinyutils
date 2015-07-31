import subprocess


def fire(command):

    # Using subprocess.Popen() we can execute a Linux command from within
    # Python. The full command redirects the output in variable 'output' and
    # errors, if any, to 'err' variable

    output, err = subprocess.Popen(
        command.split(" "), stdout=subprocess.PIPE).communicate()

    # 'output' variable has data in bytes. We want to have string. Using
    # decode() method we can convert it by specifying appropriate encoding

    if err is None:
        output = only_elements(output.decode("utf-8").split("\n"))

    return output


def only_elements(input_list):

    output_list = []

    tmp = [elements.strip() for elements in input_list]

    for objects in tmp:
        for elements in objects.split(" "):
            if elements != '':
                output_list.append(elements)

    return output_list
