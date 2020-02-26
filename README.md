# Overview
This is a guide of compiling softwares with [LLVM](https://github.com/llvm/llvm-project) using [Git Bash](https://github.com/git-for-windows/git) shell. 

Visual Studio comes with an out-of-the-box support of LLVM, cmake, and ninja. However, if you don't want to rely on Microsoft's workflow too much, it is not that easy to configure your environment correctly. This guide provide informations that help you to set up your development environment. 

You still have to use Windows SDK and maybe some other tools from Visual Studio. The motivation of this guide is to minimize the dependency on Microsoft's tools, so that you can rely on other (open source) tools develop your software, while you should be able to go back to the powerful Visual Studio to develop your project if you want to do so. 

Note: you may also consier the [MSYS2](https://www.msys2.org/) project if you want to go further and drop the dependency on Windows SDK. 

## Prerequisites
* [Git Bash](https://gitforwindows.org/) (you may also consider the built-in Git Bash in [cmder](https://github.com/cmderdev/cmder/releases))
* [LLVM](https://github.com/llvm/llvm-project/releases)
* [Python](https://www.python.org/downloads/)

Optional recommendations:

* [CMake](https://cmake.org/download)
* [Ninja](https://github.com/ninja-build/ninja/releases)

In my opinion, CMake + Ninja + LLVM is a really nice combo for software development on Windows.

## Extract environment from developer powershell

`Get-ChildItem Env: | Format-Table -AutoSize -wrap`
`Get-ChildItem Env: | Export-CSV Env.csv`
