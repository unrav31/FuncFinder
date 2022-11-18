# FuncFinder
Find function by function name in libc path.

This tool use `grep -r` and `nm -D` command to find symbols in given libc path, parse results and return the library name.

Useage:

```bash
funcFinder.py -l [PATH] -s [symbol name]
```

Example 1:

```bash
python3 funcFinder.py -l /lib/x86_64-linux-gnu/libc.so.6 -s read
```

results：

```text
[...] Checking /lib/x86_64-linux-gnu/libc.so.6
[ * ] Find funciton in : /lib/x86_64-linux-gnu/libc.so.6
```

Example 2:

```bash
python3 funcFinder.py -l ./lib -s hs_debug_print
```

results:

```text
[...] Checking ./lib/libhostid.so
[...] Checking ./lib/libuser_mapping.so.1
[...] Checking ./lib/libhcd.so.1
[...] Checking ./lib/libhostid.so.1
[...] Checking ./lib/libadmin.so
[...] Checking ./lib/libtif.so.1
[...] Checking ./lib/libamproxyd.so.1
[...] Checking ./lib/libaddrpool.so.1
[...] Checking ./lib/libap_receiver.so
[...] Checking ./lib/libcloud.so.1
[...] Checking ./lib/libnetd.so.1
[...] Checking ./lib/libstat.so
[...] Checking ./lib/libstat.so.1
[...] Checking ./lib/libmix.so.1
[...] Checking ./lib/libnetd.so
[...] Checking ./lib/libauth.so.1
[...] Checking ./lib/libsche.so.1
[...] Checking ./lib/libendpoint_tag.so.1
[...] Checking ./lib/libap_receiver.so.1
[...] Checking ./lib/libaddrpool.so
[...] Checking ./lib/libsche.so
[...] Checking ./lib/libcloud.so
[...] Checking ./lib/libamproxyd.so
[...] Checking ./lib/libauth.so
[...] Checking ./lib/libhcd.so
[...] Checking ./lib/libmix.so
[...] Checking ./lib/libsyslog.so.1
[ * ] Find funciton in : ./lib/libsyslog.so.1
[...] Checking ./lib/libtif.so
[...] Checking ./lib/libmail.so
[...] Checking ./lib/libdev.so.1
[...] Checking ./lib/libdev.so
[...] Checking ./lib/libsyslog.so
[ * ] Find funciton in : ./lib/libsyslog.so
[...] Checking ./lib/libuser_mapping.so
[...] Checking ./lib/libendpoint_tag.so
[...] Checking ./lib/libmail.so.1
[...] Checking ./lib/libadmin.so.1
```

