# Overview

This is a guide of compiling softwares with [LLVM](https://github.com/llvm/llvm-project) using [Git Bash](https://github.com/git-for-windows/git) shell. 

<<<<<<< HEAD
Note: you may also consier the [MSYS2](https://www.msys2.org/) project if you want to go further and drop the dependency on Windows SDK, check [llvm-mingw](https://github.com/mstorsjo/llvm-mingw.git) for a working version of LLVM-MINGW toolchain.
=======
Visual Studio comes with an out-of-the-box support of LLVM, cmake, and ninja. However, if you don't want to rely on Microsoft's workflow too much, it is not that easy to configure your environment correctly. This guide provide informations that help you to set up your development environment. 

You still have to use Windows SDK and maybe some other tools from Visual Studio. The motivation of this guide is to minimize the dependency on Microsoft's tools and the Visual Studio IDE, so that you pick your favorite alternative (open source) tools to develop your software, while you should be able to easily go back to the powerful Visual Studio to develop your project if you want to do so. 

Note: you may also consider the [MSYS2](https://www.msys2.org/) project if you want to go further and drop the dependency on Windows SDK, check [llvm-mingw](https://github.com/mstorsjo/llvm-mingw.git) for a working version of LLVM-MINGW toolchain.
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2

## Prerequisites

* [Git Bash](https://gitforwindows.org/) (you may also consider the built-in Git Bash in [cmder](https://github.com/cmderdev/cmder/releases))
* [LLVM](https://github.com/llvm/llvm-project/releases)
<<<<<<< HEAD
* [Python](https://www.python.org/downloads/): and `pandas` package.
* [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) : Minimally, you should install the latest individual component `MSVC v142 -VS 2019 C++ x64/x86 build tools`)
* [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/): if you prefer to install Windows SDK without Visual studio installer
=======
* [Python](https://www.python.org/downloads/) and `pandas` package.
* [Visual Studio](https://visualstudio.microsoft.com/downloads/) (Minimally, you can download `Build Tools for Visual Studio 2019` and install MSVC and Windows 10 SDK, you can also use the bundled cmake, ninja, and LLVM)
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2

Optional recommendations:

* [Scoop](https://github.com/lukesampson/scoop): to manage software packages, not working for Visual Studio and Windows SDK at the moment
* [CMake](https://cmake.org/download)
* [Ninja](https://github.com/ninja-build/ninja/releases)

<<<<<<< HEAD
## Quick start

The quick start guide assume these install location in Git bash notation:

Scoop: `/d/packages/scoop`
MSVC build tool: `/d/Program/MSVC/BuildTools`
Windows SDK: `/d/Program/WindowsSDK`
Directory for storing script: `/d/EnvScripts`
=======
Say you install LLVM in `D:\Program\LLVM`, the path in Git Bash is represented as `/d/Program/LLVM`. The binaries of LLVM should be located inside `/d/Program/LLVM/bin`. Add `export PATH='/d/Program/LLVM/bin':$PATH` in your `~/.bashrc` so that the binaries (`clang.exe`, `lld.exe`, etc.) can be found automatically. Do the same if you installed python, cmake or ninja. You may also add the `Scripts` folder of your python to the `PATH` such that you can use `pip`. Then you can install `pandas` by `pip install pandas`
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2

Modify them to suit your need. They should be located in your C drive or D drive and there shouldn't be any spaces in the name, such as `Program Files`, else you have to modify the python script to translate the name.

<<<<<<< HEAD
First, install the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and [Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/).
=======
Visual Studio 2019 comes with a Developer Powershell, where environment variables are pre-defined. You can view the variables by opening the shell and run:
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2


<<<<<<< HEAD
Install scoop: open powershell and run 
```
$env:SCOOP='D:\packages\scoop'
$env:SCOOP_GLOBAL='D:\packages\scoopGlobal'
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```
=======
Run the following command export the variables into a csv file `Env.csv`.
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2


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


<<<<<<< HEAD
Close and reopen cmder, install python, llvm, ninja, cmake
```
scoop install python llvm ninja cmake
```

Close and reopen cmder, install pandas
```
pip install pandas
```
=======
* `env_original.sh`: Original format of environment variables
* `env_all.sh`: Converted Git Bash format of environment variables, cannot be executed directly since `(x86)` in variable name is not allowed in Git Bash
* `env.sh`: export `PATH`, `LIB`, and `INCLUDE` in Git Bash format
* `env64.sh`: basically `env.sh` where all `x86` are converted to `x64` to use 64bit library (excrept `(x86)` which should only exists in the name `Program Files (x86)`)

Depends on whether you want to build 32bit or 64bit binary, do `source env.sh` or `source env64.sh` in your `~/.bashrc`.
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2

Output all the environment in from the native tools command prompt for VS 2019 to `EnvVar.csv` in the script directory
```
cd /d/EnvScripts
cmd "/C D:\Program\MSVC\BuildTools\VC\Auxiliary\Build\vcvars64.bat & env > EnvVar.csv"
```

Convert the Windows path into Git bash's path by the [python script](script/python/env_translate.py)
```
curl -O https://raw.githubusercontent.com/Adriankhl/llvm-git-bash/master/script/python/env_translate.py
python env_translate.py EnvVar.csv
```

<<<<<<< HEAD
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
=======
After you execute `source env.sh`, some tools that are provided by Git Bash are overrode by the tools provided by Microsoft since they have exactly the same name, such as `find` or `link`. Therefore, it is recommended that you can use alias or bash script to create two commands to change the `PATH` variable - one prepare for the development environment and one return to the original Git Bash environment. You can run something like `llvmdev` before you want to compile your project and run something like `undev` if you want to `find` a file afterwards.

## Examples

As far as I know, not many open source softwares can be successfully compiled if you strictly follow the approach in this guide. For example, if the project is developed based on a `.sln` file, you have no choice but to use `MSBuild` and/or Visual Studio IDE. Fortunately, unlike MinGW, LLVM tools are designed to be an (almost) drop-in replacement of Microsoft's tools, zero or relatively small tweaks are necessary if you want to build CMake or Scons projects which are orginally designed to build with Visual Studio. Here are some examples that can be successfully built, feel free to make more suggestions by PR.
>>>>>>> ef9fc68cd7fc886f240654dabb30a2b5a54ce3d2

* [Aseprite](examples/Aseprite.md)
* [Godot](examples/Godot.md)
* [minetest](examples/minetest.md)
