
Summary: A git GUI viewer
Name: qgit
Version: 2.11
Release: 1
Source0: https://github.com/tibirna/qgit/archive/refs/tags/qgit-%{version}.tar.gz
License: GPL
Group: Development/Other
Url: https://sourceforge.net/projects/qgit
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scons
BuildRequires: qt5-devel
BuildRequires:	cmake ninja
Requires: git-core

%define qtdir /usr/lib/qt5

%description
With qgit you will be able to browse revisions history, view patch content
and changed
files, graphically following different development branches.

Main features
- View revisions, diffs, files history, files annotation, archive tree.
- Commit changes visually cherry picking modified files.
- Apply or format patch series from selected commits, drag and
  drop commits between two instances of qgit.
- qgit implements a GUI for the most common StGIT commands like push/pop
  and apply/format patches. You can also create new patches or refresh
  current top one using the same semantics of git commit, i.e. cherry
  picking single modified files.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
%cmake_qt5 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%defattr(-,root,root)
%{_bindir}/qgit
%{_datadir}/applications/qgit.desktop
%{_datadir}/icons/hicolor/*/apps/qgit.*
%{_datadir}/metainfo/qgit.appdata.xml
