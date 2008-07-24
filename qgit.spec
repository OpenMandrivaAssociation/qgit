
Summary: A git GUI viewer
Name: qgit
Version: 1.5.7
Release: %mkrel 3
Source0: http://ovh.dl.sourceforge.net/sourceforge/qgit/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://sourceforge.net/projects/qgit
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scons 
BuildRequires: qt3-devel
Requires: git-core

%define qtdir /usr/lib/qt3

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
%setup -q

%build

export QTDIR=%{qtdir}
%configure --with-qt-libraries=$QTDIR/%{_lib}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc README



