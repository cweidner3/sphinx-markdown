
import sys

def file_readline(filepath):
    '''
    :param filepath (str): Path to file to read.
    :returns: Contents of file as string.
    '''
    with open(filepath) as handle:
        if sys.version_info.major == 2:
            data = handle.readline()
            data = unicode(data.decode('utf-8'))
        else:
            data = handle.read()
    return data

def file_write(filepath, text, encoding):
    '''
    :param filepath (str): Path to file to write.
    :param text (str): Contents to write.
    :param encoding (str): The output encoding.
    '''
    with open(filepath, 'w') as writer:
        if sys.version_info.major == 2:
            text = (text.encode(encoding, 'ignore'))
        writer.write(text)
