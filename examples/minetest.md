Compiling [minetest](https://github.com/minetest/minetest) is simple, follow the instruction in their [repo](https://github.com/minetest/minetest), and install all the libraries with vcpkg, in my case: `/d/packages/vcpkg`
```
git clone https://github.com/minetest/minetest.git
mkdir minetest/compile
cd minetest/compile
cmake .. -GNinja -DCMAKE_TOOLCHAIN_FILE=/d/packages/vcpkg/scripts/buildsystems/vcpkg.cmake -DVCPKG_TARGET_TRIPLET=x64-windows -DCMAKE_BUILD_TYPE=Release -DENABLE_GETTEXT=0 -DENABLE_CURSES=0 -DCMAKE_RC_COMPILER_INIT=llvm-rc
```
