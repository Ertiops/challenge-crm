def value_by_key_prefix(d, partial):
    """takes dictionary and a pattern of a key to get the value. Designed for jinja form submit"""
    matches = [val for key, val in d.iteritems() if key.startswith(partial)]
    if not matches:
        raise KeyError(partial)
    if len(matches) > 1:
        raise ValueError('{} matches more than one key'.format(partial))
    return matches[0]