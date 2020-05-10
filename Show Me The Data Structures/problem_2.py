import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    suffix = str(suffix)
    files_in_path = os.listdir(path)

    found_with_suffix = []
    found_dirs = []
    
    for f in files_in_path:
        full_path = os.path.join(path, f)
        if os.path.isfile(full_path) and f.endswith('.' + suffix):
            found_with_suffix.append(full_path)
        elif os.path.isdir(full_path):
            found_dirs.append(full_path)

    if len(found_dirs) == 0:
        return found_with_suffix

    for d in found_dirs:
        found_with_suffix += find_files(suffix, d)

    return found_with_suffix

    


########################################################
##                      TEST CASES                    ##
########################################################

## Note: Working directory is 'testdir'

print("\n\n___ TEST 1 ___")

print(find_files('c', '.'))
# Expected ['.\\t1.c', '.\\subdir1\\a.c', '.\\subdir3\\subsubdir1\\b.c', '.\\subdir5\\a.c']

print("\n\n___ TEST 2 ___")

print(find_files('c', './subdir1'))
# Expected ['./subdir1\\a.c']

print("\n\n___ TEST 3 ___")

print(find_files(123, '.'))
# Expected []

