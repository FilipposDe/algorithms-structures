find_files() works recursively, because of the nature of directory structure (directories inside directories with no limit to the depth).

For the worst case, we assume there are n files total and m levels of directories that contain k directories each. That is a total of k^m directories. Each directory contains n/(k^m) files on average.

On one execution, the function runs once for the directory T(1). In each directory, it iterates n/(k^m) times for each file. It also iterates through contained directories (assumed to be k). So for one directory it takes time: T(n/k^m + k). This runs k^m times. So overall it is O( k^m * ( n/k^m + k) ) = O(n+k^(m+1)) or O(n+k^m) or: O(k^m)

Space complexity is (n) for n files / directories in each directory.