%define name pyogg
%define version 1.3
%define release %mkrel 8

Summary: A wrapper for the Ogg libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.andrewchatham.com/pyogg/download/%{name}-%{version}.tar.bz2
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libogg-devel
BuildRequires: libpython-devel
Url: http://www.andrewchatham.com/pyogg/

%description
pyogg is a Python wrapper for the Ogg libraries.

There's not a whole lot you can do with this module by itself. You'll
probably also want the ogg.vorbis module, which can be found wherever
you got this.

You can now write Python programs to encode and decode Ogg Vorbis
files (encoding is quite a bit more involved). The module is
self-documenting, though I need to update quite a bit of it.

%prep
%setup -q

%build
python config_unix.py
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%dir %{_includedir}/python?.?/pyogg/
%{_includedir}/python?.?/pyogg/pyogg.h
%py_platsitedir/*


