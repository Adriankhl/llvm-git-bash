# Godot

[Godot](https://github.com/godotengine/godot) is an assume open source game engine. The build instruction is based on [Godot documentation](https://docs.godotengine.org/en/3.2/development/compiling/compiling_for_windows.html). Remember to prepare your environment as mentioned in the [guide](https://github.com/Adriankhl/llvm-git-bash/blob/master/README.md). Additionally, install `scons` by `pip install scons`

* Tested version: 3.2

Clone the repository, my fork is based on the `3.2-stable` branch with a few tweaks to the scons script:

`git clone -b 3.2-llvm-win https://github.com/Adriankhl/godot.git`

Then simply do 

`scons -j6 platform=windows target=release_debug bits=64 use_llvm=yes use_thinlto=yes`

You will see `godot.windows.opt.tools.64.exe` in `bin`.
