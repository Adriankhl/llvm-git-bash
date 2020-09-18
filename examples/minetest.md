Compiling [minetest](https://github.com/minetest/minetest) is simple, follow the instruction in their [repo](https://github.com/minetest/minetest), and install all the libraries with vcpkg, in my case, vcpkg is located at `/d/packages/vcpkg`
```
vcpkg install irrlicht zlib curl[winssl] openal-soft libvorbis libogg sqlite3 freetype luajit gmp jsoncpp --triplet x64-windows
git clone https://github.com/minetest/minetest.git
mkdir minetest/compile
cd minetest/compile
cmake .. -GNinja -DCMAKE_TOOLCHAIN_FILE=/d/packages/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows -DCMAKE_RC_COMPILER_INIT=llvm-rc -DCMAKE_BUILD_TYPE=Release -DENABLE_GETTEXT=OFF -DENABLE_CURSES=OFF -DENABLE_SYSTEM_JSONCPP=ON
```
