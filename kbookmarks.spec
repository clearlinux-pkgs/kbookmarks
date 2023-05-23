#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kbookmarks
Version  : 5.106.0
Release  : 64
URL      : https://download.kde.org/stable/frameworks/5.106/kbookmarks-5.106.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.106/kbookmarks-5.106.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.106/kbookmarks-5.106.0.tar.xz.sig
Summary  : Support for bookmarks and the XBEL format
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-3.0
Requires: kbookmarks-data = %{version}-%{release}
Requires: kbookmarks-lib = %{version}-%{release}
Requires: kbookmarks-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kiconthemes-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KBookmarks
Bookmarks management library
## Introduction
KBookmarks lets you access and manipulate bookmarks stored using the
[XBEL format][1].

%package data
Summary: data components for the kbookmarks package.
Group: Data

%description data
data components for the kbookmarks package.


%package dev
Summary: dev components for the kbookmarks package.
Group: Development
Requires: kbookmarks-lib = %{version}-%{release}
Requires: kbookmarks-data = %{version}-%{release}
Provides: kbookmarks-devel = %{version}-%{release}
Requires: kbookmarks = %{version}-%{release}

%description dev
dev components for the kbookmarks package.


%package lib
Summary: lib components for the kbookmarks package.
Group: Libraries
Requires: kbookmarks-data = %{version}-%{release}
Requires: kbookmarks-license = %{version}-%{release}

%description lib
lib components for the kbookmarks package.


%package license
Summary: license components for the kbookmarks package.
Group: Default

%description license
license components for the kbookmarks package.


%prep
%setup -q -n kbookmarks-5.106.0
cd %{_builddir}/kbookmarks-5.106.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684849261
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684849261
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kbookmarks
cp %{_builddir}/kbookmarks-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kbookmarks/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kbookmarks-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kbookmarks/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kbookmarks-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kbookmarks/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kbookmarks-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kbookmarks/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kbookmarks-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kbookmarks/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kbookmarks-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kbookmarks/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kbookmarks-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kbookmarks/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kbookmarks5_qt.qm
/usr/share/qlogging-categories5/kbookmarks.categories
/usr/share/qlogging-categories5/kbookmarks.renamecategories

%files dev
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Bookmarks.so
/usr/include/KF5/KBookmarks/KBookmark
/usr/include/KF5/KBookmarks/KBookmarkAction
/usr/include/KF5/KBookmarks/KBookmarkActionInterface
/usr/include/KF5/KBookmarks/KBookmarkActionMenu
/usr/include/KF5/KBookmarks/KBookmarkContextMenu
/usr/include/KF5/KBookmarks/KBookmarkDialog
/usr/include/KF5/KBookmarks/KBookmarkDomBuilder
/usr/include/KF5/KBookmarks/KBookmarkManager
/usr/include/KF5/KBookmarks/KBookmarkMenu
/usr/include/KF5/KBookmarks/KBookmarkOwner
/usr/include/KF5/KBookmarks/KonqBookmarkMenu
/usr/include/KF5/KBookmarks/kbookmark.h
/usr/include/KF5/KBookmarks/kbookmarkaction.h
/usr/include/KF5/KBookmarks/kbookmarkactioninterface.h
/usr/include/KF5/KBookmarks/kbookmarkactionmenu.h
/usr/include/KF5/KBookmarks/kbookmarkcontextmenu.h
/usr/include/KF5/KBookmarks/kbookmarkdialog.h
/usr/include/KF5/KBookmarks/kbookmarkdombuilder.h
/usr/include/KF5/KBookmarks/kbookmarkexporter.h
/usr/include/KF5/KBookmarks/kbookmarkimporter.h
/usr/include/KF5/KBookmarks/kbookmarkimporter_ie.h
/usr/include/KF5/KBookmarks/kbookmarkimporter_ns.h
/usr/include/KF5/KBookmarks/kbookmarkimporter_opera.h
/usr/include/KF5/KBookmarks/kbookmarkmanager.h
/usr/include/KF5/KBookmarks/kbookmarkmenu.h
/usr/include/KF5/KBookmarks/kbookmarkowner.h
/usr/include/KF5/KBookmarks/kbookmarks_export.h
/usr/include/KF5/KBookmarks/kbookmarks_version.h
/usr/include/KF5/KBookmarks/konqbookmarkmenu.h
/usr/lib64/cmake/KF5Bookmarks/KF5BookmarksConfig.cmake
/usr/lib64/cmake/KF5Bookmarks/KF5BookmarksConfigVersion.cmake
/usr/lib64/cmake/KF5Bookmarks/KF5BookmarksTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Bookmarks/KF5BookmarksTargets.cmake
/usr/lib64/libKF5Bookmarks.so
/usr/lib64/qt5/mkspecs/modules/qt_KBookmarks.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Bookmarks.so.5
/V3/usr/lib64/libKF5Bookmarks.so.5.106.0
/usr/lib64/libKF5Bookmarks.so.5
/usr/lib64/libKF5Bookmarks.so.5.106.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kbookmarks/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kbookmarks/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kbookmarks/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kbookmarks/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kbookmarks/e712eadfab0d2357c0f50f599ef35ee0d87534cb
