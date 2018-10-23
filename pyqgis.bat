@echo off
set OSGEO4W_ROOT=C:\OSGeo4W
IF EXIST C:\OsGeo4W64\nul set OSGEO4W_ROOT=C:\OSGeo4W64
IF EXIST C:\OsGeo4W32\nul set OSGEO4W_ROOT=C:\OSGeo4W32
call "%OSGEO4W_ROOT%\bin\o4w_env.bat" >NUL
IF EXIST "%OSGEO4W_ROOT%\bin\qt5_env.bat" call "%OSGEO4W_ROOT%\bin\qt5_env.bat"
@echo off
path %~dp0;%OSGEO4W_ROOT%\apps\qgis-ltr\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis-ltr
set GDAL_FILENAME_IS_UTF8=YES
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis-ltr\qtplugins;%OSGEO4W_ROOT%\apps\qt4\plugins
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis-ltr\python;%PYTHONPATH%
rem CD <path to cadastre files>
cmd.exe
