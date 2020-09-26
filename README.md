# Overview

This is a guide of compiling softwares with [LLVM](https://github.com/llvm/llvm-project) using [Git Bash](https://github.com/git-for-windows/git) shell. 

Note: you may also consier the [MSYS2](https://www.msys2.org/) project if you want to go further and drop the dependency on Windows SDK, check [llvm-mingw](https://github.com/mstorsjo/llvm-mingw.git) for a working version of LLVM-MINGW toolchain.

## Prerequisites

* [Git Bash](https://gitforwindows.org/) (you may also consider the built-in Git Bash in [cmder](https://github.com/cmderdev/cmder/releases))
* [LLVM](https://github.com/llvm/llvm-project/releases)
* [Python](https://www.python.org/downloads/): and `pandas` package.
* [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) : Minimally, you should install the latest individual component `MSVC v142 -VS 2019 C++ x64/x86 build tools`)
* [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/): if you prefer to install Windows SDK without Visual studio installer

Optional recommendations:

* [Scoop](https://github.com/lukesampson/scoop): to manage software packages, not working for Visual Studio and Windows SDK at the moment
* [CMake](https://cmake.org/download)
* [Ninja](https://github.com/ninja-build/ninja/releases)

## Quick start

The quick start guide assume these install location in Git bash notation:

Scoop: `/d/packages/scoop`
MSVC build tool: `/d/Program/MSVC`
Windows SDK: `/d/Program/WindowsSDK`
Directory for storing script: `/d/EnvScripts`

Modify them to suit your need. They should be located in your C drive or D drive and there shouldn't be any spaces in the name, such as `Program Files`, else you have to modify the python script to translate the name.

First, install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/).

Install scoop: open powershell and run 
```
$env:SCOOP='D:\packages\scoop'
$env:SCOOP_GLOBAL='D:\packages\scoopGlobal'
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```

Install cmder (with git bash)
```
scoop install cmder-full
```

Open cmder, change `settings > Startup > Specified named task` to `{bash::bash}`
Add the following to `~/.bashrc`
```
export SCOOP=/d/packages/scoop
export SCOOP_GLOBAL=/d/packages/scoopGlobal
```


Close and reopen cmder, install python, llvm, ninja, cmake
```
scoop install python llvm ninja cmake
```

Close and reopen cmder, install pandas
```
pip install pandas
```

Output all the environment in from the native tools command prompt for VS 2019 to `EnvVar.csv` in the script directory
```
cd /d/EnvScripts
cmd "/C D:\Program\MSVC\VC\Auxiliary\Build\vcvars64.bat & env > EnvVar.csv"
```

Convert the Windows path into Git bash's path by the [python script](script/python/env_translate.py)
```
curl -O https://raw.githubusercontent.com/Adriankhl/llvm-git-bash/master/script/python/env_translate.py
python env_translate.py EnvVar.csv
```

2 files will be generated: 

* `env_full.sh`: Converted Git Bash format of environment variables, some of them are removed since their variable name contain invalid characters, such as `(x86).
* `env.sh`: export `PATH`, `LIB`, and `INCLUDE` in Git Bash format, only contain minimal stuffs for llvm to work.

## How to use the files generated
You can add `source /d/EnvScripts/env.sh` to your `~/.bashrc` file

Besides, add 
```
export CC=clang-cl
export CXX=clang-cl
```
for cmake to prefer `clang-cl` compiler

## Examples

Here are some examples that can be successfully built by `clang-cl`, feel free to add more

* [Aseprite](examples/Aseprite.md)
* [Godot](examples/Godot.md)
* [minetest](examples/minetest.md)
