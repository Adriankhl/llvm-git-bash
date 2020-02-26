# Aseprite
[Aseprite](https://github.com/aseprite/aseprite) is a pixel-art editor and a sprite editor. Note that it is a "source available" software instead of an "open source" software. Basically the build follow the [instruction](https://github.com/aseprite/aseprite/blob/master/INSTALL.md) with a few tweaks. You should use python 2 instead of python 3 for this, just `export` your python 2 to `PATH`. Remember to prepare your environment as mentioned in the [guide](https://github.com/Adriankhl/llvm-git-bash/blob/master/README.md).

* Tested version: v1.2.16.3

Clone the repositories:

```
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
git clone -b aseprite-m71 https://github.com/aseprite/skia.git
```
As of v1.2.16.3, a small tweak is required, you either my fork:

`git clone -b llvm https://github.com/Adriankhl/aseprite.git`

or 

`git clone -b v1.2.16.3 https://github.com/aseprite/aseprite.git`

and then manually edit `src/CMakeLists.txt`: 

modify `set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /LTCG")` to

```
if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fuse-ld=lld -flto=thin")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fuse-ld=lld -flto=thin")
else()
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /LTCG")
endif()
```

Now modify the `clang_win` and `win_vc` below to your LLVM and Visual studio `VC` folders and do:
```
export PATH="${PWD}/depot_tools:${PATH}"
cd depot_tools
gclient sync
cd ../skia
python tools/git-sync-deps
gn gen out/Release --args='is_official_build=true skia_use_system_expat=false skia_use_system_libjpeg_turbo=false skia_use_system_libpng=false skia_use_system_libwebp=false skia_use_system_zlib=false target_cpu="x64" cc="clang" cxx="clang++" clang_win="D:\Program\LLVM" win_vc="D:\Program\VisualStudio\2019\BuildTools\VC"'
ninja -C out/Release skia
```
Ignore the `Error: client not configured; see 'gclient config'`.


Finally, modify the `SKIA_DIR` and `SKIA_OUT_DIR` below to your skia directories, recent cmake can recognize the Git Bash directory name style (`/d/something`) if you run it in the shell. And run: 

```
cd ../aseprite
git submodule update --init --recursive
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLAF_OS_BACKEND=skia -DSKIA_DIR=/d/git/aseprite-project/skia -DSKIA_OUT_DIR=/d/git/aseprite-project/skia/out/Release -DCMAKE_C_FLAGS="-mssse3 -msse4.1" -DCMAKE_CXX_FLAGS=" /EHsc" -G Ninja ..
ninja aseprite
```

Now you should have `aseprite.exe` in `bin`.
