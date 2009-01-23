
Summary: A git GUI viewer
Name: qgit
Version: 2.2
Release: %mkrel 1
Source0: http://ovh.dl.sourceforge.net/sourceforge/qgit/%{name}-%{version}.tar.bz2
Patch0: %{name}-2.2-qmake.patch
License: GPL
Group: Development/Other
Url: http://sourceforge.net/projects/qgit
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scons
BuildRequires: qt4-devel
Requires: git-core

%define qtdir /usr/lib/qt4

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
%setup -q -n %{name}
%patch0 -p1 -b .qmake

# fix permissions
chmod a-x src/*.{cpp,h}

%build
qmake %{name}.pro
%make

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
