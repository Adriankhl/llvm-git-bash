# Overview

This is a guide of compiling softwares with [LLVM](https://github.com/llvm/llvm-project) using [Git Bash](https://github.com/git-for-windows/git) shell. 

Visual Studio comes with an out-of-the-box support of LLVM, cmake, and ninja. However, if you don't want to rely on Microsoft's workflow too much, it is not that easy to configure your environment correctly. This guide provide informations that help you to set up your development environment. 

You still have to use Windows SDK and maybe some other tools from Visual Studio. The motivation of this guide is to minimize the dependency on Microsoft's tools and the Visual Studio IDE, so that you pick your favorite alternative (open source) tools to develop your software, while you should be able to easily go back to the powerful Visual Studio to develop your project if you want to do so. 

Note: you may also consider the [MSYS2](https://www.msys2.org/) project if you want to go further and drop the dependency on Windows SDK, check [llvm-mingw](https://github.com/mstorsjo/llvm-mingw.git) for a working version of LLVM-MINGW toolchain.

## Prerequisites

* [Git Bash](https://gitforwindows.org/) (you may also consider the built-in Git Bash in [cmder](https://github.com/cmderdev/cmder/releases))
* [LLVM](https://github.com/llvm/llvm-project/releases)
* [Python](https://www.python.org/downloads/) and `pandas` package.
* [Visual Studio](https://visualstudio.microsoft.com/downloads/) (Minimally, you can download `Build Tools for Visual Studio 2019` and install MSVC and Windows 10 SDK, you can also use the bundled cmake, ninja, and LLVM)

Optional recommendations:

* [CMake](https://cmake.org/download)
* [Ninja](https://github.com/ninja-build/ninja/releases)

Say you install LLVM in `D:\Program\LLVM`, the path in Git Bash is represented as `/d/Program/LLVM`. The binaries of LLVM should be located inside `/d/Program/LLVM/bin`. Add `export PATH='/d/Program/LLVM/bin':$PATH` in your `~/.bashrc` so that the binaries (`clang.exe`, `lld.exe`, etc.) can be found automatically. Do the same if you installed python, cmake or ninja. You may also add the `Scripts` folder of your python to the `PATH` such that you can use `pip`. Then you can install `pandas` by `pip install pandas`

## Extract environment from developer powershell

Visual Studio 2019 comes with a Developer Powershell, where environment variables are pre-defined. You can view the variables by opening the shell and run:

`Get-ChildItem Env: | Format-Table -AutoSize -wrap`

Run the following command export the variables into a csv file `Env.csv`.

`Get-ChildItem Env: | Export-CSV Env.csv`

Now, you have to turn the `Path`, `LIB`, and `INCLUDE` variables to a suitable format for Git Bash. 
Copy or download the [python script](script/python/env_translate.py), run:

`python env_translate.py Env.csv`

4 files will be generated: 

* `env_original.sh`: Original format of environment variables
* `env_all.sh`: Converted Git Bash format of environment variables, cannot be executed directly since `(x86)` in variable name is not allowed in Git Bash
* `env.sh`: export `PATH`, `LIB`, and `INCLUDE` in Git Bash format
* `env64.sh`: basically `env.sh` where all `x86` are converted to `x64` to use 64bit library (excrept `(x86)` which should only exists in the name `Program Files (x86)`)

Depends on whether you want to build 32bit or 64bit binary, do `source env.sh` or `source env64.sh` in your `~/.bashrc`.

Important: there is a `python` in the `env.sh` (and `env64.sh`) but it is not something that you should use, make sure that your working python path is in front of the `PATH` you just add, check `which python` to see if it correctly finds your python.

## Recommended extra step

After you execute `source env.sh`, some tools that are provided by Git Bash are overrode by the tools provided by Microsoft since they have exactly the same name, such as `find` or `link`. Therefore, it is recommended that you can use alias or bash script to create two commands to change the `PATH` variable - one prepare for the development environment and one return to the original Git Bash environment. You can run something like `llvmdev` before you want to compile your project and run something like `undev` if you want to `find` a file afterwards.

## Examples

As far as I know, not many open source softwares can be successfully compiled if you strictly follow the approach in this guide. For example, if the project is developed based on a `.sln` file, you have no choice but to use `MSBuild` and/or Visual Studio IDE. Fortunately, unlike MinGW, LLVM tools are designed to be an (almost) drop-in replacement of Microsoft's tools, zero or relatively small tweaks are necessary if you want to build CMake or Scons projects which are orginally designed to build with Visual Studio. Here are some examples that can be successfully built, feel free to make more suggestions by PR.

* [Aseprite](examples/Aseprite.md)
* [Godot](examples/Godot.md)

