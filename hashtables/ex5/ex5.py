def finder(files, queries):
    cache = {}
    result = []
    for path in files:
        key = path.split('/')[-1]
        if key in cache:
            cache[key] = [*cache[key],path]
        else:
            cache[key] = [path]
    for name in queries:
        if name in cache:
            result.extend(cache[name])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
