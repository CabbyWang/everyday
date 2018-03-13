def unCompress(file_name):
    """ungz zip file"""
    import gzip
    f_name = file_name.replace(".gz", "")
    try:
        with open(file_name, 'rb') as f:
            g = gzip.GzipFile(mode='rb', fileobj=f)
            content = g.read()
        with open(f_name, 'wb') as fp:
            fp.write(content)
    except OSError:
        print('the file {} failed!!'.format(file_name))


if __name__ == '__main__':
    pass