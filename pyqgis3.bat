@echo off 
set OSGEO4W_ROOT=C:\OSGeo4W
@IF EXIST C:\OsGeo4W64\nul set OSGEO4W_ROOT=C:\OSGeo4W64
@IF EXIST C:\OsGeo4W32\nul set OSGEO4W_ROOT="C:\OSGeo4W32
call "%OSGEO4W_ROOT%\bin\o4w_env.bat" 
call "%OSGEO4W_ROOT%\bin\qt5_env.bat" 
call "%OSGEO4W_ROOT%\bin\py3_env.bat" 
path %~dp0;%OSGEO4W_ROOT%\apps\qgis\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis
set GDAL_FILENAME_IS_UTF8=YES
set VSI_CACHE=TRUE
set VSI_CACHE_SIZE=1000000
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis\qtplugins;%OSGEO4W_ROOT%\apps\Qt5\plugins
set PYTHONHOME=%OSGEO4W_ROOT%\apps\Python37
set PYTHONPATH=%OSGEO4W_ROOT%\apps\qgis\python;%PYTHONPATH%
set PYTHONPATH=%OSGEO4W_ROOT%\apps\Python37\Lib\site-packages;%PYTHONPATH%
rem cd <path to cadastre files>
cmd.exe
